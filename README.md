# Excel Automation Tool

Automate common Excel and CSV cleanup tasks from the command line.

## Current features

- Read `.csv`, `.xlsx`, and `.xlsm` files.
- Remove completely empty rows and columns.
- Trim whitespace from text cells.
- Remove duplicate rows by default.
- Export cleaned data to CSV or Excel.
- Print a JSON summary of the processed data.
- Automated tests and GitHub Actions CI.

## Requirements

- Python 3.10+

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the tool with a CSV or Excel file:

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

Version 0.1.0 — initial MVP.

The project is intentionally small at first. Future versions can add configurable cleaning rules, richer reports, a graphical/web interface, and workflow automation.

## License

MIT License.
