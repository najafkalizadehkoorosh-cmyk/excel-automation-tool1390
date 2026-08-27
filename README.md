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

## Example

The repository includes synthetic test data in [`examples/customer_contacts_sample.csv`](examples/customer_contacts_sample.csv). It contains no real customer information.

For the Customer Contacts preset:

```bash
python -m src.excel_automation.cli examples/customer_contacts_sample.csv --preset customer_contacts --quality-report customer_quality.html
```

## Beta testing

The public beta package includes:

- [`BETA_RELEASE.md`](BETA_RELEASE.md) — 10-minute trial and safety guide.
- [`FEEDBACK_TEMPLATE.md`](FEEDBACK_TEMPLATE.md) — structured feedback template.
- [`BETA_OUTREACH.md`](BETA_OUTREACH.md) — responsible, zero-budget outreach guidance.

Please use synthetic or non-sensitive sample data during public testing and review important outputs before business use.

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

## Commercialization

The project includes a zero-budget commercialization plan in [`docs/SALES_PLAN.md`](docs/SALES_PLAN.md). The target of $50/month is an illustrative goal, not a revenue guarantee.

The current repository uses the MIT License. Before selling a proprietary or exclusive build based on this repository, review the licensing and distribution model appropriately. The project does not contain a payment backend and does not activate paid services by default.

## Project structure

```text
.
├── main.py
├── requirements.txt
├── pyproject.toml
├── CHANGELOG.md
├── BETA_RELEASE.md
├── FEEDBACK_TEMPLATE.md
├── BETA_OUTREACH.md
├── examples/
├── docs/
├── src/
├── tests/
└── .github/workflows/
```

## Release

Windows builds are produced by GitHub Actions. Version tags such as `v0.5.1` can trigger the release workflow and attach the standalone Windows executable to a GitHub Release.

No paid infrastructure is required for the current desktop MVP.

## Status

**Release Candidate — 0.5.1.** The core desktop workflows are implemented and tested in CI. Public beta testing and commercial validation are the next steps; revenue is not guaranteed.

## Roadmap

1. More customer-specific presets and configurable rules.
2. Better progress reporting for large folders.
3. Optional hosted product only if validated demand justifies infrastructure.
4. Automated support, analytics, billing, backups, and monitoring for a future hosted version.

## License

MIT License.
