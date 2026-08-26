"""Safe, deterministic data transformations for cleaned tables."""

from __future__ import annotations

import re

import pandas as pd


def normalize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize column names to readable snake_case without changing values."""
    result = df.copy()
    names: list[str] = []
    seen: dict[str, int] = {}
    for column in result.columns:
        name = re.sub(r"[^a-zA-Z0-9]+", "_", str(column).strip().lower()).strip("_")
        name = name or "column"
        seen[name] = seen.get(name, 0) + 1
        if seen[name] > 1:
            name = f"{name}_{seen[name]}"
        names.append(name)
    result.columns = names
    return result


def normalize_text_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Trim text and collapse repeated internal whitespace."""
    result = df.copy()
    for column in result.select_dtypes(include=["object", "string"]).columns:
        result[column] = result[column].map(
            lambda value: re.sub(r"\s+", " ", value).strip() if isinstance(value, str) else value
        )
    return result


def normalize_email_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize likely email columns without inventing missing values."""
    result = df.copy()
    for column in result.columns:
        if "email" in str(column).lower() or "e-mail" in str(column).lower():
            result[column] = result[column].map(
                lambda value: value.strip().lower() if isinstance(value, str) else value
            )
    return result


def transform_table(
    df: pd.DataFrame,
    *,
    column_names: bool = True,
    text: bool = True,
    emails: bool = True,
) -> pd.DataFrame:
    """Apply only deterministic transformations selected by the caller."""
    result = df.copy()
    if column_names:
        result = normalize_column_names(result)
    if text:
        result = normalize_text_columns(result)
    if emails:
        result = normalize_email_columns(result)
    return result
