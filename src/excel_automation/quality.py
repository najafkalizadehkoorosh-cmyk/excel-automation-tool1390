"""Data-quality diagnostics for Excel/CSV tables."""

from __future__ import annotations

import re

import pandas as pd

_EMAIL_RE = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")


def profile_table(df: pd.DataFrame) -> dict:
    """Return useful, JSON-friendly data-quality diagnostics."""
    issues: list[dict] = []

    for column in df.columns:
        name = str(column)
        series = df[column]
        missing = int(series.isna().sum())
        empty_text = int(series.map(lambda v: isinstance(v, str) and not v.strip()).sum())
        repeated_values = int(series.duplicated(keep=False).sum()) if len(series) else 0

        if missing:
            issues.append({"column": name, "type": "missing", "count": missing})
        if empty_text:
            issues.append({"column": name, "type": "empty_text", "count": empty_text})
        if repeated_values and series.nunique(dropna=True) < len(series):
            issues.append({"column": name, "type": "repeated_values", "count": repeated_values})

        if len(series.dropna()) and "email" in name.lower():
            invalid = int(
                series.dropna().map(lambda v: not bool(_EMAIL_RE.match(str(v).strip()))).sum()
            )
            if invalid:
                issues.append({"column": name, "type": "invalid_email", "count": invalid})

    return {
        "rows": int(len(df)),
        "columns": int(len(df.columns)),
        "missing_cells": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "issues": issues,
        "issue_count": len(issues),
    }
