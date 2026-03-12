---
name: export
description: "Export your design system to Code, Figma, or Pencil. One-time setup step."
trigger: "/export"
argument-hint: "[code|figma|pencil]"
metadata:
  author: claudekit
  version: "1.0.0"
---

# Export — Design System Export

Export your design system to your chosen target. This is a one-time setup step.

<args>$ARGUMENTS</args>

## Pipeline

```
/create → /design-system → /export (you are here) → /build → /review
```

## Prerequisites

A design system must exist before exporting. Check for:
1. `design-system/MASTER.md` in the project (created by `/design-system` with `--persist`)
2. Or design system context from a previous `/design-system` run in the current conversation

If neither exists, tell the user:
> "No design system found. Run `/design-system` first to create one."

## Workflow

### Step 1: Choose Target

If `$ARGUMENTS` specifies a target (`code`, `figma`, `pencil`), route directly. Otherwise, ask:

**Ask:** "Where do you want to export your design system?"
Options:
- **Code** — Generate CSS variables, Tailwind config, or platform-specific tokens + base component files
- **Figma** — Push to Figma Desktop (variables + component frames via figma-bridge MCP)
- **Pencil** — Create a .pen file with component library (via Pencil MCP)

### Step 2A: Export to Code

Ask: "What tech stack?"
Options:
- HTML + Tailwind CSS
- React
- Next.js
- Vue / Nuxt
- Svelte
- shadcn/ui
- SwiftUI
- React Native
- Flutter
- Jetpack Compose

Then generate:
1. **CSS variables file** (`design-tokens.css`) with all tokens from MASTER.md
2. **Tailwind config** (`tailwind.config.js/ts`) if using Tailwind-based stack
3. **Base component files** for each component in the design system, using the stack's patterns
4. **Google Fonts import** link from typography selection

Output: List all created files and their locations.

### Step 2B: Export to Figma

Uses **HTML Import** via the `/figma` skill. This generates Figma-optimized HTML from the design system and sends it in a single `import_html` call.

**Step 2B.1: Generate Figma-optimized HTML**

From the design system (MASTER.md), generate HTML with:
- **Inline styles** for all colors, spacing, typography, shadows (no CSS classes)
- **`data-figma-name`** on every element for clean layer names
- **`data-figma-component="true"`** on each component variant
- **`data-figma-variant="Key=Value"`** for variant properties (Size, Style, State)
- **`data-figma-component-set="ComponentName"`** to group variants into Figma component sets
- **Fixed pixel dimensions** (not responsive — use 1440px desktop frames)
- **Separate frame per variant/state** (default, hover, disabled, etc.)

Example structure:
```html
<div data-figma-name="Design System" style="display:flex;flex-direction:column;gap:80px;padding:64px;background:#FFFFFF;">

  <!-- Color tokens as visual swatches -->
  <div data-figma-name="Colors" style="display:flex;flex-direction:column;gap:16px;">
    <h2 style="font-family:Inter;font-size:24px;font-weight:700;color:#111827;">Colors</h2>
    <div style="display:flex;gap:16px;">
      <div data-figma-name="Primary" style="width:72px;height:72px;background:#4F46E5;border-radius:12px;"></div>
      ...
    </div>
  </div>

  <!-- Button component set with variants -->
  <div data-figma-component-set="Button" style="display:flex;gap:32px;">
    <div data-figma-component="true" data-figma-variant="Style=Primary, Size=Default" ...>...</div>
    <div data-figma-component="true" data-figma-variant="Style=Secondary, Size=Default" ...>...</div>
  </div>

</div>
```

**Step 2B.2: Sync Figma variables (optional)**

For design tokens that should be Figma variables:
```
set_variable({ name: "primary/500", value: "#4F46E5", type: "COLOR" })
set_variable({ name: "spacing/4", value: 16, type: "FLOAT" })
```

**Step 2B.3: Import HTML**

```
import_html({ html: "<generated HTML>", name: "Design System", createComponents: true })
```

This creates all frames, text, components, and component sets (with variants) in one operation.

### Step 2C: Export to Pencil

Invoke the `/pencil` skill with the design system context:
1. Create a .pen file with design system components
2. Set up variables in the .pen file matching design tokens
3. Create reusable component instances for each component

### Step 3: Persist

If not already persisted, save the design system:
```bash
python3 skills/ui-ux-pro-max/scripts/search.py "$QUERY" --design-system --persist -p "$PROJECT_NAME"
```

### Step 4: Guide to Next Step

> "Design system exported! Now run `/build` to create pages, sections, and components using your design system. You can run `/build` as many times as you need."
