# AGENTS.md — Baituzhan (百图斩) Skill

Guidance for AI coding agents (Codex, Claude Code, Kimi, Hermes, etc.) working in or with this repository.

## What this repo is

A reusable **style-agnostic illustration-replication skill package**. Two phases:

1. **Style harvesting (斩风格 / archiving)** — the user supplies 1–3 reference images of ANY visual style → the agent analyzes them with the 8-dimension framework in `references/style-guide.md` → writes a **style archive** to `styles/<style-name>.md` (breakdown table, verbatim EN/CN anchor paragraphs, negative constraints, scene-translation hints, default aspect ratio).
2. **Generation (出图)** — turn an article or a one-line brief into unified-style illustrations using a chosen archive.

Ships with one built-in example archive: `styles/watercolor-sketch.md` (watercolor reportage sketch; reference image `assets/example-watercolor-sketch.jpeg`).

## Entry points

| File | Role |
|------|------|
| `SKILL.md` | Canonical workflow (Chinese). Read this first. |
| `references/style-guide.md` | Generic 8-dimension style breakdown framework, anchor-writing rules, universal negative constraints, scene-translation table, and the new-style archiving SOP incl. the `styles/<name>.md` file format contract. |
| `styles/*.md` | Style archives. Each contains three fenced code blocks: ` ```anchor-en `, ` ```anchor-cn `, ` ```negative ` — parsed by regex by the script. |
| `scripts/build_prompt.py` | Deterministic prompt assembler (stdlib only). CLI: `--scene` (required, CN), `--scene-en` (optional EN), `--ratio` (default `16:9`), `--style <name>`, `--anchor-file <path>`, `--list-styles`. Prints EN prompt + negatives + CN prompt. Falls back to the embedded watercolor-sketch anchor when no style is specified. |
| `tests/test_build_prompt.py` | Stdlib unittest suite. Run: `python tests/test_build_prompt.py` from repo root. |
| `assets/` | Reference images, one per style archive (naming mirrors the archive name). |
| `examples/` | Real outputs + the prompt sheets that produced them (filled after field tests). |

## The two generation modes (details in SKILL.md)

1. **Article mode** — user supplies an article → pick 2–4 key scenes (conflict/turning point > person in action > relationship/atmosphere > abstract idea translated into concrete people doing things) → for each scene run `scripts/build_prompt.py --style <name> --scene "..."` → generate images one by one.
2. **Brief mode** — user supplies a one-line story/request → assemble a single prompt the same way → generate one image.

## Image generation backends

After prompts are assembled, generate with whatever backend is available, in this priority:

1. A backend the **user explicitly named** (e.g. GPT image2 / gpt-image API, nano banana / Gemini image generation).
2. The Kimi `image_generation` plugin: supports `--reference-image`, the strongest style-locking mechanism — upload the style's reference image from `assets/` via its `image-to-url` command first, then pass the public URL to every `generate` call.
3. Any other local image tool (即梦, Midjourney, etc.).

**If no backend is available**: do NOT pretend to generate. Output the complete, detailed bilingual prompt list (anchor + scene + negative constraints, one block per image) so the user can edit and paste it into any tool themselves.

## Hard rules (do not break)

1. Reuse the style anchor **verbatim** on every generation; never paraphrase or shorten it.
2. All images in one batch share the same style archive and aspect ratio; only the scene description changes.
3. Always append the negative constraints; the four bans — `no artist signature, no dates, no timestamps, no watermark` — are never removed.
4. **The generated image must not contain any artist signature, date, timestamp, or watermark.** Reference images often carry them and models mimic them — visually inspect every output and regenerate with tightened negatives if they appear.
5. **Never put a real artist's name in a prompt or anchor** — it triggers copyright moderation (observed HTTP 403). Style fidelity comes from the reference image + generic description, not the name.
6. After each generation, verify against the archive's breakdown table. Regenerate with tightened negatives if it drifts.

## Conventions

- Prompts are assembled in English for generation; the Chinese prompt is for CN-native tools and human review.
- Default aspect ratio `16:9` (WeChat official-account cover); the style archive may declare its own default.
- Style archive filenames: lowercase, hyphenated English, e.g. `styles/pixel-noir.md`; reference images live in `assets/` with a matching name, e.g. `assets/example-pixel-noir.jpeg`.
- Scripts are stdlib-only Python 3; no dependencies to install.
