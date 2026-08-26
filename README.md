# Excel Automation Tool

A lightweight desktop automation tool for cleaning, transforming, profiling, batch-processing, and merging Excel/CSV data.

## What it does

- Clean `.csv`, `.xlsx`, and `.xlsm` files.
- Remove completely empty rows and columns.
- Trim and normalize text whitespace.
- Remove duplicate rows by default.
- Normalize column names to readable `snake_case`.
- Normalize likely email fields without inventing missing values.
- Profile missing values, duplicate rows, repeated values, empty text, and likely invalid emails.
- Process an entire folder in batch mode with per-file error isolation.
- Merge multiple supported files into one output, with optional source-file tracking.
- Export CSV or Excel output.
- Run from a desktop GUI or CLI.

## Requirements

- Python 3.10+
- Tkinter (normally included with Python on Windows).

Install dependencies:

```bash
pip install -r requirements.txt
```

## Desktop app

```bash
python main.py
```

Choose one workflow:

- **Clean one file** — clean, transform, and report on one file.
- **Process a folder** — clean and transform every supported file into `cleaned_output`.
- **Merge a folder** — combine supported files into `merged.xlsx` and optionally add `source_file`.

## CLI

Single file:

```bash
python -m src.excel_automation.cli input.xlsx
```

Batch:

```bash
python -m src.excel_automation.cli ./data --batch --output ./processed
```

Merge:

```bash
python -m src.excel_automation.cli ./data --merge --output merged.xlsx
```

Merge without source tracking:

```bash
python -m src.excel_automation.cli ./data --merge --output merged.xlsx --no-source-column
```

Keep duplicate rows:

```bash
python -m src.excel_automation.cli input.csv --keep-duplicates
```

Skip deterministic transformations:

```bash
python -m src.excel_automation.cli input.xlsx --no-transform
```

## Quality and safety

The tool favors deterministic, explainable transformations. It does not silently invent values. Quality diagnostics are separated from cleaning so users can review issues before applying more aggressive business-specific rules.

The current desktop version processes selected files locally by default.

## Project structure

```text
.
├── main.py
├── requirements.txt
├── pyproject.toml
├── docs/
│   ├── index.html
│   ├── privacy.html
│   └── terms.html
├── src/
│   └── excel_automation/
│       ├── __init__.py
│       ├── batch.py
│       ├── cleaner.py
│       ├── cli.py
│       ├── gui.py
│       ├── merge.py
│       ├── quality.py
│       ├── reader.py
│       ├── reporter.py
│       └── transform.py
├── tests/
└── .github/workflows/
    ├── ci.yml
    ├── windows-build.yml
    └── release.yml
```

## Release

Windows builds are produced by GitHub Actions. A version tag such as `v0.4.0` triggers the release workflow and attaches the Windows executable to a GitHub Release.

No paid infrastructure is required for the current desktop MVP.

## Status

**Pre-release MVP — 0.4.0 direction.** The core desktop workflows are implemented; public commercial release still requires real-world Windows validation, product/legal review, and a lawful payment/distribution setup.

## Roadmap

1. Configurable workflow presets.
2. Better validation rules and exportable quality reports.
3. Drag-and-drop and background processing.
4. Signed Windows installer when distribution requirements are validated.
5. Optional web product and accounts only if market validation justifies the added infrastructure.
6. Automated support, analytics, billing, backups, and monitoring for a future hosted version.

## License

MIT License.
