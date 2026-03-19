---
name: ui-ux-pro-max
description: "Core design intelligence engine. Not invoked directly — used by /create, /design-system, /export, /build, and /review."
---

# UI/UX Pro Max - Design Intelligence

Design intelligence for web and mobile: 161 product types, 67 styles, 161 color palettes, 57 font pairings, 99 UX guidelines, 25 chart types, 6 stacks.

## Search Commands

```bash
# Design system (primary use — run before generating any UI)
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "<query>" --design-system

# With persistence across sessions
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "<query>" --design-system --persist -p "ProjectName"

# Domain search
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "<query>" --domain <domain>
# Domains: style | color | typography | product | landing | chart | ux | icons | google-fonts

# Stack-specific guidelines
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "<query>" --stack <stack>
# Stacks: react | nextjs | vue | nuxtjs | nuxt-ui | svelte | astro | swiftui | flutter | react-native | shadcn | html-tailwind | jetpack-compose
```

## Rule Priority

| Priority | Category | Impact | Domain |
|----------|----------|--------|--------|
| 1 | Accessibility | CRITICAL | `ux` |
| 2 | Touch & Interaction | CRITICAL | `ux` |
| 3 | Performance | HIGH | `ux` |
| 4 | Style Selection | HIGH | `style`, `product` |
| 5 | Layout & Responsive | HIGH | `ux` |
| 6 | Typography & Color | MEDIUM | `typography`, `color` |
| 7 | Animation | MEDIUM | `ux` |
| 8 | Forms & Feedback | MEDIUM | `ux` |
| 9 | Navigation | HIGH | `ux` |
| 10 | Charts & Data | LOW | `chart` |

## Reference Files

Read these only when the task requires detailed rules for that category:

- `.claude/skills/ui-ux-pro-max/references/rules-critical.md` — Accessibility + Touch (P1-P2)
- `.claude/skills/ui-ux-pro-max/references/rules-high.md` — Performance + Style + Layout (P3-P5)
- `.claude/skills/ui-ux-pro-max/references/rules-medium.md` — Typography + Animation + Forms + Nav (P6-P9)
- `.claude/skills/ui-ux-pro-max/references/stack-guidelines.md` — Stack-specific patterns

## When to Use

Use this skill when the task involves: UI structure, visual design decisions, component creation, UX quality, accessibility, choosing colors/typography/layout, or reviewing UI code.

Skip for: pure backend, API design, DB schema, infrastructure, non-visual scripts.
