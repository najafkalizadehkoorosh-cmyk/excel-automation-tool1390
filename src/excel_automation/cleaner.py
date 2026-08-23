"""Data cleaning operations."""

import pandas as pd


def clean_table(df: pd.DataFrame, *, drop_duplicates: bool = True) -> pd.DataFrame:
    """Return a cleaned copy of a DataFrame.

    - Normalizes completely empty rows/columns.
    - Trims whitespace from text cells.
    - Optionally removes duplicate rows.
    """
    result = df.copy()

    result = result.dropna(axis=0, how="all")
    result = result.dropna(axis=1, how="all")

    for column in result.select_dtypes(include=["object", "string"]).columns:
        result[column] = result[column].map(
            lambda value: value.strip() if isinstance(value, str) else value
        )

    if drop_duplicates:
        result = result.drop_duplicates(ignore_index=True)

    return result.reset_index(drop=True)
