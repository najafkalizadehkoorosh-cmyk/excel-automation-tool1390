import pandas as pd

from src.excel_automation.quality import profile_table


def test_profile_table_detects_missing_duplicates_and_invalid_email():
    df = pd.DataFrame(
        {
            "name": ["Alice", "Alice", None],
            "email": ["alice@example.com", "not-an-email", None],
        }
    )

    profile = profile_table(df)

    assert profile["rows"] == 3
    assert profile["columns"] == 2
    assert profile["missing_cells"] == 2
    assert profile["duplicate_rows"] == 0
    assert profile["issue_count"] >= 3
    assert any(issue["type"] == "invalid_email" for issue in profile["issues"])
    assert any(issue["type"] == "missing" for issue in profile["issues"])
