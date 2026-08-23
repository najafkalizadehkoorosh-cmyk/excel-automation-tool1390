import pandas as pd

from src.excel_automation.cleaner import clean_table


def test_clean_table_removes_empty_rows_and_duplicates_and_trims_text():
    df = pd.DataFrame(
        {
            "name": [" Alice ", "Bob", "Bob", None],
            "value": [1, 2, 2, None],
        }
    )

    cleaned = clean_table(df)

    assert len(cleaned) == 2
    assert cleaned.iloc[0]["name"] == "Alice"
    assert cleaned.iloc[1]["name"] == "Bob"
