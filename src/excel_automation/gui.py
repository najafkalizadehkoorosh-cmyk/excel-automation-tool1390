"""Desktop graphical interface for Excel Automation Tool."""

from __future__ import annotations

import json
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from .batch import process_folder
from .cli import run
from .merge import merge_files


class ExcelAutomationApp(tk.Tk):
    """Desktop UI for single-file, batch, and merge workflows."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Excel Automation Tool")
        self.geometry("900x700")
        self.minsize(760, 620)
        self.input_path: Path | None = None
        self.mode = tk.StringVar(value="single")
        self.remove_duplicates = tk.BooleanVar(value=True)
        self.include_source = tk.BooleanVar(value=True)
        self._build_ui()

    def _build_ui(self) -> None:
        container = ttk.Frame(self, padding=28)
        container.pack(fill="both", expand=True)
        ttk.Label(container, text="Excel Automation Tool", font=("TkDefaultFont", 20, "bold")).pack(anchor="center")
        ttk.Label(container, text="Clean, inspect, transform, batch-process, or merge Excel/CSV data.").pack(anchor="center", pady=(4, 20))

        workflow = ttk.LabelFrame(container, text="1. Choose a workflow", padding=12)
        workflow.pack(fill="x")
        for value, label in (("single", "Clean one file"), ("batch", "Process a folder"), ("merge", "Merge a folder")):
            ttk.Radiobutton(workflow, text=label, value=value, variable=self.mode, command=self._update_mode).pack(side="left", padx=(0, 18))

        source = ttk.LabelFrame(container, text="2. Input", padding=12)
        source.pack(fill="x", pady=14)
        self.file_label = ttk.Label(source, text="No file or folder selected")
        self.file_label.pack(side="left", fill="x", expand=True)
        self.choose_button = ttk.Button(source, text="Choose file", command=self.choose_input)
        self.choose_button.pack(side="right")

        options = ttk.LabelFrame(container, text="3. Options", padding=12)
        options.pack(fill="x")
        self.duplicates_check = ttk.Checkbutton(options, text="Remove duplicate rows", variable=self.remove_duplicates)
        self.duplicates_check.pack(anchor="w")
        self.source_check = ttk.Checkbutton(options, text="Add source_file column when merging", variable=self.include_source)
        self.source_check.pack(anchor="w", pady=(6, 0))

        self.progress = ttk.Progressbar(container, mode="indeterminate")
        self.progress.pack(fill="x", pady=(16, 10))
        self.process_button = ttk.Button(container, text="Run workflow", command=self.process_input)
        self.process_button.pack(anchor="center")

        self.result = tk.Text(container, height=19, wrap="word", state="disabled")
        self.result.pack(fill="both", expand=True, pady=(16, 0))
        self._update_mode()

    def _update_mode(self) -> None:
        is_single = self.mode.get() == "single"
        is_merge = self.mode.get() == "merge"
        self.choose_button.config(text="Choose file" if is_single else "Choose folder")
        self.duplicates_check.config(state="normal" if not is_merge else "disabled")
        self.source_check.config(state="normal" if is_merge else "disabled")
        self.input_path = None
        self.file_label.config(text="No file or folder selected")

    def choose_input(self) -> None:
        if self.mode.get() == "single":
            selected = filedialog.askopenfilename(
                title="Select Excel or CSV file",
                filetypes=[
                    ("Excel/CSV files", "*.csv *.xlsx *.xlsm"),
                    ("CSV files", "*.csv"),
                    ("Excel files", "*.xlsx *.xlsm"),
                ],
            )
        else:
            selected = filedialog.askdirectory(title="Select folder")
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
            mode = self.mode.get()
            if mode == "single":
                summary = run(str(self.input_path), keep_duplicates=not self.remove_duplicates.get())
                report = json.dumps(summary, indent=2, ensure_ascii=False)
            elif mode == "batch":
                results = process_folder(self.input_path, keep_duplicates=not self.remove_duplicates.get())
                report = json.dumps(results, indent=2, ensure_ascii=False)
            else:
                output = self.input_path / "merged.xlsx"
                saved = merge_files(self.input_path, output, include_source=self.include_source.get())
                report = json.dumps({"status": "ok", "output_file": str(saved)}, indent=2, ensure_ascii=False)
            self._show_result(report)
            messagebox.showinfo("Done", "Workflow completed successfully.")
        except (FileNotFoundError, NotADirectoryError, ValueError, OSError, RuntimeError) as exc:
            self._show_result(f"Error: {exc}")
            messagebox.showerror("Processing error", str(exc))
        finally:
            self.progress.stop()
            self.process_button.config(state="normal")


def main() -> None:
    ExcelAutomationApp().mainloop()
