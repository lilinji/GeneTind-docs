# Documentation project instructions

## About this project

- This repository is a Mintlify documentation site for OpenClaw and related learning content.
- Site configuration lives in `docs.json`.
- Content is mostly Markdown and MDX. Both `.md` and `.mdx` are used in this repo.
- The site uses language-aware navigation under `navigation.languages` in `docs.json`.
- English content usually lives at the repo root. Chinese content usually lives under `zh/`.
- Static assets live in folders such as `images/`, `logo/`, and `public/`.

## Current site structure

- Core product and onboarding content lives in `openclaw/` and `zh/openclaw/`.
- General documentation content lives in sections such as `guide/`, `guides/`, `concepts/`, `use-cases/`, `api-reference/`, `blog/`, `changelog/`, `showcase/`, `skills-market/`, `templates/`, and `contribute/`.
- Long-form imported or curated content also exists in `ml/` and `agentic-design-patterns/`.
- Do not assume every section is fully bilingual or newly written. Follow the existing structure before adding new folders.

## Terminology

- Use "OpenClaw" for new product-facing content.
- Use "AI assistant" for the product. Avoid "chatbot" except when contrasting terms.
- Use "Skill" for installable modules and capitalize it when referring to the OpenClaw feature.
- Use "Heartbeat" for scheduled checks.
- Format files as code: `SOUL.md`, `USER.md`, `IDENTITY.md`, `MEMORY.md`, `HEARTBEAT.md`.
- Preserve existing "Trellis" wording on legacy pages unless the task is explicitly a rebrand or terminology cleanup.

## Writing style

- Use active voice and second person.
- Keep sentences concise. One idea per sentence.
- Use sentence case for headings.
- Bold UI labels: Click **Settings**.
- Use code formatting for file names, commands, paths, URLs, and code identifiers.
- Use numbered lists for procedures. Keep each step short.
- Avoid adding new emoji unless you are quoting existing content.
- Prefer Mintlify built-in components over custom components.

## Editing rules for this repo

- Read `docs.json` before changing navigation, branding, links, or language structure.
- When you add a new page, add it to the correct language section in `docs.json` or it will stay hidden.
- Use root-relative internal links without file extensions.
- Keep language prefixes correct in links. Examples: `/openclaw/day/1` and `/zh/openclaw/day/1`.
- Match the surrounding directory convention before creating a new page. Do not invent a parallel structure when an existing section already fits.
- Treat `docs.json` as the source of truth for navigation labels, grouping, and external anchors.
- Do not add `pnpm` or `npm` workflow instructions unless the repository actually contains those scripts. This repo currently has no root `package.json`.
- Some terminal output may render Chinese text incorrectly. Do not rename files or navigation items based only on mojibake in console output. Verify the source file content first.

## Bilingual content

- For user-facing product documentation, prefer updating both English and Chinese when both sections already exist.
- Mirror paths when appropriate, for example `openclaw/...` and `zh/openclaw/...`.
- If a section is intentionally single-language or imported content, keep scope tight and avoid unnecessary duplication.
- When translating, keep code blocks, commands, file names, and config keys unchanged.

## Content boundaries

- Document user-facing setup, configuration, usage, examples, and troubleshooting.
- Do not document internal admin features or private endpoints.
- Do not include secrets, API keys, or private tokens in examples.
- Avoid opportunistic rebranding or broad terminology cleanup outside the requested scope.

## Validation

- Run `mint dev` to preview locally.
- Run `mint broken-links` after adding or moving pages.
- Run `mint validate` before finishing larger documentation changes.
- Run `mint a11y` when the task changes structure, components, or accessibility-sensitive content.
- Respect `.mintignore`. Content under `.tmp/`, `.qodo/`, and excluded directories such as `GeneTind-Life-Skills/` should not be treated as published docs.
