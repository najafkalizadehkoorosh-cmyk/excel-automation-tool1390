"""Command-line interface for the Excel Automation Tool."""

import argparse
import json
from pathlib import Path

from .batch import process_folder
from .cleaner import clean_table
from .reader import load_table
from .reporter import save_table, summarize
from .quality import profile_table
from .transform import transform_table


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Clean, transform, and generate data-quality reports for Excel/CSV files."
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
    parser.add_argument(
        "--no-transform", action="store_true",
        help="Skip deterministic column, text, and email normalization.",
    )
    return parser


def run(
    input_path: str,
    output_path: str | None = None,
    keep_duplicates: bool = False,
    apply_transform: bool = True,
) -> dict:
    """Run the complete single-file cleaning, transformation, and quality workflow."""
    source = Path(input_path)
    df = load_table(source)
    quality_before = profile_table(df)
    cleaned = clean_table(df, drop_duplicates=not keep_duplicates)
    transformed = transform_table(cleaned) if apply_transform else cleaned

    if output_path is None:
        output_path = str(source.with_name(f"cleaned_{source.stem}.xlsx"))

    saved = save_table(transformed, output_path)
    summary = summarize(transformed)
    summary["output_file"] = str(saved)
    summary["quality_before"] = quality_before
    summary["quality_after"] = profile_table(transformed)
    summary["transformations_applied"] = apply_transform
    return summary


def main() -> int:
    args = build_parser().parse_args()

    try:
        if args.batch:
            results = process_folder(
                args.input,
                args.output,
                keep_duplicates=args.keep_duplicates,
                apply_transform=not args.no_transform,
            )
            print(json.dumps(results, indent=2, ensure_ascii=False))
        else:
            summary = run(
                args.input,
                args.output,
                args.keep_duplicates,
                apply_transform=not args.no_transform,
            )
            print(json.dumps(summary, indent=2, ensure_ascii=False))
    except (FileNotFoundError, NotADirectoryError, ValueError, OSError) as exc:
        print(f"Error: {exc}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
