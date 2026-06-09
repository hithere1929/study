import json
import re
from pathlib import Path

from pypdf import PdfReader

root = Path(__file__).parent
notes = root / "Notes"
index = {}
files = {}

for pdf in sorted(notes.glob("Unit *.pdf")):
    match = re.match(r"Unit (\d+\.\d+) - ", pdf.name)
    if not match:
        continue
    section = match.group(1)
    files[section] = "Notes/" + pdf.name
    pages = []
    for page in PdfReader(str(pdf)).pages:
        text = page.extract_text() or ""
        text = re.sub(r"\s+", " ", text).lower()
        pages.append(text)
    index[section] = pages

payload = (
    "const BIO_NOTES_FILES = "
    + json.dumps(files, ensure_ascii=True, separators=(",", ":"))
    + ";\nconst BIO_NOTES_PAGE_INDEX = "
    + json.dumps(index, ensure_ascii=True, separators=(",", ":"))
    + ";\n"
)

path = root / "index.html"
html = path.read_text(encoding="utf-8")
marker = "const MEMORY_LAB_KEY = 'bio_memory_lab_v1';"
html = re.sub(
    r"const BIO_NOTES_FILES = .*?\nconst BIO_NOTES_PAGE_INDEX = .*?\n(?=const MEMORY_LAB_KEY)",
    "",
    html,
    flags=re.S,
)
html = html.replace(marker, payload + marker)
path.write_text(html, encoding="utf-8", newline="")
print(f"Indexed {len(files)} note PDFs.")
