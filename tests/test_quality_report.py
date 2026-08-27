from pathlib import Path

from src.excel_automation.quality_report import save_quality_report


def test_quality_report_writes_json(tmp_path: Path):
    output = tmp_path / "report.json"
    result = save_quality_report(
        {"rows": 2, "columns": 1, "missing_cells": 1, "duplicate_rows": 0, "issue_count": 1, "issues": []},
        output,
    )

    assert result == output
    assert '"rows": 2' in output.read_text(encoding="utf-8")


def test_quality_report_writes_html(tmp_path: Path):
    output = tmp_path / "report.html"
    save_quality_report(
        {"rows": 2, "columns": 1, "missing_cells": 1, "duplicate_rows": 0, "issue_count": 1,
         "issues": [{"column": "email", "type": "invalid_email", "count": 1}]},
        output,
    )

    html = output.read_text(encoding="utf-8")
    assert "Data Quality Report" in html
    assert "invalid_email" in html
