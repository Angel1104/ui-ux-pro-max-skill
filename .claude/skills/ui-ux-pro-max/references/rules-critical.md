# Rules: Critical (P1-P2)

## P1 — Accessibility (CRITICAL)

- `color-contrast` — Min 4.5:1 for normal text, 3:1 for large text
- `focus-states` — Visible focus rings 2-4px on all interactive elements
- `alt-text` — Descriptive alt for meaningful images, `alt=""` for decorative
- `aria-labels` — aria-label for icon-only buttons; accessibilityLabel in native
- `keyboard-nav` — Tab order matches visual order; full keyboard support
- `form-labels` — `<label for>` per input, never placeholder-only
- `skip-links` — Skip to main content for keyboard users
- `heading-hierarchy` — Sequential h1→h6, no skipped levels
- `color-not-only` — Never convey meaning by color alone; add icon/text
- `reduced-motion` — Respect `prefers-reduced-motion`
- `voiceover-sr` — Logical reading order for VoiceOver/TalkBack
- `escape-routes` — Cancel/back always available in modals and multi-step flows
- `dynamic-type` — Support system text scaling; avoid truncation as text grows

## P2 — Touch & Interaction (CRITICAL)

- `touch-target-size` — Min 44×44pt (Apple) / 48×48dp (Material)
- `touch-spacing` — Min 8px gap between touch targets
- `hover-vs-tap` — Never rely on hover alone for primary interactions
- `loading-buttons` — Disable + show spinner during async; re-enable on resolve
- `error-feedback` — Clear error message near the problem field
- `cursor-pointer` — `cursor: pointer` on all clickable elements (web)
- `tap-delay` — `touch-action: manipulation` to remove 300ms delay
- `press-feedback` — Visual feedback on press (ripple, opacity, scale)
- `haptic-feedback` — Haptic for confirmations; avoid overuse
- `safe-area-awareness` — Keep targets away from notch, Dynamic Island, gesture bar
- `no-precision-required` — No pixel-perfect taps on small/thin targets
- `gesture-alternative` — Always provide visible controls for gesture-only actions
- `standard-gestures` — Use platform-standard gestures; never redefine swipe-back
