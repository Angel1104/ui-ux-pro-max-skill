# [UI UX Pro Max](https://uupm.cc)

<p align="center">
  <a href="https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/releases"><img src="https://img.shields.io/github/v/release/nextlevelbuilder/ui-ux-pro-max-skill?style=for-the-badge&color=blue" alt="GitHub Release"></a>
  <img src="https://img.shields.io/badge/reasoning_rules-161-green?style=for-the-badge" alt="161 Reasoning Rules">
  <img src="https://img.shields.io/badge/UI_styles-84-purple?style=for-the-badge" alt="84 UI Styles">
  <img src="https://img.shields.io/badge/stacks-13-orange?style=for-the-badge" alt="13 Stacks">
  <img src="https://img.shields.io/badge/python-3.x-yellow?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.x">
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/uipro-cli"><img src="https://img.shields.io/npm/v/uipro-cli?style=flat-square&logo=npm&label=CLI" alt="npm"></a>
  <a href="https://www.npmjs.com/package/uipro-cli"><img src="https://img.shields.io/npm/dm/uipro-cli?style=flat-square&label=downloads" alt="npm downloads"></a>
  <a href="https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/stargazers"><img src="https://img.shields.io/github/stars/nextlevelbuilder/ui-ux-pro-max-skill?style=flat-square&logo=github" alt="GitHub stars"></a>
  <a href="https://paypal.me/uiuxpromax"><img src="https://img.shields.io/badge/PayPal-Support%20Development-00457C?style=flat-square&logo=paypal&logoColor=white" alt="PayPal"></a>
</p>

An AI skill that provides design intelligence for building professional UI/UX across multiple platforms and frameworks.

<p align="center">
  <a href="https://uupm.cc">
    <img src="screenshots/website.png" alt="UI UX Pro Max" width="800">
  </a>
</p>

<p align="center">
  <b>If you find this useful, consider supporting the project:</b><br><br>
  <a href="https://paypal.me/uiuxpromax"><img src="https://img.shields.io/badge/PayPal-Donate-00457C?style=for-the-badge&logo=paypal&logoColor=white" alt="PayPal Donate"></a>
</p>

<p align="center">
  <i>Other projects</i><br>
  <a href="https://nextlevelbuilder.io">NextLevelBuilder.io</a> | <a href="https://goclaw.sh">GoClaw.sh</a> | <a href="https://claudekit.cc">ClaudeKit.cc</a> | <a href="https://tose.sh">TOSE.sh</a>
</p>

## The Pipeline

Every project follows this flow. Each command asks questions and guides you to the next step.

```
/create  →  /design-system  →  /export  →  /build  →  /review
  (1)           (2)               (3)         (4)         (5)
context      colors, fonts     code/figma   pages &     audit
& goals      components        /pencil     components
              tokens
```

| Command | What it does | Run |
|---------|-------------|-----|
| `/create` | Gathers project brief — type, audience, goals | Once |
| `/design-system` | Generates complete design system — style, colors, fonts, tokens | Once |
| `/export` | Exports to Code (any stack), Figma, or Pencil | Once per target |
| `/build` | Builds pages, sections, and components | Repeat |
| `/review` | Audits for accessibility, performance, UX | Repeat |

### Design Tools

| Command | What it does |
|---------|-------------|
| `/figma` | Push designs to Figma Desktop via figma-bridge MCP |
| `/pencil` | Create visual mockups in .pen files |
| `/design` | Logo, CIP, icons, social photos |
| `/banner` | Social media, ads, website heroes, print banners |
| `/slides` | HTML presentations with Chart.js |
| `/brand` | Brand voice, visual identity, messaging |
| `/styling` | shadcn/ui components, Tailwind, dark mode |
| `/help` | Full usage guide |

## How Design System Generation Works

```
┌─────────────────────────────────────────────────────────────────┐
│  1. USER REQUEST                                                │
│     "Build a landing page for my beauty spa"                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  2. MULTI-DOMAIN SEARCH (5 parallel searches)                   │
│     • Product type matching (161 categories)                    │
│     • Style recommendations (84 styles)                         │
│     • Color palette selection (161 palettes)                    │
│     • Landing page patterns (34 patterns)                       │
│     • Typography pairing (73 font combinations)                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  3. REASONING ENGINE                                            │
│     • Match product → UI category rules (161 rules)             │
│     • Execute Decision_Rules against query                       │
│     • Apply style priorities (BM25 ranking)                     │
│     • Filter anti-patterns for industry                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  4. COMPLETE DESIGN SYSTEM OUTPUT                               │
│     Pattern + Style + Colors + Typography + Effects             │
│     + Anti-patterns to avoid + Pre-delivery checklist           │
└─────────────────────────────────────────────────────────────────┘
```

Example output:

```
+-----------------------------------------------------------------------------------------+
|  TARGET: Serenity Spa - RECOMMENDED DESIGN SYSTEM                                       |
+-----------------------------------------------------------------------------------------+
|  PATTERN: Hero-Centric + Social Proof                                                   |
|  STYLE:   Soft UI Evolution                                                             |
|  COLORS:  Primary #E8B4B8 · Secondary #A8D5BA · CTA #D4AF37 · BG #FFF5F5               |
|  FONTS:   Cormorant Garamond / Montserrat                                               |
|  AVOID:   Bright neon · Harsh animations · AI purple/pink gradients                    |
+-----------------------------------------------------------------------------------------+
```

## Features

- **84 UI Styles** — Glassmorphism, Claymorphism, Minimalism, Brutalism, Neumorphism, Bento Grid, Liquid Glass, and more
- **161 Color Palettes** — Industry-specific palettes aligned 1:1 with 161 product types
- **73 Font Pairings** — Curated typography with Google Fonts imports
- **34 Landing Patterns** — Conversion-optimized page structures
- **25 Chart Types** — Recommendations for dashboards and analytics
- **13 Tech Stacks** — Framework-specific guidelines (see below)
- **99 UX Guidelines** — Best practices, anti-patterns, and accessibility rules
- **161 Reasoning Rules** — Industry-specific Decision_Rules executed programmatically

### Supported Stacks (13)

| Category | Stacks |
|----------|--------|
| **Web** | HTML + Tailwind, shadcn/ui |
| **React Ecosystem** | React, Next.js |
| **Vue Ecosystem** | Vue, Nuxt.js, Nuxt UI |
| **Other Web** | Svelte, Astro |
| **iOS** | SwiftUI |
| **Android** | Jetpack Compose |
| **Cross-Platform** | React Native, Flutter |

### Available Styles (84)

<details>
<summary><b>General Styles (49)</b></summary>

| # | Style | Best For |
|---|-------|----------|
| 1 | Minimalism & Swiss Style | Enterprise apps, dashboards, documentation |
| 2 | Neumorphism | Health/wellness apps, meditation platforms |
| 3 | Glassmorphism | Modern SaaS, financial dashboards |
| 4 | Brutalism | Design portfolios, artistic projects |
| 5 | 3D & Hyperrealism | Gaming, product showcase, immersive |
| 6 | Vibrant & Block-based | Startups, creative agencies, gaming |
| 7 | Dark Mode (OLED) | Night-mode apps, coding platforms |
| 8 | Accessible & Ethical | Government, healthcare, education |
| 9 | Claymorphism | Educational apps, children's apps, SaaS |
| 10 | Aurora UI | Modern SaaS, creative agencies |
| 11 | Retro-Futurism | Gaming, entertainment, music platforms |
| 12 | Flat Design | Web apps, mobile apps, startup MVPs |
| 13 | Skeuomorphism | Legacy apps, gaming, premium products |
| 14 | Liquid Glass | Premium SaaS, high-end e-commerce |
| 15 | Motion-Driven | Portfolio sites, storytelling platforms |
| 16 | Micro-interactions | Mobile apps, touchscreen UIs |
| 17 | Inclusive Design | Public services, education, healthcare |
| 18 | Zero Interface | Voice assistants, AI platforms |
| 19 | Soft UI Evolution | Modern enterprise apps, SaaS |
| 20 | Neubrutalism | Gen Z brands, startups, Figma-style |
| 21 | Bento Box Grid | Dashboards, product pages, portfolios |
| 22 | Y2K Aesthetic | Fashion brands, music, Gen Z |
| 23 | Cyberpunk UI | Gaming, tech products, crypto apps |
| 24 | Organic Biophilic | Wellness apps, sustainability brands |
| 25 | AI-Native UI | AI products, chatbots, copilots |
| 26 | Memphis Design | Creative agencies, music, youth brands |
| 27 | Vaporwave | Music platforms, gaming, portfolios |
| 28 | Dimensional Layering | Dashboards, card layouts, modals |
| 29 | Exaggerated Minimalism | Fashion, architecture, portfolios |
| 30 | Kinetic Typography | Hero sections, marketing sites |
| 31 | Parallax Storytelling | Brand storytelling, product launches |
| 32 | Swiss Modernism 2.0 | Corporate sites, architecture, editorial |
| 33 | HUD / Sci-Fi FUI | Sci-fi games, space tech, cybersecurity |
| 34 | Pixel Art | Indie games, retro tools, creative |
| 35 | Bento Grids | Product features, dashboards, personal |
| 36 | Spatial UI (VisionOS) | Spatial computing apps, VR/AR |
| 37 | E-Ink / Paper | Reading apps, digital newspapers |
| 38 | Gen Z Chaos / Maximalism | Gen Z lifestyle, music artists |
| 39 | Biomimetic / Organic 2.0 | Sustainability tech, biotech, health |
| 40 | Anti-Polish / Raw Aesthetic | Creative portfolios, artist sites |
| 41 | Tactile Digital / Deformable UI | Modern mobile apps, playful brands |
| 42 | Nature Distilled | Wellness brands, sustainable products |
| 43 | Interactive Cursor Design | Creative portfolios, interactive |
| 44 | Voice-First Multimodal | Voice assistants, accessibility apps |
| 45 | 3D Product Preview | E-commerce, furniture, fashion |
| 46 | Gradient Mesh / Aurora Evolved | Hero sections, backgrounds, creative |
| 47 | Editorial Grid / Magazine | News sites, blogs, magazines |
| 48 | Chromatic Aberration / RGB Split | Music platforms, gaming, tech |
| 49 | Vintage Analog / Retro Film | Photography, music/vinyl brands |

</details>

<details>
<summary><b>Landing Page Styles (8)</b></summary>

| # | Style | Best For |
|---|-------|----------|
| 1 | Hero-Centric Design | Products with strong visual identity |
| 2 | Conversion-Optimized | Lead generation, sales pages |
| 3 | Feature-Rich Showcase | SaaS, complex products |
| 4 | Minimal & Direct | Simple products, apps |
| 5 | Social Proof-Focused | Services, B2C products |
| 6 | Interactive Product Demo | Software, tools |
| 7 | Trust & Authority | B2B, enterprise, consulting |
| 8 | Storytelling-Driven | Brands, agencies, nonprofits |

</details>

<details>
<summary><b>BI/Analytics Dashboard Styles (10)</b></summary>

| # | Style | Best For |
|---|-------|----------|
| 1 | Data-Dense Dashboard | Complex data analysis |
| 2 | Heat Map & Heatmap Style | Geographic/behavior data |
| 3 | Executive Dashboard | C-suite summaries |
| 4 | Real-Time Monitoring | Operations, DevOps |
| 5 | Drill-Down Analytics | Detailed exploration |
| 6 | Comparative Analysis Dashboard | Side-by-side comparisons |
| 7 | Predictive Analytics | Forecasting, ML insights |
| 8 | User Behavior Analytics | UX research, product analytics |
| 9 | Financial Dashboard | Finance, accounting |
| 10 | Sales Intelligence Dashboard | Sales teams, CRM |

</details>

## Installation

### Using Claude Marketplace (Claude Code)

```
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill
```

### Using CLI (Recommended)

```bash
npm install -g uipro-cli
cd /path/to/your/project
uipro init --ai claude      # Claude Code
uipro init --ai cursor      # Cursor
uipro init --ai windsurf    # Windsurf
uipro init --ai copilot     # GitHub Copilot
uipro init --ai kiro        # Kiro
uipro init --ai codex       # Codex CLI
uipro init --ai gemini      # Gemini CLI
uipro init --ai trae        # Trae
uipro init --ai opencode    # OpenCode
uipro init --ai roocode     # Roo Code
uipro init --ai continue    # Continue
uipro init --ai codebuddy   # CodeBuddy
uipro init --ai droid       # Droid (Factory)
uipro init --ai all         # All assistants
```

### Other CLI Commands

```bash
uipro versions              # List available versions
uipro update                # Update to latest version
uipro init --offline        # Use bundled assets, skip download
```

## Prerequisites

Python 3.x — no external dependencies.

```bash
python3 --version       # Check
brew install python3    # macOS
sudo apt install python3  # Ubuntu/Debian
winget install Python.Python.3.12  # Windows
```

## Usage

### Skill Mode (Auto-activate)

The skill activates automatically for UI/UX requests. Just chat naturally:

```
Build a landing page for my SaaS product
Create a dashboard for healthcare analytics
Design a mobile app for food delivery
```

> **Trae**: Switch to **SOLO** mode first.

### Workflow Mode (Slash Command)

For platforms that use slash commands (Kiro, Copilot, Roo Code):

```
/ui-ux-pro-max Build a landing page for my SaaS product
```

### Direct Search Commands

```bash
# Generate complete design system
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "beauty spa" --design-system -p "Serenity"

# Domain search
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "glassmorphism" --domain style
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "elegant serif" --domain typography
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "dashboard" --domain chart

# Stack-specific guidelines
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "form validation" --stack react
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "server components" --stack nextjs
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "composable" --stack vue
```

### Persist Design System Across Sessions

```bash
# Save global design system
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "SaaS dashboard" --design-system --persist -p "MyApp"

# Add page-specific overrides
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "checkout flow" --design-system --persist -p "MyApp" --page "checkout"
```

Creates:

```
design-system/
├── BRIEF.md            # Project context (written by /create)
├── MASTER.md           # Global design system (colors, fonts, tokens)
└── pages/
    └── checkout.md     # Page overrides (only deviations from MASTER)
```

When building a page, Claude reads `MASTER.md` first, then checks for a page override.

## Architecture & Contributing

```
src/ui-ux-pro-max/           # Source of truth
├── data/                    # CSV databases (161 products, 84 styles, 73 fonts...)
│   └── stacks/              # 13 stack-specific CSVs
├── scripts/                 # BM25 search engine + design system generator
└── templates/               # Platform configs (claude, cursor, windsurf...)

cli/                         # npm package (uipro-cli)
├── assets/                  # Copy of src/ — synced before publish
└── src/                     # CLI source (TypeScript)

.claude/skills/              # Claude Code skills
├── ui-ux-pro-max/           # Core engine (symlinks to src/)
├── create/                  # /create — project intake
├── design-system/           # /design-system — token generation
├── build/                   # /build — page generation
├── export/                  # /export — code/figma/pencil output
├── review/                  # /review — UX audit
├── figma/                   # /figma — Figma Desktop bridge
├── pencil/                  # /pencil — .pen file design
└── help/                    # /help — usage guide
```

### Contributing

```bash
# 1. Clone
git clone https://github.com/nextlevelbuilder/ui-ux-pro-max-skill.git
cd ui-ux-pro-max-skill

# 2. Make changes in src/ui-ux-pro-max/

# 3. Run data integrity tests
python3 src/ui-ux-pro-max/scripts/test_integrity.py

# 4. Sync to CLI assets
cd cli && npm run sync

# 5. Build and test CLI
bun run build
node dist/index.js init --ai claude --offline

# 6. Create PR (never push to main)
git checkout -b feat/your-feature
git commit -m "feat: description"
git push -u origin feat/your-feature
gh pr create
```

> Note: For Continue use `.continue/skills/`, for Droid use `.factory/skills/`.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=nextlevelbuilder/ui-ux-pro-max-skill&type=Date)](https://star-history.com/#nextlevelbuilder/ui-ux-pro-max-skill&Date)
