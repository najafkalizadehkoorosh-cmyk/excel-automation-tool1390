# Excel Automation Tool

A lightweight desktop tool for cleaning and processing Excel and CSV files.

## Current features

- Choose `.csv`, `.xlsx`, or `.xlsm` files from a desktop UI.
- Remove completely empty rows and columns.
- Trim whitespace from text cells.
- Remove duplicate rows by default.
- Export cleaned data to Excel.
- Show a processing summary.
- Command-line workflow for automation.
- Automated tests and GitHub Actions CI.

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

Choose an Excel/CSV file, select whether duplicate rows should be removed, and click **Process file**. The cleaned file is written next to the input file.

## Command-line usage

```bash
python -m src.excel_automation.cli input.xlsx
```

Choose an output file:

```bash
python -m src.excel_automation.cli input.xlsx --output output.xlsx
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
│       ├── cleaner.py
│       ├── cli.py
│       ├── gui.py
│       ├── reader.py
│       └── reporter.py
├── tests/
│   ├── test_cleaner.py
│   ├── test_reader.py
│   └── test_reporter.py
└── .github/
    └── workflows/
        └── ci.yml
```

## Status

Version 0.2.0 — desktop MVP.

## Roadmap

- Configurable cleaning rules
- Richer reports and data quality checks
- Drag-and-drop support
- Batch processing
- Web version
- User-focused workflow templates

## License

MIT License.
