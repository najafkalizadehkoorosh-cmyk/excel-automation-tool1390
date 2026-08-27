from pathlib import Path

import pandas as pd

from src.excel_automation.batch import process_folder


def test_batch_reports_quality_before_and_after(tmp_path: Path):
    source = tmp_path / "input"
    source.mkdir()
    pd.DataFrame({" Name ": [" Alice ", "Alice"], "Email": [" ALICE@EXAMPLE.COM ", "ALICE@EXAMPLE.COM"]}).to_csv(source / "customers.csv", index=False)

    results = process_folder(source)

    assert len(results) == 1
    assert results[0]["status"] == "ok"
    assert results[0]["quality_before"]["rows"] == 2
    assert results[0]["quality_after"]["rows"] == 1
    assert Path(results[0]["output_file"]).exists()
