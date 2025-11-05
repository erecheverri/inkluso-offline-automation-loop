#!/usr/bin/env python3
import markdown, datetime
from pathlib import Path

base_dir = Path(__file__).resolve().parents[1]
out_base = base_dir / "XT-MAG-out"

# Find latest issue folder
latest = max(out_base.iterdir(), key=lambda p: p.stat().st_mtime)
md_path = latest / "inkloso_issue.md"
html_path = latest / "inkloso_issue.html"

md_content = md_path.read_text()
html_content = markdown.markdown(md_content, extensions=["tables", "fenced_code"])

html_template = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Inkluso Issue – {datetime.datetime.now().strftime('%Y-%m-%d')}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/water.css">
</head>
<body>
{html_content}
</body>
</html>
"""

html_path.write_text(html_template)
print(f"✅ HTML built at: {html_path}")
