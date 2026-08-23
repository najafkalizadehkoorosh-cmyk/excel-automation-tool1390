from pathlib import Path

import pandas as pd

from src.excel_automation.reader import load_table


def test_load_csv(tmp_path: Path):
    source = tmp_path / "sample.csv"
    pd.DataFrame({"name": ["Alice"], "score": [10]}).to_csv(source, index=False)

    result = load_table(source)

    assert list(result.columns) == ["name", "score"]
    assert result.iloc[0]["name"] == "Alice"


def test_unsupported_extension(tmp_path: Path):
    source = tmp_path / "sample.txt"
    source.write_text("hello", encoding="utf-8")

    try:
        load_table(source)
    except ValueError as exc:
        assert "Unsupported file type" in str(exc)
    else:
        raise AssertionError("Expected ValueError")
