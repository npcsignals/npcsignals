"""Rebuild and verify English SVG copies while preserving original plotted geometry and numeric labels."""
import argparse
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "phase23" / "figures"
TARGET = ROOT / "phase25" / "figures"
MANIFEST = ROOT / "phase25" / "figure_translations.json"
from phase25.build_layouts import outputs, text
TAG = re.compile(r"<(title|desc|text)([^>]*)>([^<]*)</\1>")
NUMBER = re.compile(r"(?<![A-Za-z])\d+(?:[.,]\d+)?")

def convert(source, pairs):
    replacements = dict(pairs)
    seen = set()
    def change(match):
        original = match.group(3)
        translated = replacements.get(original, original)
        if original in replacements:
            seen.add(original)
            if NUMBER.findall(original) != NUMBER.findall(translated):
                raise ValueError(f"numeric token changed: {original!r}")
        return f"<{match.group(1)}{match.group(2)}>{translated}</{match.group(1)}>"
    output = TAG.sub(change, source)
    missing = set(replacements) - seen
    if missing:
        raise ValueError(f"unused translation entries: {missing}")
    return output

# Display source locators directly on the artwork for use outside the article.
SOURCE_LINES = {
    "01_geography": ("sources: TE-SAT 2016–2020 attack annexes.",),
    "02_eu27_series": ("sources: TE-SAT 2016–2026 annual tables; 2024 report p. 51 n. 75 for the French entries.",),
    "03_revisions": ("sources: TE-SAT 2023 p. 9 n. 4; TE-SAT 2024 p. 51 n. 75.",),
    "04_coverage": ("source: NPCsignals annual crosswalks and fixed geography analysis.",),
    "05_institutions": ("sources: NRW 2025 pp. 28, 216; Bundestag 21/4296 p. 18;",
                        "PNAT 2025 activity bundle p. 27; TE-SAT 2026 pp. 19, 47."),
    "06_judicial": ("Holbæk: Østre Landsret, S-25-23, 14 May 2024 (court notice); PET, same date (agency report).",
                    "A100: LG Berlin 5/2022; BGH 036/2023; TE-SAT 2023 p. 9 n. 4. Solingen: TE-SAT 2025; BGH above."),
}
TOP_LINES = {
    "02_eu27_series": (60, "2023 reporting cohort includes 26 entries from earlier French occurrence years."),
    "04_coverage": (89, "original reporting cohorts: EU28 through 2019; EU27 from 2020."),
}


def annotate(name, svg):
    lines = SOURCE_LINES[name]
    # Extend the lower margin without moving any plotted data or axes.
    height = int(re.search(r'height="(\d+)"', svg).group(1))
    extended = height + 14 + 20 * len(lines)
    svg = svg.replace(f'height="{height}" viewBox="0 0 880 {height}"',
                      f'height="{extended}" viewBox="0 0 880 {extended}"', 1)
    svg = svg.replace(f'height="{height:.2f}" fill="#ffffff"',
                      f'height="{extended:.2f}" fill="#ffffff"', 1)
    notes = [text(30, height + 12 + 20*i, line, 13) for i, line in enumerate(lines)]
    svg = svg.replace("</g>\n</svg>", '<g fill="#162436">\n' + "\n".join(notes) + "\n</g>\n</g>\n</svg>")
    if name in TOP_LINES:
        y, note = TOP_LINES[name]
        annotation = '<g fill="#162436">' + text(30, y, note, 15, True) + "</g>\n"
        title_end = svg.index("</text>") + len("</text>\n")
        svg = svg[:title_end] + annotation + svg[title_end:]
    return svg.replace("NPCsignals internal review. ", "NPCsignals. ")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="verify committed SVG bytes")
    args = parser.parse_args()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for name, pairs in manifest.items():
        original = (SOURCE / f"{name}.svg").read_text(encoding="utf-8")
        expected = annotate(name, convert(original, pairs))
        destination = TARGET / f"{name}_en.svg"
        if args.check:
            actual = destination.read_text(encoding="utf-8")
            if actual != expected:
                raise SystemExit(f"FAIL: {destination}")
        else:
            destination.write_text(expected, encoding="utf-8")
        print(f"PASS: {name}")
    for name, expected in outputs():
        destination = TARGET / name
        if args.check:
            if destination.read_text(encoding="utf-8") != expected:
                raise SystemExit(f"FAIL: {destination}")
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(expected, encoding="utf-8")
    print("PASS: deterministic lead and seven mobile layouts")
    lead = (TARGET / "01_2019_2020_geography.svg").read_text(encoding="utf-8")
    with (ROOT.parent / "data" / "phase22_annual_analysis.csv").open(
        encoding="utf-8", newline=""
    ) as stream:
        annual = {row["reference_year"]: row for row in csv.DictReader(stream)}
    year_2019, year_2020 = annual["2019"], annual["2020"]
    assert int(year_2019["original_attacks"]) - int(year_2019["included_uk_attacks"]) == int(year_2019["fixed_eu27_attacks"])
    assert int(year_2019["original_attacks"]) == 119
    assert int(year_2019["fixed_eu27_attacks"]) == 55
    assert int(year_2020["fixed_eu27_attacks"]) == 57
    assert int(year_2020["later_official_attack_revision"]) == 56
    for value in ("119", "55", "57", "56"):
        if not re.search(rf">{value}</text>", lead):
            raise SystemExit(f"FAIL: geographic figure missing value {value}")
    print("PASS: lead figure values match versioned annual dataset")
    if args.check:
        print("PASS: all six English SVGs reproduce byte-for-byte from originals, translation manifest and source annotations")

if __name__ == "__main__":
    main()
