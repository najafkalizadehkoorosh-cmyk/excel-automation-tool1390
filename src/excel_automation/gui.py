"""Desktop graphical interface for Excel Automation Tool."""

from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from .cli import run


class ExcelAutomationApp(tk.Tk):
    """Small desktop UI for selecting, cleaning, and exporting a data file."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Excel Automation Tool")
        self.geometry("680x470")
        self.minsize(620, 420)
        self.input_path: Path | None = None
        self._build_ui()

    def _build_ui(self) -> None:
        container = ttk.Frame(self, padding=28)
        container.pack(fill="both", expand=True)

        ttk.Label(
            container,
            text="Excel Automation Tool",
            font=("TkDefaultFont", 20, "bold"),
        ).pack(anchor="center", pady=(0, 8))

        ttk.Label(
            container,
            text="Clean Excel and CSV files in a few clicks.",
        ).pack(anchor="center", pady=(0, 24))

        file_frame = ttk.LabelFrame(container, text="Input file", padding=16)
        file_frame.pack(fill="x")

        self.file_label = ttk.Label(file_frame, text="No file selected")
        self.file_label.pack(side="left", fill="x", expand=True)
        ttk.Button(file_frame, text="Choose file", command=self.choose_file).pack(side="right")

        options = ttk.LabelFrame(container, text="Cleaning options", padding=16)
        options.pack(fill="x", pady=18)

        self.remove_duplicates = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            options,
            text="Remove duplicate rows",
            variable=self.remove_duplicates,
        ).pack(anchor="w")
        ttk.Label(
            options,
            text="Empty rows/columns are removed and text whitespace is trimmed automatically.",
        ).pack(anchor="w", pady=(8, 0))

        self.progress = ttk.Progressbar(container, mode="indeterminate")
        self.progress.pack(fill="x", pady=(4, 12))

        self.process_button = ttk.Button(
            container, text="Process file", command=self.process_file
        )
        self.process_button.pack(anchor="center", pady=6)

        self.result = tk.Text(container, height=9, wrap="word", state="disabled")
        self.result.pack(fill="both", expand=True, pady=(18, 0))

    def choose_file(self) -> None:
        selected = filedialog.askopenfilename(
            title="Select Excel or CSV file",
            filetypes=[
                ("Excel/CSV files", "*.csv *.xlsx *.xlsm"),
                ("CSV files", "*.csv"),
                ("Excel files", "*.xlsx *.xlsm"),
            ],
        )
        if selected:
            self.input_path = Path(selected)
            self.file_label.config(text=str(self.input_path))

    def _show_result(self, text: str) -> None:
        self.result.config(state="normal")
        self.result.delete("1.0", "end")
        self.result.insert("1.0", text)
        self.result.config(state="disabled")

    def process_file(self) -> None:
        if self.input_path is None:
            messagebox.showwarning("No file", "Please choose an Excel or CSV file first.")
            return

        self.progress.start(10)
        self.process_button.config(state="disabled")
        self.update_idletasks()

        try:
            summary = run(
                str(self.input_path),
                keep_duplicates=not self.remove_duplicates.get(),
            )
            report = (
                "Processing complete!\n\n"
                f"Rows: {summary['rows']}\n"
                f"Columns: {summary['columns']}\n"
                f"Missing cells: {summary['missing_cells']}\n"
                f"Duplicate rows: {summary['duplicate_rows']}\n\n"
                f"Output: {summary['output_file']}"
            )
            self._show_result(report)
            messagebox.showinfo("Done", "Your cleaned file is ready.")
        except (FileNotFoundError, ValueError, OSError, RuntimeError) as exc:
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
