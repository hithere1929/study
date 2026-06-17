import json
import logging
import re
from pathlib import Path

from pypdf import PdfReader


logging.getLogger("pypdf").setLevel(logging.ERROR)
ROOT = Path(__file__).parent
NOTES = ROOT / "Notes"
VISUAL_PAGE_TEXT = (
    "[This page is visual or image-based and contains no machine-extractable "
    "text. Open the matching notes page to study its diagrams and labels.]"
)


def section_info(pdf_path):
    match = re.search(r"Unit\s+(\d+)\.(\d+)\s*-\s*(.+)\.pdf$", pdf_path.name, re.I)
    if not match:
        raise ValueError(f"Cannot identify section from {pdf_path.name}")
    unit, section, title = match.groups()
    return int(unit), f"Unit_{unit}_{section}.txt", title


def clean_text(value):
    value = (value or "").replace("\x00", " ")
    value = re.sub(r"[ \t]+", " ", value)
    value = re.sub(r"\n{3,}", "\n\n", value)
    return value.strip()


def page_title(text, fallback):
    if text.startswith("[This page is visual or image-based"):
        return fallback

    line = next((line.strip() for line in text.splitlines() if line.strip()), fallback)
    line = line.lstrip(" -\u2013\u2014\u2022\u00b7\u00a8\u00a4\t")
    line = re.split(r"[\u00a8\u00a4\u2022]|(?<=\S)\u2013", line, maxsplit=1)[0]
    line = re.split(
        r"(?i)(?=Mr\.\s*Queenan|Biology\s*9|For more information|Text\s*-?Ch\.?|Unit\s+\d)",
        line,
        maxsplit=1,
    )[0].strip(" :-\u2013\u2014")

    line = {
        "Virioidsand Prions": "Viroids and Prions",
        "Viriodsand Prions": "Viroids and Prions",
        "Virioids and Prions": "Viroids and Prions",
    }.get(line, line)

    if len(line) > 100:
        line = line[:100].rsplit(" ", 1)[0].rstrip(" ,;:-\u2013\u2014") + "..."
    return line or fallback


def make_questions(title, text):
    excerpt = " ".join(text.split())
    if len(excerpt) > 420:
        excerpt = excerpt[:417].rsplit(" ", 1)[0] + "..."
    return [
        {
            "q": (
                "Without looking back, explain the important information "
                f'on the page titled "{title}."'
            ),
            "type": "recall",
            "answer": excerpt,
            "exp": (
                "A complete answer should include the page's major terms, "
                "relationships, processes, examples, and exceptions. Compare your "
                "response with the complete page notes shown above."
            ),
        }
    ]


by_unit = {}
for unit in range(1, 9):
    entries = json.loads(
        (ROOT / f"unit{unit}_active_recall.json").read_text(encoding="utf-8-sig")
    )
    by_unit[unit] = entries
    for legacy_index, entry in enumerate(entries):
        entry.setdefault("legacy_index", legacy_index)

for unit in range(1, 9):
    existing = {}
    for entry in by_unit[unit]:
        key = (entry["filename"], int(entry["page_num_in_file"]))
        if key not in existing:
            existing[key] = entry

    rebuilt = []
    unit_pdfs = []
    for pdf_path in NOTES.glob("*.pdf"):
        pdf_unit, filename, section_title = section_info(pdf_path)
        if pdf_unit == unit:
            section_number = tuple(int(part) for part in filename[5:-4].split("_"))
            unit_pdfs.append((section_number, pdf_path, filename, section_title))

    for _, pdf_path, filename, section_title in sorted(unit_pdfs):
        reader = PdfReader(str(pdf_path))
        for page_number, pdf_page in enumerate(reader.pages, start=1):
            extracted = clean_text(pdf_page.extract_text() or "") or VISUAL_PAGE_TEXT
            title = page_title(
                extracted, f"{section_title} - Visual Page {page_number}"
            )
            entry = existing.get((filename, page_number))
            if entry is None:
                entry = {
                    "unit": unit,
                    "filename": filename,
                    "section_title": section_title,
                    "page_num_in_file": page_number,
                    "slide_title": title,
                    "original_text": extracted,
                    "explanation": (
                        "Study this complete page carefully, then recall its terminology, "
                        "relationships, steps, examples, and exceptions without looking."
                    ),
                    "questions": make_questions(title, extracted),
                    "legacy_index": None,
                }
            else:
                entry["original_text"] = extracted
                entry["slide_title"] = title
                if len(clean_text(entry.get("explanation"))) < 80:
                    entry["explanation"] = (
                        "Study this complete page carefully. Focus on every named term, "
                        "relationship, process, example, qualification, and exception shown "
                        "in the notes, then answer the recall prompt below."
                    )
                if not entry.get("questions"):
                    entry["questions"] = make_questions(title, extracted)
                for question in entry.get("questions", []):
                    if question.get("type") == "recall":
                        question["q"] = (
                            "Without looking back, explain the important information "
                            f'on the page titled "{title}."'
                        )
            rebuilt.append(entry)

    for global_page, entry in enumerate(rebuilt, start=1):
        entry["page"] = global_page
    (ROOT / f"unit{unit}_active_recall.json").write_text(
        json.dumps(rebuilt, ensure_ascii=False, indent=2),
        encoding="utf-8",
        newline="\n",
    )
    print(f"Unit {unit}: {len(rebuilt)} pages")
