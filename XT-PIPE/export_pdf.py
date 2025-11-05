#!/usr/bin/env python3
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER

base_dir = Path(__file__).resolve().parents[1]
out_base = base_dir / "XT-MAG-out"
latest = max(out_base.iterdir(), key=lambda p: p.stat().st_mtime)

md_file = latest / "inkloso_issue.md"
pdf_file = latest / "inkloso_issue.pdf"

styles = getSampleStyleSheet()
doc = SimpleDocTemplate(str(pdf_file), pagesize=LETTER)
story = []

for line in md_file.read_text().splitlines():
    if line.strip():
        story.append(Paragraph(line, styles["Normal"]))
        story.append(Spacer(1, 8))

doc.build(story)
print(f"✅ PDF exported at: {pdf_file}")
