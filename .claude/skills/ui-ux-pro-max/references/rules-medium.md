# Rules: Medium Priority (P6-P9)

## P6 — Typography & Color (MEDIUM)

- `line-height` — 1.5-1.75 for body text
- `font-scale` — Consistent type scale: 12 / 14 / 16 / 18 / 24 / 32
- `weight-hierarchy` — Bold headings (600-700), Regular body (400), Medium labels (500)
- `color-semantic` — Define semantic tokens (primary, error, surface, on-surface); no raw hex in components
- `color-dark-mode` — Desaturated/lighter tonal variants; never inverted colors
- `color-accessible-pairs` — 4.5:1 AA or 7:1 AAA; verify with tooling
- `color-not-decorative-only` — Error/success color must include icon/text
- `number-tabular` — Tabular figures for data columns, prices, timers
- `whitespace-balance` — Intentional whitespace to group related items

## P7 — Animation (MEDIUM)

- `duration-timing` — 150-300ms micro-interactions; complex ≤400ms; never >500ms
- `transform-performance` — `transform`/`opacity` only; never animate width/height/top/left
- `loading-states` — Skeleton or progress when loading >300ms
- `easing` — `ease-out` entering, `ease-in` exiting; no linear for UI transitions
- `motion-meaning` — Every animation expresses cause-effect; nothing purely decorative
- `exit-faster-than-enter` — Exit ~60-70% of enter duration
- `stagger-sequence` — 30-50ms stagger per list item
- `interruptible` — Animations must be cancellable by user input
- `no-blocking-animation` — UI stays interactive during animations
- `scale-feedback` — 0.95-1.05 scale on press for tappable elements
- `navigation-direction` — Forward = left/up; back = right/down

## P8 — Forms & Feedback (MEDIUM)

- `input-labels` — Visible label per input; never placeholder-only
- `error-placement` — Error below the related field, not only at top
- `submit-feedback` — Loading → success/error state on submit
- `required-indicators` — Mark required fields (asterisk + legend)
- `empty-states` — Helpful message + action when no content
- `toast-dismiss` — Auto-dismiss toasts in 3-5s; dismissable manually
- `confirmation-dialogs` — Confirm before destructive actions
- `progressive-disclosure` — Reveal complexity progressively; don't overwhelm
- `inline-validation` — Validate on blur, not on keystroke
- `input-type-keyboard` — `type=email/tel/number` triggers correct mobile keyboard
- `disabled-states` — opacity 0.38-0.5 + cursor-not-allowed + disabled attribute

## P9 — Navigation (HIGH)

- `predictable-back` — Back always returns to previous screen
- `bottom-nav-limit` — ≤5 items in bottom nav
- `deep-linking` — All screens deep-linkable
- `active-state` — Current page/tab clearly indicated
- `breadcrumbs-depth` — Breadcrumbs for hierarchies >2 levels deep
- `no-overloaded-nav` — Max 7 items in any nav; group if more
- `search-prominent` — Search visible/accessible when content >15 items
