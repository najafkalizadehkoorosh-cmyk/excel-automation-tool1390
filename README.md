# Excel Automation Tool

A lightweight desktop tool for cleaning and batch-processing Excel and CSV files.

## Features

- Desktop GUI for Windows and other Python/Tkinter environments.
- Process `.csv`, `.xlsx`, and `.xlsm` files.
- Remove completely empty rows and columns.
- Trim whitespace from text cells.
- Remove duplicate rows by default.
- Export cleaned data to Excel.
- Show a data-quality summary.
- Batch-process an entire folder.
- Command-line workflow for automation.
- Unit tests and GitHub Actions CI.

## Requirements

- Python 3.10+
- Tkinter (normally included with standard Python installations on Windows).

Install dependencies:

```bash
pip install -r requirements.txt
```

## Desktop usage

Run:

```bash
python main.py
```

For one file, choose **Choose file**, select the cleaning options, and click **Process**.

For many files, enable **Batch mode**, choose a folder, and click **Process**. Cleaned files are written into a `cleaned_output` folder inside the selected directory.

## Command-line usage

Single file:

```bash
python -m src.excel_automation.cli input.xlsx
```

Custom output:

```bash
python -m src.excel_automation.cli input.xlsx --output output.xlsx
```

Batch folder:

```bash
python -m src.excel_automation.cli ./data --batch
```

Batch with a custom output directory:

```bash
python -m src.excel_automation.cli ./data --batch --output ./processed
```

Keep duplicate rows:

```bash
python -m src.excel_automation.cli input.csv --keep-duplicates
```

## Project structure

```text
.
├── main.py
├── requirements.txt
├── pyproject.toml
├── src/
│   └── excel_automation/
│       ├── __init__.py
│       ├── batch.py
│       ├── cleaner.py
│       ├── cli.py
│       ├── gui.py
│       ├── reader.py
│       └── reporter.py
├── tests/
│   ├── test_batch.py
│   ├── test_cleaner.py
│   ├── test_reader.py
│   └── test_reporter.py
└── .github/
    └── workflows/
        └── ci.yml
```

## Status

Version 0.3.0 — desktop MVP with batch automation.

## Roadmap

- Configurable cleaning rules and column-specific transformations.
- Better data-quality and validation reports.
- Drag-and-drop support.
- Windows executable packaging.
- Web version for broader distribution.
- User-focused workflow templates and a paid professional tier.

## License

MIT License.
