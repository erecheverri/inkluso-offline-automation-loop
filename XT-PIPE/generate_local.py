#!/usr/bin/env python3
import os, datetime
from pathlib import Path

# 1. Prepare output directory
now = datetime.datetime.now().strftime("%Y%m%d-%H%M")
base_dir = Path(__file__).resolve().parents[1]
out_dir = base_dir / "XT-MAG-out" / now
out_dir.mkdir(parents=True, exist_ok=True)

# 2. Read source content (placeholder or imported from another chat)
# You can drop your SIG1/LOTI content in XT-MAG-out/content_input.md
input_file = base_dir / "XT-MAG-out" / "content_input.md"
if input_file.exists():
    content = input_file.read_text()
else:
    content = "# Inkluso Issue\nGenerated offline by SIG1/LOTI."

# 3. Save a timestamped copy
output_path = out_dir / "inkloso_issue.md"
output_path.write_text(content)

print(f"✅ Markdown saved at: {output_path}")
