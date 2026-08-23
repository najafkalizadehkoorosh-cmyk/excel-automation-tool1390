"""Input file loading utilities."""

from pathlib import Path

import pandas as pd


SUPPORTED_EXTENSIONS = {".csv", ".xlsx", ".xlsm"}


def load_table(path: str | Path) -> pd.DataFrame:
    """Load a CSV or Excel workbook into a DataFrame."""
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    suffix = file_path.suffix.lower()
    if suffix not in SUPPORTED_EXTENSIONS:
        supported = ", ".join(sorted(SUPPORTED_EXTENSIONS))
        raise ValueError(f"Unsupported file type '{suffix}'. Supported: {supported}")

    if suffix == ".csv":
        return pd.read_csv(file_path)

    return pd.read_excel(file_path)
