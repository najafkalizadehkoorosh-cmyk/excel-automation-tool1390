import pandas as pd

from src.excel_automation.reporter import summarize


def test_summarize_reports_shape_missing_and_duplicates():
    df = pd.DataFrame({"name": ["Alice", "Alice", None], "score": [10, 10, 20]})

    summary = summarize(df)

    assert summary["rows"] == 3
    assert summary["columns"] == 2
    assert summary["missing_cells"] == 1
    assert summary["duplicate_rows"] == 1
