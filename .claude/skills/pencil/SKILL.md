---
name: pencil
description: "Create visual designs in Pencil (.pen files) using the Pencil MCP. Use when the user wants a visual mockup, UI design, or design file instead of code. Trigger: /pencil, design in pencil, create mockup, make a .pen file, diseñar en pencil, mockup visual."
argument-hint: "[what to design]"
---

# Pencil Design Skill

Creates visual designs directly in Pencil (.pen files) using the Pencil MCP tools. Use this when you want a **visual design / mockup** instead of code.

---

## When to use `/pencil` vs code

| Use `/pencil` when | Use code (default) when |
|---|---|
| You want a visual mockup to review before building | You need production-ready code |
| You're in the design exploration phase | The design is already decided |
| You want to share a design with stakeholders | You need something deployed |
| You want to iterate on layout visually | You want a working component |

---

## Workflow

### Step 1 — Get design context from ui-ux-pro-max

Before opening Pencil, run the design system generator to know what style, colors, and fonts to use:

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "<product description>" --design-system
```

Example:
```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "beauty spa wellness" --design-system
```

### Step 2 — Check editor state

Always start by checking what's currently open in Pencil:

```
get_editor_state()
```

If no document is open, create a new one or open an existing `.pen` file:

```
open_document("new")           # Create new empty file
open_document("path/to/file.pen")  # Open existing file
```

### Step 3 — Get design guidelines for the type of screen

Use the appropriate topic:

```
get_guidelines(topic="web-app")      # Web app / dashboard
get_guidelines(topic="landing-page") # Landing page
get_guidelines(topic="mobile-app")   # Mobile app
get_guidelines(topic="tailwind")     # Tailwind-based UI
get_guidelines(topic="design-system") # Design system / tokens
```

### Step 4 — Get a style guide

After guidelines, get visual inspiration:

```
get_style_guide_tags()   # Get available tags
get_style_guide(tags=["modern", "saas", "dark"], name=null)
```

Match the tags to what the design system generator recommended (e.g. if it recommended "Glassmorphism", use tags like `["glass", "dark", "modern"]`).

### Step 5 — Design with batch_design

Use `batch_design` to create nodes. Each operation on its own line:

```
foo=I("parent", { "type": "FRAME", "name": "Hero Section", "width": 1440, "height": 800 })
bar=I(foo, { "type": "TEXT", "content": "Your headline here", "fontSize": 56, "fontWeight": 700 })
btn=I(foo, { "type": "FRAME", "name": "CTA Button", "width": 200, "height": 56, "fills": [{"type":"SOLID","color":"#6366F1"}] })
```

Operations available:
- `foo=I("parent", {...})` — Insert new node
- `baz=C("nodeId", "parent", {...})` — Copy existing node
- `R("nodeId", {...})` — Replace node
- `U("nodeId", {...})` — Update node properties
- `D("nodeId")` — Delete node
- `M("nodeId", "parent", index)` — Move node
- `G("nodeId", "ai", "description")` — Generate AI image

### Step 6 — Validate visually

Periodically take a screenshot to verify the design looks right:

```
get_screenshot()
```

Also check layout structure if positioning seems off:

```
snapshot_layout()
```

---

## Design rules for Pencil

- Max 25 operations per `batch_design` call — break large designs into chunks
- Use `snapshot_layout()` before inserting to find the right parent and position
- Use `get_variables()` to check existing tokens/variables before creating new ones
- Use `set_variables()` to define color/spacing tokens at the start
- Use `find_empty_space_on_canvas()` when adding new screens to avoid overlapping

---

## Example: Landing page mockup

```
# 1. Get design system
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "SaaS project management" --design-system

# 2. Check editor state
get_editor_state()

# 3. Get guidelines
get_guidelines(topic="landing-page")

# 4. Get style guide
get_style_guide(tags=["saas", "modern", "minimal"], name=null)

# 5. Set design tokens
set_variables([
  { "name": "primary", "value": "#6366F1" },
  { "name": "bg", "value": "#0F172A" },
  { "name": "text", "value": "#F8FAFC" }
])

# 6. Design hero section
batch_design("""
hero=I("page", { "type": "FRAME", "name": "Hero", "width": 1440, "height": 900, "fills": [{"type":"SOLID","color":"#0F172A"}] })
nav=I(hero, { "type": "FRAME", "name": "Nav", "width": 1440, "height": 72 })
h1=I(hero, { "type": "TEXT", "content": "Manage projects smarter", "fontSize": 64, "fontWeight": 800, "fills": [{"type":"SOLID","color":"#F8FAFC"}] })
sub=I(hero, { "type": "TEXT", "content": "The all-in-one workspace for modern teams.", "fontSize": 20, "fills": [{"type":"SOLID","color":"#94A3B8"}] })
cta=I(hero, { "type": "FRAME", "name": "CTA", "width": 180, "height": 52, "fills": [{"type":"SOLID","color":"#6366F1"}], "cornerRadius": 8 })
""")

# 7. Screenshot to verify
get_screenshot()
```

---

## Tips

- Start with the most important screen first (usually Hero or main dashboard)
- Use the colors from the `--design-system` output — don't invent colors
- Keep font sizes consistent: H1=56-72px, H2=36-48px, H3=24-30px, body=16-18px
- After designing, you can send to Figma with `/figma` or export to code
