---
name: help
description: "Help guide for UI/UX Pro Max. Shows all commands and how to use them."
trigger: "/help, how do I use this, what can you do, what skills are available, getting started, ayuda, como usar"
argument-hint: "[topic]"
---

# UI/UX Pro Max — Help Guide

## What is this?

An AI design intelligence toolkit with 161 product types, 67 styles, 161 color palettes, 57 font pairings, 99 UX guidelines, and 25 chart types. Everything is command-driven — you control each step.

---

## The Pipeline

Every project follows this flow. Each step is a `/command` that asks you questions and guides you to the next.

```
/create  →  /design-system  →  /export  →  /build  →  /review
  (1)           (2)              (3)         (4)         (5)
 context     colors, fonts    code/figma   pages &     audit
 & goals     components       /pencil     components
              tokens
```

| Step | Command | What it does | Frequency |
|------|---------|-------------|-----------|
| 1 | `/create` | Gathers project context — what, who, why | Once |
| 2 | `/design-system` | Creates complete design system — style, colors, fonts, components | Once |
| 3 | `/export` | Exports to Code, Figma, or Pencil | Once per target |
| 4 | `/build` | Builds pages, sections, components using your design system | Repeat |
| 5 | `/review` | Audits for accessibility, performance, UX issues | Repeat |

---

## Quick Start

### Small project (landing page, portfolio)

```
/create "landing page for a yoga studio"
```
Answer the questions, then:
```
/design-system
```
Pick your colors, fonts, components, then:
```
/export code
```
Choose your stack, then:
```
/build "homepage with hero, features, testimonials, and CTA"
```

### Large project (SaaS, dashboard, e-commerce)

Same flow, but `/build` multiple times:

```
/create "project management SaaS for remote teams"
/design-system
/export code        → sets up tokens + base components
/build "dashboard page with KPIs and project list"
/build "settings page with profile and team management"
/build "notification dropdown component"
/review
```

### Design-first (Figma or Pencil)

```
/create "fintech mobile app"
/design-system
/export figma       → pushes design system to Figma
/build "onboarding flow"
```

---

## All Commands

### Main Pipeline

| Command | Purpose |
|---------|---------|
| `/create` | Start a new project. Asks about type, audience, goals, and idea. |
| `/design-system` | Generate complete design system. Asks about style, colors, fonts, and which components to include. |
| `/export` | Export design system to Code (any stack), Figma, or Pencil. |
| `/build` | Build a page, section, or component using your design system. Repeatable. |
| `/review` | Audit UI for accessibility, performance, and best practices. |

### Design Assets

| Command | Purpose |
|---------|---------|
| `/design` | Router for: logo, CIP (corporate identity), icon, social photos. |
| `/banner` | Design banners for social media, ads, web heroes, print. |
| `/slides` | Create HTML presentations with Chart.js. |

### Brand & Styling

| Command | Purpose |
|---------|---------|
| `/brand` | Brand voice, visual identity, messaging frameworks. |
| `/styling` | shadcn/ui components, Tailwind patterns, dark mode. |

### Export Tools

| Command | Purpose |
|---------|---------|
| `/figma` | Push designs to Figma Desktop via figma-bridge MCP. |
| `/pencil` | Create visual mockups in .pen files. |

### Help

| Command | Purpose |
|---------|---------|
| `/help` | This guide. |

---

## Supported Projects

Landing pages, SaaS apps, dashboards, admin panels, e-commerce stores, portfolios, mobile apps, blogs, and design systems.

## Supported Stacks

HTML+Tailwind (default), React, Next.js, Vue/Nuxt, Svelte, shadcn/ui, SwiftUI, React Native, Flutter, Jetpack Compose.

---

## Built-in Quality

Every `/build` and `/review` enforces:

| Priority | Rules |
|----------|-------|
| CRITICAL | Contrast 4.5:1, focus rings, aria-labels, keyboard nav, 44px touch targets |
| HIGH | Mobile-first, SVG icons, consistent style, no horizontal scroll |
| MEDIUM | 150-300ms transitions, visible form labels, semantic color tokens |

---

## Example Conversation

```
You:    /create "e-commerce store for handmade ceramics"
Claude: What are you building? → E-commerce store
        Who is this for? → "Women 25-45, artisan craft lovers"
        What's the goal? → Sell products
        Describe the idea → "Homepage, product catalog, product detail, cart, checkout"
        Any references? → "Similar to Etsy but more minimal"
        ✓ Brief captured! Now run /design-system

You:    /design-system
Claude: Style: Minimalism with warm organic feel. Works?
        Colors: #8B7355 primary, #F5F0EB background... Adjust?
        Fonts: Playfair Display + Source Sans Pro. Alternatives?
        Components: nav, hero, product-card, cart-item, button, input, modal, badge, filter. Add/remove?
        ✓ Design system ready! Run /export

You:    /export code
Claude: Stack? → Next.js
        ✓ Generated: design-tokens.css, tailwind.config.ts, base components
        Run /build to start creating pages

You:    /build "homepage with hero and featured products grid"
Claude: [builds the page using design system]
        ✓ Done! /build again or /review to audit
```
