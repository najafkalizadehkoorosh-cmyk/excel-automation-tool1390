from pathlib import Path

import pandas as pd

from src.excel_automation.batch import process_folder


def test_process_folder_creates_cleaned_outputs(tmp_path: Path):
    source = tmp_path / "input"
    source.mkdir()
    pd.DataFrame({"name": [" Alice ", "Alice"], "score": [10, 10]}).to_csv(
        source / "people.csv", index=False
    )

    results = process_folder(source)

    assert len(results) == 1
    assert results[0]["status"] == "ok"
    assert Path(results[0]["output_file"]).exists()
    assert results[0]["rows"] == 1
