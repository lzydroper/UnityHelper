---
name: changesrecorder
description: Use this skill whenever adding a new project feature or user-facing capability so a dated Markdown change note is created under Docs/Changes using the YYMMDDNN_title.md convention, with Chinese note content by default.
---

# ChangesRecorder

## Purpose

When a task adds a new feature, record the update in `Docs/Changes` as part of the same work. The record should be short, factual, and tied to what actually changed.

## When To Use

Use this skill when the current task introduces a new feature, capability, option, workflow, UI behavior, API behavior, or project-level automation.

Do not create a change note for pure refactors, formatting-only edits, dependency housekeeping, or bug fixes unless the user asks for one or the work also adds a feature.

## File Naming

Create the note at:

```text
Docs/Changes/YYMMDDNN_title.md
```

Rules:

- `YY`, `MM`, `DD`, and `NN` are all two-digit numbers.
- `YYMMDD` comes from the user's current local date for the task.
- `NN` is the daily sequence number. List existing files matching `YYMMDD??_*.md`; use the next number after the highest existing value, or `01` if none exist.
- `title` is a concise ASCII slug that names the main feature. Prefer lowercase words separated by hyphens. Follow an existing project convention if one is already present.

Example: `26052601_initiate.md` is the first change note for May 26, 2026.

## Language

Write the body content of the Markdown change note in Simplified Chinese by default.

Keep the document structure in English: metadata field names must be `Date`, `Code`, and `Type`; section headings must be `Summary`, `Changes`, `Files`, `Verification`, and `Notes`; the default type value is `Feature`.

Keep file paths, command names, code identifiers, API names, and literal filenames in their original spelling inside code spans. Use another body language only when the user explicitly asks for it or the existing project convention clearly requires it.

## Workflow

1. Finish enough of the implementation to know the real behavioral surface.
2. Ensure `Docs/Changes` exists.
3. Determine the next filename from the naming rules.
4. Write the change note using the template below.
5. Include the change note in the same final status as the feature work.

## Note Template

```markdown
# 功能标题

Date: YYYY-MM-DD
Code: YYMMDDNN
Type: Feature

## Summary

用一到两句话说明新增功能及其目的。

## Changes

- 新增的具体行为或能力。
- 重要实现细节，保持简洁。

## Files

- `path/to/file`

## Verification

- 命令、测试、人工检查，或写明“未运行”并给出简短原因。

## Notes

- 后续工作、兼容性说明或迁移细节。没有内容时写“无”。
```

Keep the note useful for future maintainers. Avoid broad claims, marketing language, and implementation speculation that is not visible in the finished change.
