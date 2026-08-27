import pandas as pd

from src.excel_automation.presets import get_preset


def test_customer_contacts_preset_normalizes_contact_data():
    df = pd.DataFrame(
        {
            " Customer Name ": ["  Alice  ", "Alice"],
            "Email Address": [" ALICE@EXAMPLE.COM ", "alice@example.com"],
        }
    )

    result = get_preset("customer_contacts").handler(df)

    assert list(result.columns) == ["customer_name", "email_address"]
    assert result.loc[0, "customer_name"] == "Alice"
    assert result.loc[0, "email_address"] == "alice@example.com"
    assert len(result) == 1


def test_sales_export_preserves_duplicate_transactions():
    df = pd.DataFrame({"Order ID": [1, 1], "Email": ["A@EXAMPLE.COM", "A@EXAMPLE.COM"]})

    result = get_preset("sales_export").handler(df)

    assert len(result) == 2
    assert list(result.columns) == ["order_id", "email"]
