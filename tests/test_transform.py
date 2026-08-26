import pandas as pd

from src.excel_automation.transform import transform_table


def test_transform_normalizes_columns_text_and_emails():
    df = pd.DataFrame(
        {
            " Customer Name ": ["  Alice   Smith  "],
            "Email Address": ["  ALICE@EXAMPLE.COM  "],
        }
    )

    result = transform_table(df)

    assert list(result.columns) == ["customer_name", "email_address"]
    assert result.loc[0, "customer_name"] == "Alice Smith"
    assert result.loc[0, "email_address"] == "alice@example.com"
