import json
import logging
import re
from collections import Counter
from pathlib import Path

from pypdf import PdfReader


logging.getLogger("pypdf").setLevel(logging.ERROR)
ROOT = Path(__file__).resolve().parent.parent


def source_key(pdf_path):
    match = re.search(r"Unit\s+(\d+)\.(\d+)", pdf_path.name, re.I)
    assert match, f"Cannot identify section for {pdf_path.name}"
    return f"Unit_{match.group(1)}_{match.group(2)}.txt"


entries = []
for unit in range(1, 9):
    entries.extend(
        json.loads(
            (ROOT / f"unit{unit}_active_recall.json").read_text(encoding="utf-8-sig")
        )
    )

actual = Counter(
    (entry["filename"], int(entry["page_num_in_file"])) for entry in entries
)
expected = Counter()
for pdf_path in sorted((ROOT / "Notes").glob("*.pdf")):
    for page_number in range(1, len(PdfReader(str(pdf_path)).pages) + 1):
        expected[(source_key(pdf_path), page_number)] += 1

missing = sorted((expected - actual).elements())
duplicates = sorted(key for key, count in actual.items() if count > 1)
unexpected = sorted((actual - expected).elements())

assert len(entries) == sum(expected.values()) == 1025, (
    f"Expected 1,025 recall pages, found {len(entries)}"
)
assert not missing, f"Missing recall pages: {missing}"
assert not duplicates, f"Duplicate recall pages: {duplicates}"
assert not unexpected, f"Unexpected recall pages: {unexpected}"
assert all(entry.get("questions") for entry in entries), "Every page needs recall questions"
assert all(
    str(entry.get("original_text", "")).strip() for entry in entries
), "Every page needs its extracted source text"

print("Active recall covers all 1,025 PDF pages exactly once.")
