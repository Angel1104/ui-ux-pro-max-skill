# Architecture & Project Internals

This document explains what this project is, why it exists, how it works internally, what each skill does, and every architectural decision made.

---

## What Is This?

A design intelligence skill for AI coding assistants (Claude Code, Cursor, Windsurf, etc.).

When you ask Claude to "build a landing page for a yoga studio", it has no idea what colors, fonts, or layout patterns work for that industry. This skill fixes that — it gives Claude a searchable database of 161 product types, 84 UI styles, 161 color palettes, 73 font pairings, 99 UX guidelines, and 13 stack-specific rules.

The result: Claude picks the right design system for your project before writing a single line of code.

---

## Why We Built It This Way

### Zero external dependencies
The search engine is pure Python 3 (BM25 + regex). No pip install, no API calls, no internet required. It runs locally in milliseconds.

### Zero tokens burned on search
The databases live in CSV files. Search runs as a subprocess (`python3 search.py "query"`). Claude only sees the output — 3-5 rows of relevant data — not the entire 161-row database. This is the key efficiency decision.

### Slim SKILL.md = fewer tokens always loaded
Every skill's `SKILL.md` is loaded into context on every invocation. We cut `ui-ux-pro-max/SKILL.md` from 44KB (~11,000 tokens) down to 2.3KB (~580 tokens). Detailed rules live in `references/` files that are only read when needed.

---

## How the Search Engine Works

```
User query: "luxury e-commerce fashion"
        │
        ▼
search.py (CLI entry point)
        │
        ▼
core.py — BM25 search
  ├── Tokenize query
  ├── Score all rows in CSV against query tokens
  └── Return top 3 ranked rows
        │
        ▼
design_system.py (when --design-system flag is used)
  ├── Run 5 parallel domain searches: product, style, color, landing, typography
  ├── Apply Decision_Rules from ui-reasoning.csv (programmatic overrides)
  └── Output MASTER.md or print formatted result
```

### BM25
Standard probabilistic ranking (k1=1.5, b=0.75). Searches across designated columns per domain (e.g. for `style`: Style Category + Keywords + Best For + AI Prompt Keywords).

### Decision_Rules
`ui-reasoning.csv` has a `Decision_Rules` JSON column per product type. Example:
```json
{"if_luxury": "switch-to-Liquid Glass", "if_budget": "switch-to-Flat Design"}
```
`design_system.py` parses these and executes them against the query at runtime. If your query contains "luxury", the style switches automatically — no hardcoded logic.

### Domain Auto-Detection
If you don't pass `--domain`, `core.py` scores the query against keyword lists for each domain and picks the best match.

---

## File Structure

```
src/ui-ux-pro-max/               # Source of truth — edit here
├── data/
│   ├── products.csv             # 161 product types + style/color/landing recommendations
│   ├── styles.csv               # 84 UI styles + CSS keywords + AI prompts + checklists
│   ├── colors.csv               # 161 color palettes (primitive tokens)
│   ├── typography.csv           # 73 font pairings + Google Fonts URLs + Tailwind config
│   ├── landing.csv              # 34 landing page patterns + CTA placements
│   ├── charts.csv               # 25 chart types + Chart.js recommendations
│   ├── ux-guidelines.csv        # 99 UX rules (accessibility, touch, performance, nav)
│   ├── icons.csv                # Icon library recommendations
│   ├── components.csv           # Component specs
│   ├── google-fonts.csv         # Full Google Fonts index
│   ├── app-interface.csv        # Web app interface guidelines
│   ├── ui-reasoning.csv         # Decision_Rules JSON per product type
│   └── stacks/                  # 13 stack-specific CSV files
│       ├── html-tailwind.csv
│       ├── react.csv
│       ├── nextjs.csv
│       ├── vue.csv
│       ├── nuxtjs.csv
│       ├── nuxt-ui.csv
│       ├── svelte.csv
│       ├── astro.csv
│       ├── swiftui.csv
│       ├── flutter.csv
│       ├── react-native.csv
│       ├── shadcn.csv
│       └── jetpack-compose.csv
├── scripts/
│   ├── search.py                # CLI entry point (argparse)
│   ├── core.py                  # BM25 engine + domain detection
│   ├── design_system.py         # Full design system generation + Decision_Rules
│   └── test_integrity.py        # 114 data integrity checks
└── templates/
    ├── base/
    │   ├── skill-content.md     # Common SKILL.md content shared across platforms
    │   └── quick-reference.md   # Quick reference section (Claude only)
    └── platforms/               # Per-platform configs (claude.json, cursor.json, ...)
```

### Symlinks (don't edit these directly)
```
.claude/skills/ui-ux-pro-max/  →  src/ui-ux-pro-max/
.factory/skills/ui-ux-pro-max/ →  src/ui-ux-pro-max/
.shared/ui-ux-pro-max/         →  src/ui-ux-pro-max/
```

### CLI sync
`cli/assets/` is a flat copy of `src/`. Run before publishing:
```bash
cd cli && npm run sync
```
This is also wired into `prepublishOnly` so it runs automatically on `npm publish`.

---

## Skills Reference

Skills live in `.claude/skills/<name>/SKILL.md`. Claude Code loads the relevant SKILL.md when the trigger is matched.

### Pipeline Skills (run in order)

| Skill | Trigger | What It Does |
|-------|---------|-------------|
| `create` | `/create` | Asks 5 questions (type, audience, goal, idea, references). Writes `design-system/BRIEF.md`. |
| `design-system` | `/design-system` | Reads BRIEF.md, runs search engine with `--design-system --persist`, presents style/color/font choices, generates CSS tokens. |
| `export` | `/export` | Exports the confirmed design system to code (any stack), Figma, or Pencil. |
| `build` | `/build` | Builds a page, section, or component using the active design system. Repeatable. |
| `review` | `/review` | Audits generated UI for accessibility (WCAG), performance, and UX anti-patterns. |

### Pipeline State
`/create` writes `design-system/BRIEF.md` with a `Query:` field.
`/design-system` reads that file and uses `Query:` as the search input.
This allows pipeline state to persist across sessions without burning tokens on re-asking.

### Design Asset Skills

| Skill | Trigger | What It Does |
|-------|---------|-------------|
| `design` | `/design` | Routes to logo, CIP (corporate identity), icon, or social photo generation. |
| `banner` | `/banner` | Designs banners: social media, ads, web heroes, print. |
| `slides` | `/slides` | Creates HTML presentations with Chart.js, design tokens, and Duarte Sparkline emotion arcs. |
| `brand` | `/brand` | Brand voice, visual identity, messaging frameworks. |
| `ui-styling` | `/styling` | shadcn/ui components, Tailwind CSS patterns, dark mode. |

### Integration Skills

| Skill | Trigger | What It Does |
|-------|---------|-------------|
| `figma` | `/figma` | Sends designs to Figma Desktop via figma-bridge MCP (WebSocket broker). Supports HTML import with `data-figma-*` attributes that map to native Figma nodes with auto-layout and component sets. |
| `pencil` | `/pencil` | Creates visual mockups in `.pen` files using the Pencil MCP. Uses `get_guidelines`, `get_style_guide`, `batch_design` to build screens. |

### Meta Skills

| Skill | Trigger | What It Does |
|-------|---------|-------------|
| `help` | `/help` | Full usage guide: all commands, pipeline explanation, supported project types, stacks, quality rules, example conversation. |
| `ui-ux-pro-max` | (internal) | Core design intelligence router. Not invoked directly — used by all other skills. Points to reference files loaded on demand. |

### On-Demand Reference Files
`ui-ux-pro-max/references/` — loaded only when the task needs them:
- `rules-critical.md` — P1 Accessibility (WCAG 2.1 AA) + P2 Touch targets
- `rules-high.md` — P3 Performance + P4 Style selection + P5 Layout/responsive
- `rules-medium.md` — P6 Typography + P7 Animation + P8 Forms + P9 Navigation

---

## Data Integrity

Run before any commit that touches CSV files:

```bash
python3 src/ui-ux-pro-max/scripts/test_integrity.py
```

Checks 114 conditions:
- Required columns exist in every CSV
- No empty critical fields (Product Type, Style Category, etc.)
- All 13 stack CSVs present and valid
- Color token completeness (Primary, Secondary, Background, etc.)
- Typography entries have Google Fonts URLs
- No draft.csv files

---

## Stack CSVs — Column Schema

All 13 stack files use the same schema:

```
No, Category, Guideline, Description, Do, Don't, Code Good, Code Bad, Severity, Docs URL
```

Severity values: `critical`, `high`, `medium`, `low`

---

## Key Architectural Decisions

| Decision | Why |
|----------|-----|
| BM25 in pure Python, no dependencies | Runs everywhere, zero setup, no tokens |
| CSV as database | Human-readable, git-diffable, no DB setup |
| SKILL.md kept slim (< 3KB) | Loaded on every invocation — token cost matters |
| Reference files on demand | Only load what the current task needs |
| Decision_Rules as JSON in CSV | Rules stay with the data, not hardcoded in scripts |
| Pipeline state via BRIEF.md | Persists context across sessions without re-asking |
| Symlinks src/ → .claude/skills/ | Single source of truth, no manual sync for core files |
| cli/assets/ as flat copy | CLI bundle must be self-contained for offline installs |
| `prepublishOnly` auto-sync | Can't accidentally publish stale CLI assets |

---

## Contributing

1. All data edits go in `src/ui-ux-pro-max/data/`
2. Run `python3 src/ui-ux-pro-max/scripts/test_integrity.py` — must pass
3. Run `cd cli && npm run sync` to update CLI assets
4. Never push to `main` — always branch + PR
5. Branch naming: `feat/`, `fix/`, `data/`, `docs/`
