"""Command-line interface for the Excel Automation Tool."""

import argparse
import json
from pathlib import Path

from .batch import process_folder
from .cleaner import clean_table
from .reader import load_table
from .reporter import save_table, summarize


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Clean Excel/CSV files and generate data summaries."
    )
    parser.add_argument("input", help="Path to a .csv, .xlsx, .xlsm file, or folder")
    parser.add_argument(
        "-o", "--output",
        help="Output file for single-file mode or output folder for batch mode",
    )
    parser.add_argument(
        "--keep-duplicates", action="store_true",
        help="Keep duplicate rows instead of removing them.",
    )
    parser.add_argument(
        "--batch", action="store_true",
        help="Process every supported file in the input folder.",
    )
    return parser


def run(input_path: str, output_path: str | None = None, keep_duplicates: bool = False) -> dict:
    """Run the complete single-file cleaning workflow."""
    source = Path(input_path)
    df = load_table(source)
    cleaned = clean_table(df, drop_duplicates=not keep_duplicates)

    if output_path is None:
        output_path = str(source.with_name(f"cleaned_{source.stem}.xlsx"))

    saved = save_table(cleaned, output_path)
    summary = summarize(cleaned)
    summary["output_file"] = str(saved)
    return summary


def main() -> int:
    args = build_parser().parse_args()

    try:
        if args.batch:
            results = process_folder(
                args.input,
                args.output,
                keep_duplicates=args.keep_duplicates,
            )
            print(json.dumps(results, indent=2, ensure_ascii=False))
        else:
            summary = run(args.input, args.output, args.keep_duplicates)
            print(json.dumps(summary, indent=2, ensure_ascii=False))
    except (FileNotFoundError, NotADirectoryError, ValueError, OSError) as exc:
        print(f"Error: {exc}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
