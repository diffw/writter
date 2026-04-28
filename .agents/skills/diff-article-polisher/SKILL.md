---
name: diff-article-polisher
description: 当用户提供 Markdown 文章、语音转写稿、文件路径，或要求对文章做打磨、修正、润色、断句、分段、整理时使用。必须直接处理正文，完整保留作者原意、观点、价值观与个人语言风格，且绝不修改 Markdown 头部 frontmatter。
---

# Diff Article Polisher

Use this skill whenever the task is to polish one of Diff's Markdown articles, especially when the source is a voice-to-text draft or a long-form personal post.

## Core Objective

Improve readability without changing authorship.

Priority order:

1. Preserve meaning
2. Preserve viewpoint and value judgments
3. Preserve voice and rhythm
4. Improve clarity, flow, paragraphing, and typo-level correctness

## Required Workflow

1. Read the Markdown file or article text.
2. Detect whether it starts with a frontmatter block delimited by `---`.
3. Lock that frontmatter block completely.
4. Read the body and identify the article mode:
   - reflection / essay
   - spiritual note / prayer / testimony
   - family or life narrative
   - gratitude list
   - chronology / journal fragment
   - voice-transcribed draft
5. Read [references/editing-rules.md](references/editing-rules.md).
6. Read [references/style-profile.md](references/style-profile.md) when you need the detailed style baseline or want to verify tone decisions.
7. For sentence-level polishing, inspect:
   - semantic overlap between nearby nouns or images
   - whether repetition is rhythmic/effective or merely redundant
   - whether the action chain (`看` / `想到` / `感到` / etc.) is stable
   - whether an abstract idiom should be turned back into a concrete image
   - whether the sentence follows one visual or spatial path
8. Edit only the body.
9. Run the self-check in `references/editing-rules.md` before finishing.

## Hard Constraints

- Do not rewrite the article into a different argument.
- Do not add new opinions, stronger claims, or softer claims.
- Do not remove discomfort, tension, contradiction, confession, or sharpness if they are part of the author's real meaning.
- Do not normalize everything into formal prose.
- Do not touch `title`, `date`, `draft`, `tags`, or any other header field.
- Do not reorder or reformat the header.

## Editing Heuristics

- Fix obvious typos, malformed wording, broken grammar, and awkward repetition when they reduce readability.
- Split paragraphs when the spoken flow became too dense.
- Merge fragments only when the original rhythm clearly remains intact.
- Keep signature wording such as `我想`, `我觉得`, `其实`, `但是`, `说实话`, rhetorical questions, parentheses, and mild repetition when they sound authentic.
- Keep some spoken texture in transcript-like drafts. Remove only the noise, not the person.
- When the text uses numbered lists, gratitude items, timestamps, or diary fragments, preserve that structure unless a small local adjustment clearly helps.
- Remove semantic-overlap repetition first, especially when one image already contains another.
- In scene-description sentences, prefer concrete visible motion over ready-made idioms when the idiom weakens the image.
- Keep one sentence on one visual track when possible; do not let it jump across unrelated objects without purpose.
- Keep repeated verbs only when they create rhythm, focus, or escalation.
- If a sentence shifts from observation to reflection, make the turn late and clean rather than mixing every action at once.

## Markdown Boundaries

- Preserve headings, block quotes, lists, image links, and URLs unless the user asked to change them.
- If the article starts with frontmatter, return that block exactly as-is.
- If the user pastes a full Markdown document in chat instead of giving a file path, keep the header untouched and only revise the body.

## Refreshing the Corpus Analysis

If the style baseline needs to be refreshed because the corpus changed materially, run:

```bash
python3 .agents/skills/diff-article-polisher/scripts/analyze_corpus.py \
  --root "/Users/diffwang/Library/Mobile Documents/iCloud~md~obsidian/Documents/diff-blog-source"
```

Use the output as input to update `references/style-profile.md`.
