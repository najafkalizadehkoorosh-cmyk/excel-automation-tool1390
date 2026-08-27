import pandas as pd

from src.excel_automation.presets import customer_contacts


def test_customer_contacts_deduplicates_rows_that_match_after_normalization():
    df = pd.DataFrame(
        {
            " Customer Name ": ["  Alice  ", "Alice"],
            "Email Address": [" ALICE@EXAMPLE.COM ", "alice@example.com"],
        }
    )

    result = customer_contacts(df)

    assert len(result) == 1
    assert result.loc[0, "customer_name"] == "Alice"
    assert result.loc[0, "email_address"] == "alice@example.com"
