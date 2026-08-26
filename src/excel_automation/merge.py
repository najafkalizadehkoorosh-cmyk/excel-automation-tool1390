"""Utilities for combining multiple CSV/Excel tables safely."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from .reader import SUPPORTED_EXTENSIONS, load_table


def merge_files(input_dir: str | Path, output_path: str | Path, *, include_source: bool = True) -> Path:
    """Combine all supported files in a folder into one XLSX/CSV output."""
    source_dir = Path(input_dir)
    if not source_dir.is_dir():
        raise NotADirectoryError(f"Input directory not found: {source_dir}")

    files = sorted(
        p for p in source_dir.iterdir()
        if p.is_file() and p.suffix.lower() in SUPPORTED_EXTENSIONS
    )
    if not files:
        raise ValueError("No supported CSV/XLSX/XLSM files found in the folder")

    frames: list[pd.DataFrame] = []
    for path in files:
        frame = load_table(path).copy()
        if include_source:
            frame["source_file"] = path.name
        frames.append(frame)

    merged = pd.concat(frames, ignore_index=True, sort=False)
    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    suffix = destination.suffix.lower()
    if suffix == ".csv":
        merged.to_csv(destination, index=False)
    elif suffix in {".xlsx", ".xlsm"}:
        merged.to_excel(destination, index=False)
    else:
        raise ValueError("Output must end with .csv, .xlsx, or .xlsm")
    return destination
