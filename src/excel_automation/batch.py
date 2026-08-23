"""Batch processing for folders of Excel and CSV files."""

from pathlib import Path

from .cleaner import clean_table
from .reader import SUPPORTED_EXTENSIONS, load_table
from .reporter import save_table, summarize


def process_folder(
    input_dir: str | Path,
    output_dir: str | Path | None = None,
    *,
    keep_duplicates: bool = False,
) -> list[dict]:
    """Process every supported data file in a folder.

    Each result contains the source file, output file, and summary. A failed
    file is recorded with an error instead of stopping the whole batch.
    """
    source_dir = Path(input_dir)
    if not source_dir.is_dir():
        raise NotADirectoryError(f"Input directory not found: {source_dir}")

    destination = Path(output_dir) if output_dir else source_dir / "cleaned_output"
    destination.mkdir(parents=True, exist_ok=True)

    files = sorted(
        path for path in source_dir.iterdir()
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
    )

    results: list[dict] = []
    for source in files:
        try:
            frame = clean_table(
                load_table(source),
                drop_duplicates=not keep_duplicates,
            )
            output = destination / f"cleaned_{source.stem}.xlsx"
            save_table(frame, output)
            summary = summarize(frame)
            summary.update({"input_file": str(source), "output_file": str(output), "status": "ok"})
        except (OSError, ValueError, RuntimeError) as exc:
            summary = {
                "input_file": str(source),
                "output_file": None,
                "status": "error",
                "error": str(exc),
            }
        results.append(summary)

    return results
