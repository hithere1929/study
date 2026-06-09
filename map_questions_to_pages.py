"""
Builds BIO_QUESTION_PAGE_MAP: for every biology question, asks Claude which
PDF page best covers it, then writes the mapping into index.html.

Requirements:
    pip install anthropic

Usage:
    set ANTHROPIC_API_KEY=sk-ant-...
    python map_questions_to_pages.py
"""

import json
import os
import re
import time
from pathlib import Path

import anthropic

ROOT = Path(__file__).parent
HTML_FILE = ROOT / "index.html"

# ── load page index from HTML ────────────────────────────────────────────────
html = HTML_FILE.read_text(encoding="utf-8")
m = re.search(r"const BIO_NOTES_PAGE_INDEX = ({.*?});\n", html, re.S)
if not m:
    raise SystemExit("BIO_NOTES_PAGE_INDEX not found in index.html — run build_notes_index.py first")
PAGE_INDEX: dict[str, list[str]] = json.loads(m.group(1))

# ── load all questions grouped by section ────────────────────────────────────
questions_by_section: dict[str, list[dict]] = {}
for jf in sorted(ROOT.glob("unit*_questions.json")):
    for q in json.load(jf.open(encoding="utf-8")):
        sec = q.get("section", "")
        if sec:
            questions_by_section.setdefault(sec, []).append(q)

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

MAPPING: dict[str, int] = {}

def pages_text(pages: list[str]) -> str:
    parts = []
    for i, txt in enumerate(pages, 1):
        snippet = txt[:600].replace("\n", " ")
        parts.append(f"Page {i}: {snippet}")
    return "\n".join(parts)

def ask_claude(section: str, qs: list[dict], pages: list[str]) -> dict[str, int]:
    """Return {question_text: page_number} for all qs in one API call."""
    q_block = []
    for i, q in enumerate(qs, 1):
        correct_text = ""
        if q.get("t") == "mc" and q.get("opts") and q.get("a") is not None:
            correct_text = q["opts"][q["a"]]
        elif q.get("correct"):
            correct_text = (
                ", ".join(q["correct"]) if isinstance(q["correct"], list)
                else q["correct"]
            )
        opts_text = "\n".join(
            f"  {chr(64+j+1)}. {o}" for j, o in enumerate(q.get("opts", []))
        )
        expl = (q.get("explanation") or "")[:300]
        q_block.append(
            f"Q{i}: {q['q']}\n"
            + (f"Options:\n{opts_text}\n" if opts_text else "")
            + (f"Correct answer: {correct_text}\n" if correct_text else "")
            + (f"Explanation hint: {expl}\n" if expl else "")
        )

    prompt = (
        f"Biology section {section}. Below are the text contents of each PDF slide page, "
        f"followed by exam questions. For each question, respond with ONLY the page number "
        f"(integer) of the slide that best covers the specific content tested. "
        f"Use the correct answer and explanation as your primary clue — the answer is "
        f"literally on that page.\n\n"
        f"PDF PAGES:\n{pages_text(pages)}\n\n"
        f"QUESTIONS:\n" + "\n\n".join(q_block) + "\n\n"
        f"Respond in this exact format, one per line:\n"
        + "\n".join(f"Q{i}: <page number>" for i in range(1, len(qs) + 1))
    )

    resp = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}],
    )
    text = resp.content[0].text.strip()
    result = {}
    for i, q in enumerate(qs, 1):
        m2 = re.search(rf"Q{i}:\s*(\d+)", text)
        if m2:
            result[q["q"]] = int(m2.group(1))
    return result

BATCH = 12  # questions per API call

total_sections = sorted(set(questions_by_section) & set(PAGE_INDEX))
print(f"Mapping {sum(len(v) for k,v in questions_by_section.items() if k in PAGE_INDEX)} questions across {len(total_sections)} sections...")

for sec in total_sections:
    qs = questions_by_section[sec]
    pages = PAGE_INDEX[sec]
    print(f"  Section {sec}: {len(qs)} questions, {len(pages)} pages", end="", flush=True)
    for start in range(0, len(qs), BATCH):
        batch = qs[start:start + BATCH]
        result = ask_claude(sec, batch, pages)
        for q_text, page_num in result.items():
            MAPPING[f"{sec}:{q_text}"] = page_num
        print(".", end="", flush=True)
        if start + BATCH < len(qs):
            time.sleep(0.5)
    print()

# ── embed mapping into HTML ──────────────────────────────────────────────────
map_js = (
    "const BIO_QUESTION_PAGE_MAP = "
    + json.dumps(MAPPING, ensure_ascii=True, separators=(",", ":"))
    + ";\n"
)

MARKER = "const BIO_NOTES_FILES ="
html = re.sub(r"const BIO_QUESTION_PAGE_MAP = \{.*?\};\n", "", html, flags=re.S)
html = html.replace(MARKER, map_js + MARKER)
HTML_FILE.write_text(html, encoding="utf-8", newline="")

print(f"\nDone — {len(MAPPING)} question→page mappings written to index.html.")
print("Run: git add index.html && git commit -m 'Add question-page map' && git push")
