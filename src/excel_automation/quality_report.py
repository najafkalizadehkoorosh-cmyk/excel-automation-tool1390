"""Exportable data-quality reports."""

from __future__ import annotations

import json
from html import escape
from pathlib import Path


def save_quality_report(profile: dict, output_path: str | Path) -> Path:
    """Save a quality profile as JSON or a readable HTML report."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    suffix = path.suffix.lower()

    if suffix == ".json":
        path.write_text(json.dumps(profile, indent=2, ensure_ascii=False), encoding="utf-8")
        return path

    if suffix == ".html":
        rows = "".join(
            f"<tr><td>{escape(str(issue.get('column', '')))}</td>"
            f"<td>{escape(str(issue.get('type', '')))}</td>"
            f"<td>{int(issue.get('count', 0))}</td></tr>"
            for issue in profile.get("issues", [])
        )
        if not rows:
            rows = '<tr><td colspan="3">No issues detected.</td></tr>'
        html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Data Quality Report</title>
<style>body{{font-family:system-ui;margin:32px;max-width:980px;line-height:1.5}}table{{border-collapse:collapse;width:100%}}th,td{{border:1px solid #ddd;padding:8px;text-align:left}}.cards{{display:flex;gap:12px;flex-wrap:wrap}}.card{{padding:14px;border:1px solid #ddd;border-radius:10px}}h1{{margin-bottom:8px}}</style>
</head><body><h1>Data Quality Report</h1>
<div class="cards"><div class="card"><strong>Rows</strong><br>{profile.get('rows', 0)}</div><div class="card"><strong>Columns</strong><br>{profile.get('columns', 0)}</div><div class="card"><strong>Missing cells</strong><br>{profile.get('missing_cells', 0)}</div><div class="card"><strong>Duplicate rows</strong><br>{profile.get('duplicate_rows', 0)}</div><div class="card"><strong>Issue groups</strong><br>{profile.get('issue_count', 0)}</div></div>
<h2>Detected issues</h2><table><thead><tr><th>Column</th><th>Type</th><th>Count</th></tr></thead><tbody>{rows}</tbody></table>
</body></html>"""
        path.write_text(html, encoding="utf-8")
        return path

    raise ValueError("Quality report output must end with .json or .html")
