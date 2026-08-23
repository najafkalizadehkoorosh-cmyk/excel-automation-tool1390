"""Reporting and output utilities."""

from pathlib import Path

import pandas as pd


def summarize(df: pd.DataFrame) -> dict:
    """Build a compact, JSON-friendly summary of a table."""
    missing = int(df.isna().sum().sum())
    duplicate_rows = int(df.duplicated().sum())

    return {
        "rows": int(len(df)),
        "columns": int(len(df.columns)),
        "column_names": [str(column) for column in df.columns],
        "missing_cells": missing,
        "duplicate_rows": duplicate_rows,
    }


def save_table(df: pd.DataFrame, output_path: str | Path) -> Path:
    """Save a cleaned DataFrame as CSV or XLSX."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    suffix = path.suffix.lower()
    if suffix == ".csv":
        df.to_csv(path, index=False)
    elif suffix in {".xlsx", ".xlsm"}:
        df.to_excel(path, index=False)
    else:
        raise ValueError("Output must end with .csv, .xlsx, or .xlsm")

    return path
