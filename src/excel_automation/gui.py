"""Desktop graphical interface for Excel Automation Tool."""

import json
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from .batch import process_folder
from .cli import run


class ExcelAutomationApp(tk.Tk):
    """Desktop UI for single-file and batch Excel/CSV processing."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Excel Automation Tool")
        self.geometry("800x650")
        self.minsize(700, 560)
        self.input_path: Path | None = None
        self.batch_mode = tk.BooleanVar(value=False)
        self.remove_duplicates = tk.BooleanVar(value=True)
        self._build_ui()

    def _build_ui(self) -> None:
        container = ttk.Frame(self, padding=28)
        container.pack(fill="both", expand=True)

        ttk.Label(container, text="Excel Automation Tool", font=("TkDefaultFont", 20, "bold")).pack(anchor="center", pady=(0, 8))
        ttk.Label(container, text="Clean files, detect data-quality problems, and automate folders.").pack(anchor="center", pady=(0, 24))

        source = ttk.LabelFrame(container, text="Input", padding=16)
        source.pack(fill="x")
        self.file_label = ttk.Label(source, text="No file or folder selected")
        self.file_label.pack(side="left", fill="x", expand=True)
        self.choose_button = ttk.Button(source, text="Choose file", command=self.choose_input)
        self.choose_button.pack(side="right")

        options = ttk.LabelFrame(container, text="Options", padding=16)
        options.pack(fill="x", pady=18)
        ttk.Checkbutton(options, text="Batch mode (process every supported file in a folder)", variable=self.batch_mode, command=self._update_mode).pack(anchor="w")
        ttk.Checkbutton(options, text="Remove duplicate rows", variable=self.remove_duplicates).pack(anchor="w", pady=(8, 0))
        ttk.Label(options, text="Quality checks include missing values, repeated values, empty text, and likely invalid email values.").pack(anchor="w", pady=(8, 0))

        self.progress = ttk.Progressbar(container, mode="indeterminate")
        self.progress.pack(fill="x", pady=(4, 12))
        self.process_button = ttk.Button(container, text="Process", command=self.process_input)
        self.process_button.pack(anchor="center")

        self.result = tk.Text(container, height=17, wrap="word", state="disabled")
        self.result.pack(fill="both", expand=True, pady=(18, 0))

    def _update_mode(self) -> None:
        self.choose_button.config(text="Choose folder" if self.batch_mode.get() else "Choose file")
        self.input_path = None
        self.file_label.config(text="No file or folder selected")

    def choose_input(self) -> None:
        if self.batch_mode.get():
            selected = filedialog.askdirectory(title="Select folder")
        else:
            selected = filedialog.askopenfilename(
                title="Select Excel or CSV file",
                filetypes=[("Excel/CSV files", "*.csv *.xlsx *.xlsm"), ("CSV files", "*.csv"), ("Excel files", "*.xlsx *.xlsm")],
            )
        if selected:
            self.input_path = Path(selected)
            self.file_label.config(text=str(self.input_path))

    def _show_result(self, text: str) -> None:
        self.result.config(state="normal")
        self.result.delete("1.0", "end")
        self.result.insert("1.0", text)
        self.result.config(state="disabled")

    def process_input(self) -> None:
        if self.input_path is None:
            messagebox.showwarning("No input", "Please choose a file or folder first.")
            return

        self.progress.start(10)
        self.process_button.config(state="disabled")
        self.update_idletasks()

        try:
            if self.batch_mode.get():
                results = process_folder(self.input_path, keep_duplicates=not self.remove_duplicates.get())
                ok = sum(item.get("status") == "ok" for item in results)
                failed = len(results) - ok
                report = f"Batch processing complete!\n\nFiles found: {len(results)}\nSuccessful: {ok}\nFailed: {failed}\n\n{json.dumps(results, indent=2, ensure_ascii=False)}"
            else:
                summary = run(str(self.input_path), keep_duplicates=not self.remove_duplicates.get())
                before = summary["quality_before"]
                after = summary["quality_after"]
                report = (
                    "Processing complete!\n\n"
                    f"Rows: {summary['rows']}\nColumns: {summary['columns']}\n"
                    f"Missing cells after cleaning: {summary['missing_cells']}\n"
                    f"Duplicate rows after cleaning: {summary['duplicate_rows']}\n\n"
                    f"Quality issues before: {before['issue_count']}\n"
                    f"Quality issues after: {after['issue_count']}\n\n"
                    f"Output: {summary['output_file']}\n\n"
                    f"Detected issues:\n{json.dumps(before['issues'], indent=2, ensure_ascii=False)}"
                )

            self._show_result(report)
            messagebox.showinfo("Done", "Processing completed.")
        except (FileNotFoundError, NotADirectoryError, ValueError, OSError, RuntimeError) as exc:
            self._show_result(f"Error: {exc}")
            messagebox.showerror("Processing error", str(exc))
        finally:
            self.progress.stop()
            self.process_button.config(state="normal")


def main() -> None:
    app = ExcelAutomationApp()
    app.mainloop()


if __name__ == "__main__":
    main()
