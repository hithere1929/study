import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
entries = []
for unit in range(1, 9):
    entries.extend(
        json.loads(
            (ROOT / f"unit{unit}_active_recall.json").read_text(encoding="utf-8")
        )
    )

bad_markers = ("¨", "¤", "•")
bad_titles = [
    (entry["filename"], entry["page_num_in_file"], entry.get("slide_title", ""))
    for entry in entries
    if len(entry.get("slide_title", "")) > 120
    or any(marker in entry.get("slide_title", "") for marker in bad_markers)
]
assert not bad_titles, f"Titles still contain slide body text: {bad_titles[:10]}"

viroids = next(
    entry
    for entry in entries
    if entry["filename"] == "Unit_6_1.txt" and entry["page_num_in_file"] == 11
)
assert viroids["slide_title"] == "Viroids and Prions", viroids["slide_title"]

print("Active recall titles are concise and separated from slide body text.")
