"""Command-line interface for the Excel Automation Tool."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .batch import process_folder
from .cleaner import clean_table
from .merge import merge_files
from .presets import PRESETS, get_preset
from .quality import profile_table
from .quality_report import save_quality_report
from .reader import load_table
from .reporter import save_table, summarize
from .transform import transform_table


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Clean, transform, merge, and profile Excel/CSV files."
    )
    parser.add_argument("input", help="Path to a file or folder")
    parser.add_argument("-o", "--output", help="Output file or folder")
    parser.add_argument("--keep-duplicates", action="store_true")
    parser.add_argument("--batch", action="store_true", help="Process every supported file in a folder")
    parser.add_argument("--merge", action="store_true", help="Merge every supported file in a folder")
    parser.add_argument("--no-transform", action="store_true")
    parser.add_argument("--no-source-column", action="store_true", help="Do not add source_file when merging")
    parser.add_argument(
        "--preset",
        choices=sorted(PRESETS),
        default=None,
        help="Apply a ready-to-use workflow preset to a single file.",
    )
    parser.add_argument(
        "--quality-report",
        help="Write the before-cleaning quality profile to .json or .html.",
    )
    return parser


def run(
    input_path: str,
    output_path: str | None = None,
    keep_duplicates: bool = False,
    apply_transform: bool = True,
    preset: str | None = None,
    quality_report: str | None = None,
) -> dict:
    source = Path(input_path)
    df = load_table(source)
    quality_before = profile_table(df)

    if preset:
        transformed = get_preset(preset).handler(df)
        transformations_applied = True
    else:
        cleaned = clean_table(df, drop_duplicates=not keep_duplicates)
        transformed = transform_table(cleaned) if apply_transform else cleaned
        transformations_applied = apply_transform

    output = output_path or str(source.with_name(f"cleaned_{source.stem}.xlsx"))
    saved = save_table(transformed, output)
    summary = summarize(transformed)
    summary.update(
        {
            "output_file": str(saved),
            "quality_before": quality_before,
            "quality_after": profile_table(transformed),
            "transformations_applied": transformations_applied,
            "preset": preset,
        }
    )
    if quality_report:
        summary["quality_report"] = str(save_quality_report(quality_before, quality_report))
    return summary


def main() -> int:
    args = build_parser().parse_args()
    try:
        if args.merge:
            output = args.output or str(Path(args.input) / "merged.xlsx")
            saved = merge_files(args.input, output, include_source=not args.no_source_column)
            print(json.dumps({"status": "ok", "output_file": str(saved)}, indent=2))
        elif args.batch:
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
                not args.no_transform,
                args.preset,
                args.quality_report,
            )
            print(json.dumps(summary, indent=2, ensure_ascii=False))
    except (FileNotFoundError, NotADirectoryError, ValueError, OSError) as exc:
        print(f"Error: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
