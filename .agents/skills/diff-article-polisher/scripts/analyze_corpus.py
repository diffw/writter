#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import statistics
from collections import Counter
from pathlib import Path


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


def load_markdown_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if p.is_file())


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1)


def extract_year(frontmatter: str) -> str:
    match = re.search(r"^date:\s*(\d{4})-", frontmatter, re.M)
    return match.group(1) if match else "unknown"


def extract_tags(frontmatter: str) -> list[str]:
    block_match = re.search(r"^tags:\s*\n((?:\s*-\s.*\n?)*)", frontmatter, re.M)
    if block_match and block_match.group(1).strip():
        return [
            line.split("-", 1)[1].strip()
            for line in block_match.group(1).splitlines()
            if "-" in line
        ]

    inline_match = re.search(r"^tags:\s*\[(.*?)\]\s*$", frontmatter, re.M)
    if inline_match:
        return [tag.strip() for tag in inline_match.group(1).split(",") if tag.strip()]

    return []


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze a Markdown article corpus.")
    parser.add_argument("--root", required=True, help="Corpus root directory")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    files = load_markdown_files(root)
    if not files:
        raise SystemExit(f"No Markdown files found under {root}")

    year_counts: Counter[str] = Counter()
    tag_counts: Counter[str] = Counter()
    key_counts: Counter[str] = Counter()
    patterns: Counter[str] = Counter()
    para_lengths: list[int] = []
    sent_lengths: list[int] = []

    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        match = FRONTMATTER_RE.match(text)
        frontmatter = match.group(1) if match else ""
        body = strip_frontmatter(text)

        if frontmatter:
            year_counts[extract_year(frontmatter)] += 1
            for line in frontmatter.splitlines():
                if ":" in line:
                    key_counts[line.split(":", 1)[0].strip()] += 1
            for tag in extract_tags(frontmatter):
                tag_counts[tag] += 1
        else:
            year_counts["unknown"] += 1

        paragraphs = [chunk.strip() for chunk in re.split(r"\n\s*\n", body) if chunk.strip()]
        sentences = [chunk.strip() for chunk in re.split(r"[。！？!?]\s*", body) if chunk.strip()]
        para_lengths.extend(len(chunk) for chunk in paragraphs)
        sent_lengths.extend(len(chunk) for chunk in sentences)

        if re.search(r"[「」]", body):
            patterns["中文引号"] += 1
        if re.search(r">\s", body):
            patterns["引用块"] += 1
        if re.search(r"\b[A-Za-z]{2,}\b", body):
            patterns["英文夹杂"] += 1
        if re.search(r"我想", body):
            patterns["我想"] += 1
        if re.search(r"我觉得", body):
            patterns["我觉得"] += 1
        if re.search(r"其实", body):
            patterns["其实"] += 1
        if re.search(r"但是", body):
            patterns["但是"] += 1
        if re.search(r"比如", body):
            patterns["比如"] += 1
        if re.search(r"于是", body):
            patterns["于是"] += 1
        if re.search(r"^1\.\s", body, re.M):
            patterns["数字列表"] += 1

    print(f"Corpus root: {root}")
    print(f"Markdown files: {len(files)}")
    print()

    print("Year distribution:")
    for year, count in sorted(year_counts.items()):
        print(f"  {year}: {count}")
    print()

    print("Frontmatter keys:")
    for key, count in key_counts.most_common():
        print(f"  {key}: {count}")
    print()

    print("Top tags:")
    for tag, count in tag_counts.most_common(15):
        print(f"  {tag}: {count}")
    print()

    print("Body stats:")
    print(f"  Paragraphs: {len(para_lengths)}")
    print(f"  Avg paragraph length: {statistics.mean(para_lengths):.1f}")
    print(f"  Median paragraph length: {statistics.median(para_lengths):.1f}")
    print(f"  Sentence-like units: {len(sent_lengths)}")
    print(f"  Avg sentence length: {statistics.mean(sent_lengths):.1f}")
    print(f"  Median sentence length: {statistics.median(sent_lengths):.1f}")
    print()

    print("Style markers:")
    for name, count in patterns.most_common():
        print(f"  {name}: {count}")


if __name__ == "__main__":
    main()
