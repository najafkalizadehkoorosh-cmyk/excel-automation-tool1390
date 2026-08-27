# Excel Automation Tool

A lightweight Windows-first desktop tool for cleaning, transforming, inspecting, batch-processing, and merging Excel/CSV data.

## Features

- Clean `.csv`, `.xlsx`, and `.xlsm` files.
- Remove completely empty rows and columns.
- Trim and normalize text whitespace.
- Remove duplicate rows by default.
- Normalize column names to readable `snake_case`.
- Normalize likely email fields without inventing missing values.
- Profile missing values, duplicates, repeated values, empty text, and likely invalid emails.
- Apply ready-to-use workflow presets for general cleanup, customer contacts, and sales exports.
- Process an entire folder in batch mode with per-file error isolation.
- Merge multiple supported files into one output, with optional source-file tracking.
- Export CSV or Excel output.
- Export a readable HTML or JSON data-quality report.
- Run from a desktop GUI or CLI.
- Build a standalone Windows executable with GitHub Actions.

## Why it is local-first

The current desktop workflow processes selected spreadsheets locally. Core processing does not require uploading spreadsheet contents to a hosted service. Users should still review important outputs and maintain backups.

## Desktop app

Run the Python version:

```bash
python main.py
```

Choose one workflow:

- **Clean one file** — apply a selected preset, clean, transform, and generate a quality report.
- **Process a folder** — clean and transform every supported file into `cleaned_output`.
- **Merge a folder** — combine supported files into `merged.xlsx` and optionally add `source_file`.

## Ready-to-use presets

- `general_cleanup` — default safe cleanup for ordinary spreadsheets.
- `customer_contacts` — customer/contact export cleanup, including likely email fields.
- `sales_export` — sales export cleanup while preserving duplicate transaction rows.

CLI example:

```bash
python -m src.excel_automation.cli customers.xlsx --preset customer_contacts --quality-report customers_quality.html
```

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

Keep duplicate rows in the default workflow:

```bash
python -m src.excel_automation.cli input.csv --keep-duplicates
```

Skip deterministic transformations:

```bash
python -m src.excel_automation.cli input.xlsx --no-transform
```

Generate a JSON or HTML quality report:

```bash
python -m src.excel_automation.cli input.xlsx --quality-report quality.html
python -m src.excel_automation.cli input.xlsx --quality-report quality.json
```

## Quick start

See [`docs/quickstart.md`](docs/quickstart.md).

## Project structure

```text
.
├── main.py
├── requirements.txt
├── pyproject.toml
├── CHANGELOG.md
├── docs/
│   ├── index.html
│   ├── quickstart.md
│   ├── privacy.html
│   ├── terms.html
│   ├── PRIVACY_CHECKLIST.md
│   └── RELEASE_CHECKLIST.md
├── src/
│   └── excel_automation/
│       ├── __init__.py
│       ├── batch.py
│       ├── cleaner.py
│       ├── cli.py
│       ├── gui.py
│       ├── merge.py
│       ├── presets.py
│       ├── quality.py
│       ├── quality_report.py
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

Windows builds are produced by GitHub Actions. Version tags such as `v0.5.0` can trigger the release workflow and attach the standalone Windows executable to a GitHub Release.

No paid infrastructure is required for the current desktop MVP.

## Status

**Pre-release MVP — 0.5.0.** The core desktop workflows are implemented and tested in CI; commercial distribution still requires final real-world validation, legal review for the intended market, and a lawful payment/distribution setup.

## Roadmap

1. More customer-specific presets and configurable rules.
2. Background processing and better progress reporting.
3. Optional web product only if usage data justifies hosted infrastructure.
4. Automated support, analytics, billing, backups, and monitoring for a future hosted version.

## License

MIT License.
