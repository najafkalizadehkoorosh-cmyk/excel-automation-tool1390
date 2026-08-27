"""Ready-to-use workflow presets."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import pandas as pd

from .cleaner import clean_table
from .transform import transform_table


@dataclass(frozen=True)
class WorkflowPreset:
    key: str
    name: str
    description: str
    handler: Callable[[pd.DataFrame], pd.DataFrame]


def customer_contacts(df: pd.DataFrame) -> pd.DataFrame:
    """Prepare common customer/contact exports without inventing values."""
    result = clean_table(df, drop_duplicates=True)
    return transform_table(result, column_names=True, text=True, emails=True)


def generic_cleanup(df: pd.DataFrame) -> pd.DataFrame:
    """Apply the default safe cleanup workflow."""
    return transform_table(clean_table(df, drop_duplicates=True))


def sales_export(df: pd.DataFrame) -> pd.DataFrame:
    """Prepare a typical sales export while preserving business values."""
    result = clean_table(df, drop_duplicates=False)
    return transform_table(result, column_names=True, text=True, emails=True)


PRESETS: dict[str, WorkflowPreset] = {
    "general_cleanup": WorkflowPreset(
        "general_cleanup",
        "General Cleanup",
        "Remove empty structure, duplicates, and inconsistent text formatting.",
        generic_cleanup,
    ),
    "customer_contacts": WorkflowPreset(
        "customer_contacts",
        "Customer Contacts",
        "Clean and standardize customer/contact exports including likely email fields.",
        customer_contacts,
    ),
    "sales_export": WorkflowPreset(
        "sales_export",
        "Sales Export",
        "Clean and standardize sales exports while preserving duplicate transaction rows.",
        sales_export,
    ),
}


def get_preset(key: str) -> WorkflowPreset:
    try:
        return PRESETS[key]
    except KeyError as exc:
        raise ValueError(f"Unknown workflow preset: {key}") from exc
