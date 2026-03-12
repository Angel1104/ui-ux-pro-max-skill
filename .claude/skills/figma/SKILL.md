---
name: figma
description: "Send designs to Figma Desktop via figma-bridge MCP. Supports HTML import (converts inline-styled HTML to native Figma nodes with auto-layout, components, and variants) plus individual node commands. Trigger: /figma, send to figma, create in figma, push to figma."
argument-hint: "[what to create in Figma]"
---

# Figma Design Bridge Skill

Sends designs directly to **Figma Desktop** using the figma-bridge MCP. Two modes:

1. **HTML Import** (recommended) — Send complete HTML with inline styles → automatic conversion to Figma nodes with auto-layout, components, and variants
2. **Node-by-node** (manual) — Create individual frames, text, shapes via direct commands

---

## Prerequisites — must do before anything

### 1. Start the broker (once per session)

```bash
bash /Users/angel/figma/mcp-bridge/start.sh
```

Idempotent — safe to run multiple times.

### 2. Open the plugin in Figma Desktop

1. Open Figma Desktop
2. Go to **Plugins > Development > Design System Bridge**
3. The plugin shows: `Bridge connected! Channel: ch_xxxxxxxx`
4. Copy that channel ID

### 3. Connect from Claude

```
connect_to_figma("<channel_id>")
```

---

## HTML Import (Primary Method)

The fastest way to create complex designs in Figma. Generate Figma-optimized HTML and send it in a single `import_html` call.

### How it works

```
Generate HTML with inline styles + data-figma-* attributes
    ↓
import_html({ html: "...", name: "My Design" })
    ↓
Plugin renders HTML → parses computed styles → creates Figma nodes
    ↓
Components + variants created automatically from data attributes
```

### Usage

```
import_html({
  html: "<div ...>...</div>",
  name: "Design System",
  x: 0,
  y: 0,
  createComponents: true
})
```

### HTML Format

HTML must use **inline styles** (no external CSS) and **data-figma-*** attributes for Figma-specific properties.

```html
<!-- Simple frame with text -->
<div data-figma-name="Hero Section"
     style="display:flex; flex-direction:column; gap:24px; padding:32px; background:#FFFFFF; border-radius:12px;">
  <h1 style="color:#111827; font-family:Inter; font-size:36px; font-weight:700;">Welcome</h1>
  <p style="color:#6B7280; font-family:Inter; font-size:16px;">Subtitle text here</p>
</div>
```

### Data Attributes

| Attribute | Purpose | Example |
|---|---|---|
| `data-figma-name` | Layer name in Figma | `"Hero Section"` |
| `data-figma-component="true"` | Create as Figma component | |
| `data-figma-variant` | Variant properties (comma-separated key=value) | `"Size=Large, Style=Primary"` |
| `data-figma-component-set` | Group variants into a component set | `"Button"` |
| `data-figma-sizing-h` | Layout sizing horizontal | `"FILL"`, `"HUG"`, `"FIXED"` |
| `data-figma-sizing-v` | Layout sizing vertical | `"FILL"`, `"HUG"`, `"FIXED"` |
| `data-figma-type` | Force node type | `"text"`, `"rectangle"`, `"ellipse"` |
| `data-figma-ignore="true"` | Skip this element during parsing | |
| `data-figma-clips="true"` | Clip content overflow | |
| `data-figma-opacity` | Node opacity (0-1) | `"0.8"` |
| `data-figma-text-auto-resize` | Text resize mode | `"WIDTH_AND_HEIGHT"`, `"HEIGHT"` |
| `data-figma-stroke-weight` | Explicit stroke weight | `"2"` |
| `data-figma-stroke-color` | Explicit stroke color | `"#D1D5DB"` |

### CSS → Figma Mapping

| CSS | Figma |
|---|---|
| `display:flex; flex-direction:column` | `layoutMode: VERTICAL` |
| `display:flex; flex-direction:row` | `layoutMode: HORIZONTAL` |
| `gap` | `itemSpacing` |
| `padding` | `paddingTop/Right/Bottom/Left` |
| `background-color` | `fills` (solid) |
| `border-radius` | `cornerRadius` |
| `border: Xpx solid #color` | `strokes` + `strokeWeight` |
| `color` | text fills |
| `font-family` | `fontName.family` |
| `font-weight` | `fontName.style` (400→Regular, 700→Bold, etc.) |
| `font-size` | `fontSize` |
| `text-align` | `textAlignHorizontal` |
| `align-items` | `counterAxisAlignItems` |
| `justify-content` | `primaryAxisAlignItems` |
| `overflow:hidden` | `clipsContent: true` |

### Creating Components with Variants

Use `data-figma-component-set` to group variants into a Figma ComponentSet:

```html
<!-- Button component set with 4 variants -->
<div data-figma-component-set="Button" style="display:flex; gap:32px;">

  <div data-figma-component="true" data-figma-variant="Style=Primary, Size=Default"
       style="display:flex; padding:12px 24px; background:#4F46E5; border-radius:8px; align-items:center;">
    <span style="color:#FFFFFF; font-family:Inter; font-size:14px; font-weight:500;">Primary</span>
  </div>

  <div data-figma-component="true" data-figma-variant="Style=Secondary, Size=Default"
       style="display:flex; padding:12px 24px; border:2px solid #D1D5DB; border-radius:8px; align-items:center;">
    <span style="color:#374151; font-family:Inter; font-size:14px; font-weight:500;">Secondary</span>
  </div>

  <div data-figma-component="true" data-figma-variant="Style=Primary, Size=Large"
       style="display:flex; padding:16px 32px; background:#4F46E5; border-radius:12px; align-items:center;">
    <span style="color:#FFFFFF; font-family:Inter; font-size:16px; font-weight:600;">Primary Large</span>
  </div>

  <div data-figma-component="true" data-figma-variant="Style=Secondary, Size=Large"
       style="display:flex; padding:16px 32px; border:2px solid #D1D5DB; border-radius:12px; align-items:center;">
    <span style="color:#374151; font-family:Inter; font-size:16px; font-weight:600;">Secondary Large</span>
  </div>
</div>
```

Result: A "Button" ComponentSet in Figma with 4 variants and proper variant properties (Style, Size).

### HTML Conventions

- **Top-level elements** → become top-level frames in the wrapper
- **Text-like tags** (`span`, `p`, `h1`-`h6`, `a`, `label`) with no child elements → Figma text nodes
- **Everything else** → Figma frames with auto-layout (if `display:flex`)
- **Inline styles only** — no external CSS, no classes (computed styles must be readable)
- **Fixed dimensions** — use px values, not responsive units
- **Fonts** — fallback chain: requested font → Inter → Roboto → Arial

---

## Available Tools

### HTML Import
| Tool | Use |
|---|---|
| `import_html` | Import HTML with inline styles into Figma as native nodes with components and variants |

### Node-by-node (Manual)
| Tool | Use |
|---|---|
| `connect_to_figma` | Connect via channel ID |
| `create_frame` | Create frame with auto-layout |
| `create_rectangle` | Create rectangle / shape |
| `create_text` | Create text node |
| `create_ellipse` | Create ellipse or circle |
| `modify_node` | Update any node property |
| `delete_node` | Delete a node |
| `get_node` | Read node properties |
| `get_page_structure` | Get full page tree |
| `set_variable` | Create/update Figma variables |
| `build_component` | Build design system component |
| `build_design_system` | Rebuild entire design system |
| `scroll_to_node` | Scroll viewport to a node |

### Read-only (figma-desktop)
| Tool | Use |
|---|---|
| `get_screenshot` | Screenshot of current Figma view |
| `get_design_context` | Full design context of selected element |
| `get_metadata` | File/page metadata |
| `get_variable_defs` | All variables defined in the file |

---

## Workflow: from design system to Figma

### Option A — HTML Import (recommended)

```
# 1. Get design system from ui-ux-pro-max
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "beauty spa" --design-system

# 2. Start broker + connect
bash /Users/angel/figma/mcp-bridge/start.sh
connect_to_figma("ch_xxxxxxxx")

# 3. Generate Figma-optimized HTML from design system and import
import_html({
  html: "<div data-figma-name='Design System' style='display:flex;flex-direction:column;gap:80px;padding:64px;background:#FFFFFF;'>...</div>",
  name: "Design System"
})

# 4. Screenshot to verify
get_screenshot()
```

### Option B — Set variables + HTML Import

When you want Figma variables AND visual components:

```
# 1. Sync tokens as Figma variables
set_variable({ name: "primary", value: "#E8B4B8", type: "COLOR" })
set_variable({ name: "secondary", value: "#A8D5BA", type: "COLOR" })

# 2. Import visual components via HTML
import_html({ html: "...", name: "Components" })
```

### Option C — Node-by-node (manual, for simple tweaks)

```
create_frame({ name: "Hero", width: 1440, height: 900, fills: "#FFF5F5" })
create_text({ parent: "Hero", content: "Hello", fontSize: 64 })
```

---

## Large HTML handling

HTML payloads over 500KB are automatically chunked by top-level elements. Each chunk is parsed and built independently. No special action needed — `import_html` handles this transparently.

---

## Figma plugin sandbox rules

When modifying `/Users/angel/figma/figma-plugin/code.js`:

- **No** spread operator `{...obj}` — use manual property assignment
- **No** optional chaining `obj?.prop` — use ternary: `obj ? obj.prop : undefined`
- **No** nullish coalescing `val ?? default` — use ternary: `val !== null ? val : default`
- `layoutSizingHorizontal = "FILL"` must be set **after** `appendChild()`
- Font loading: try document default → Inter → Roboto → Arial (with try-catch)

---

## When to use Figma vs Pencil

| Use `/figma` when | Use `/pencil` when |
|---|---|
| You need the design in Figma specifically | You want a quick mockup in the editor |
| Stakeholders need to review in Figma | You're designing standalone without Figma |
| You want Figma components with variants | You want design output in a .pen file |
| Design handoff to developers via Figma | Design is for internal review only |

---

## Troubleshooting

| Problem | Solution |
|---|---|
| `connect_to_figma` fails | Check broker is running: `curl localhost:18765/health` |
| Plugin shows "Disconnected" | Re-run the plugin in Figma, get new channel ID |
| Broker not starting | `cd /Users/angel/figma/mcp-bridge && npm install` then retry |
| Node not found | Use `get_page_structure()` to find the correct node ID |
| Font not rendering | Plugin tries Inter → Roboto → Arial fallback chain |
| Import timeout | Large HTML is auto-chunked; increase `IMPORT_HTML` timeout in protocol.mjs if needed |
