from pathlib import Path

import pandas as pd

from src.excel_automation.merge import merge_files


def test_merge_files(tmp_path: Path) -> None:
    source = tmp_path / "input"
    source.mkdir()
    pd.DataFrame({"Name": ["A", "B"]}).to_csv(source / "a.csv", index=False)
    pd.DataFrame({"Name": ["C"]}).to_csv(source / "b.csv", index=False)

    output = tmp_path / "merged.xlsx"
    result = merge_files(source, output)
    merged = pd.read_excel(result)

    assert len(merged) == 3
    assert set(merged["source_file"]) == {"a.csv", "b.csv"}
