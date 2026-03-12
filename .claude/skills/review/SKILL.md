---
name: review
description: "Audit UI code for accessibility, performance, and UX best practices."
trigger: "/review"
argument-hint: "[file path or component name]"
metadata:
  author: claudekit
  version: "1.0.0"
---

# Review — UI/UX Audit

Audit your UI code for accessibility, performance, and UX best practices.

<args>$ARGUMENTS</args>

## Pipeline

```
/create → /design-system → /export → /build → /review (you are here)
                                       ↑___________________________|
                                            (fix and rebuild)
```

## Workflow

### Step 1: Determine What to Review

If `$ARGUMENTS` specifies a file or component, review that. Otherwise, ask:

**Ask:** "What should I review?"
Options:
- **A specific file** — provide the file path
- **A component** — name the component to review
- **Current page** — review the most recently built page
- **Everything** — full project audit

### Step 2: Run 10-Category Audit

Check against the ui-ux-pro-max ruleset, organized by priority:

#### CRITICAL Priority

**1. Accessibility**
- [ ] Color contrast 4.5:1 minimum (large text 3:1)
- [ ] Visible focus rings on interactive elements (2-4px)
- [ ] Alt text on meaningful images
- [ ] aria-label on icon-only buttons
- [ ] Keyboard navigation (tab order matches visual order)
- [ ] Sequential heading hierarchy (h1→h6)
- [ ] Skip-to-content link
- [ ] prefers-reduced-motion respected

**2. Touch & Interaction**
- [ ] Touch targets 44x44px minimum
- [ ] 8px+ spacing between touch targets
- [ ] Click/tap for primary interactions (not hover-only)
- [ ] Loading state on async buttons
- [ ] cursor-pointer on clickable elements

#### HIGH Priority

**3. Performance**
- [ ] Images: WebP/AVIF, srcset, lazy loading below fold
- [ ] Width/height or aspect-ratio on images (prevents CLS)
- [ ] Font-display: swap
- [ ] No layout thrashing

**4. Style Consistency**
- [ ] Style matches design system (MASTER.md)
- [ ] No raw hex values (uses CSS variables/tokens)
- [ ] SVG icons (no emojis)
- [ ] Consistent shadow, radius, spacing from token scale

**5. Layout & Responsive**
- [ ] Mobile-first breakpoints
- [ ] No horizontal scroll on mobile
- [ ] Viewport meta tag present
- [ ] Min 16px body text

#### MEDIUM Priority

**6. Typography & Color**
- [ ] Line-height 1.5-1.75 for body
- [ ] 65-75 chars per line max
- [ ] Semantic color tokens used
- [ ] Dark mode variants if applicable

**7. Animation**
- [ ] Duration 150-300ms for micro-interactions
- [ ] Only transform/opacity animated (not width/height)
- [ ] Skeleton/loading states for >300ms delays

**8. Forms & Feedback**
- [ ] Visible labels (not placeholder-only)
- [ ] Error messages near related field
- [ ] Required field indicators
- [ ] Submit feedback (loading → success/error)

#### HIGH Priority

**9. Navigation**
- [ ] Predictable back behavior
- [ ] Bottom nav max 5 items (mobile)
- [ ] Active state on current nav item
- [ ] Deep linking support

#### LOW Priority

**10. Charts & Data**
- [ ] Legends visible
- [ ] Tooltips on hover/tap
- [ ] Accessible color palette
- [ ] Table alternative for screen readers

### Step 3: Generate Report

Format findings as:

```
UI/UX AUDIT REPORT
══════════════════

CRITICAL (must fix)
  ✗ [issue] — [file:line] — [how to fix]

HIGH (should fix)
  ✗ [issue] — [file:line] — [how to fix]

MEDIUM (nice to fix)
  ✗ [issue] — [file:line] — [how to fix]

PASSED ✓
  ✓ [check] — passed
  ✓ [check] — passed

Score: X/Y checks passed
```

### Step 4: Guide to Next Step

> "To fix these issues, run `/build` and describe the fixes needed. Or fix them manually and run `/review` again to verify."
