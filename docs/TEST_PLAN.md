# Test Plan

## Automated

CI should run the pytest suite on pushes to `main` and pull requests.

## Windows release smoke test

The Windows workflow verifies that `ExcelAutomationTool.exe` is created and is not unexpectedly tiny before uploading the artifact.

## Manual release validation

Before a public release, test with synthetic files covering:

- CSV input
- XLSX input
- XLSM input
- Empty rows and columns
- Duplicate rows
- Whitespace-heavy text
- Email fields
- Missing values
- Batch folder with both valid and invalid files
- Merge with and without source tracking
- HTML and JSON quality reports

Never put private or real customer files into the repository.
