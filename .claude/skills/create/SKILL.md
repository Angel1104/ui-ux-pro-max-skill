---
name: create
description: "Start a new UI/UX project. Gathers context through questions before designing."
trigger: "/create"
argument-hint: "[brief project description]"
metadata:
  author: claudekit
  version: "1.0.0"
---

# Create — Project Intake

Start a new UI/UX project by gathering context. This is the first step in the pipeline.

<args>$ARGUMENTS</args>

## Pipeline

```
/create (you are here) → /design-system → /export → /build → /review
```

## Workflow

### Step 1: Parse Arguments

If `$ARGUMENTS` contains a project description, use it as the starting point. If empty, ask the user to describe their project idea.

### Step 2: Ask Questions (AskUserQuestion)

Gather context through conversational questions. Do NOT ask about tech stack, colors, or fonts — those belong in `/design-system` and `/export`.

**Question 1 — Project Type:**
Ask: "What are you building?"
Options:
- Landing page
- Dashboard
- SaaS application
- E-commerce store
- Portfolio
- Mobile app
- Blog / Editorial
- Admin panel

**Question 2 — Target Audience:**
Ask: "Who is this for? (industry, age group, context)"
Free text. Examples: "Young professionals in fintech", "Parents looking for childcare", "B2B enterprise buyers"

**Question 3 — Goal:**
Ask: "What's the main goal?"
Options:
- Sell a product or service
- Showcase work or portfolio
- Manage data or workflows
- Inform or educate
- Entertain or engage
- Generate leads

**Question 4 — Describe the Idea:**
Ask: "Describe your idea in as much detail as you'd like. What pages, features, or sections do you envision?"
Free text. The more detail, the better the design system will be.

**Question 5 — References & Inspiration (optional):**
Ask: "Any references or inspiration? (websites, competitors, mood/feeling)"
Free text. Optional — user can skip.

### Step 3: Validate with Search Engine

Run a quick product type search to validate the project category:

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "$PROJECT_TYPE $INDUSTRY" --domain product -n 3
```

This helps confirm the best category match and surfaces relevant design patterns.

### Step 4: Summarize & Confirm

Present a clean project brief:

```
PROJECT BRIEF
─────────────
Project:    [name or description]
Type:       [landing page / SaaS / etc.]
Audience:   [target audience]
Goal:       [primary goal]
Details:    [key features and pages]
References: [inspiration if provided]
```

Ask: "Does this look right? Anything to add or change?"

### Step 5: Guide to Next Step

Once confirmed, tell the user:

> "Project brief captured! Now run `/design-system` to create your complete design system — colors, typography, components, and tokens based on this brief."
