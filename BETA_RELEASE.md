# Excel Automation Tool — Beta Release Guide

## What this is

A local-first Windows utility for recurring Excel/CSV cleanup, standardization, batch processing, merging, and quality inspection.

## Who should try it

Best suited for people who repeatedly receive spreadsheet exports from CRMs, marketplaces, vendors, sales systems, or internal teams.

## 10-minute trial

1. Download the Windows build from GitHub Actions or a published release.
2. Extract the archive.
3. Run `ExcelAutomationTool.exe`.
4. Start with a copy of a spreadsheet, not the only original.
5. Try **General Cleanup** on a small file.
6. Review the generated output and quality report.
7. Try **Customer Contacts** on synthetic or non-sensitive contact data.
8. Try folder batch processing on several small files.
9. Try Merge on compatible files and check the `source_file` field.
10. Report any unexpected result using the feedback template below.

## Safety

- Keep an original backup of important files.
- Do not test with data you are not authorized to process.
- Do not paste confidential spreadsheet contents into public issues.
- Review important outputs before business use.

## What to report

Please include:

- Windows version;
- tool version;
- workflow used;
- input format (CSV/XLSX/XLSM);
- approximate row/column count;
- expected result;
- actual result;
- exact error message, if any.

Do not include passwords, API keys, payment data, or confidential customer records.
