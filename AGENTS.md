# AGENTS.md — Writter Article Polishing Workspace

## Project Purpose

This workspace exists to polish Markdown articles for Diff without re-explaining the same constraints in every session.

Primary source corpus used to derive the style baseline:

`/Users/diffwang/Library/Mobile Documents/iCloud~md~obsidian/Documents/diff-blog-source`

## Default Workflow

When the user asks to polish, revise, refine, smooth, correct, organize, or directly provides a Markdown article or file path, you must use:

`.agents/skills/diff-article-polisher/SKILL.md`

These instructions apply to all article-polishing tasks initiated from this workspace, even when the target Markdown file lives outside this repository.

## Non-Negotiable Constraints

- Preserve the author's original meaning, viewpoint, value judgments, and faith expressions.
- Edit the source Markdown in place unless the user asks for another output form.
- Never modify the frontmatter/header block at the top of the Markdown file.
- Only edit the article body.
- Prefer the minimum necessary edit that improves readability.
- Keep the author's natural voice, including some intentional roughness, colloquial phrasing, rhetorical questions, and pacing.
- Do not flatten the writing into a generic polished essay voice.
- At sentence level, remove semantic overlap before pursuing elegance.
- In observational or descriptive sentences, prefer concrete visible actions over stock idioms or abstract phrasing.
- Keep the verb/action chain stable inside one sentence unless a turn is intentional and clearly earned.
- Let images unfold along one visual or spatial path instead of jumping between unrelated objects.
- Preserve effective rhythmic repetition; remove repetition that adds no rhythm, escalation, or focus.

## Scope Guard

For article-polishing tasks:

1. Read the target file.
2. Identify and lock the frontmatter block.
3. Follow the workflow in `.agents/skills/diff-article-polisher/SKILL.md`.
4. Edit only the body content.
5. Briefly report what changed and confirm that the header was left untouched.
