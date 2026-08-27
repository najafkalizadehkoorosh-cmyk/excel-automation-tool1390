# Quick Start

## Windows desktop app

1. Download the latest Windows artifact or release.
2. Extract the ZIP.
3. Run `ExcelAutomationTool.exe`.
4. Choose **Clean one file**, **Process a folder**, or **Merge a folder**.
5. Select your CSV/XLSX/XLSM input.
6. Choose an output location and run the workflow.
7. Review the generated output and quality report.

## Safe first test

Use a copy of your data for the first run. The tool favors deterministic transformations and does not invent missing values.

## CLI

```bash
python -m src.excel_automation.cli input.xlsx
python -m src.excel_automation.cli ./data --batch --output ./processed
python -m src.excel_automation.cli ./data --merge --output merged.xlsx
```

## Common workflows

### Clean customer data

Use **Clean one file** to remove empty rows/columns, normalize whitespace, remove duplicate rows, normalize column names, and normalize likely email fields.

### Process many files

Use **Process a folder** when the same deterministic cleaning should be applied to many supported files.

### Combine files

Use **Merge a folder** when multiple compatible files need to be combined. Keep source tracking enabled when you need to know which input produced each row.
