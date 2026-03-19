# Rules: High Priority (P3-P5)

## P3 — Performance (HIGH)

- `image-optimization` — WebP/AVIF, srcset/sizes, lazy-load non-critical
- `image-dimension` — Declare width/height or aspect-ratio to prevent CLS
- `font-loading` — `font-display: swap`; preload only critical fonts
- `lazy-loading` — Dynamic import / route-level splitting for non-hero components
- `bundle-splitting` — Split by route/feature; keep initial bundle lean
- `third-party-scripts` — Load async/defer; audit and remove unnecessary
- `virtualize-lists` — Virtualize lists with 50+ items
- `main-thread-budget` — <16ms per frame for 60fps; offload heavy tasks
- `progressive-loading` — Skeleton screens for >1s operations, not spinners
- `debounce-throttle` — Debounce/throttle scroll, resize, input events
- `offline-support` — Offline state messaging + basic fallback (PWA/mobile)

## P4 — Style Selection (HIGH)

- `style-match` — Match style to product type (run `--design-system`)
- `consistency` — Same style across all pages; no mixing flat + skeuomorphic
- `no-emoji-icons` — SVG icons (Lucide, Heroicons), never emojis
- `color-palette-from-product` — Search `--domain color` for industry palette
- `effects-match-style` — Shadows, blur, radius match chosen style
- `platform-adaptive` — Respect iOS HIG vs Material; don't mix idioms
- `state-clarity` — Hover/pressed/disabled visually distinct
- `elevation-consistent` — Consistent shadow scale for cards, sheets, modals
- `dark-mode-pairing` — Design light/dark together; don't invert
- `icon-style-consistent` — One icon set, one stroke weight, one corner radius
- `primary-action` — One primary CTA per screen; secondary is visually subordinate

## P5 — Layout & Responsive (HIGH)

- `viewport-meta` — `width=device-width initial-scale=1`; never disable zoom
- `mobile-first` — Design mobile → tablet → desktop
- `breakpoint-consistency` — 375 / 768 / 1024 / 1440
- `readable-font-size` — Min 16px body on mobile (avoids iOS auto-zoom)
- `line-length-control` — 35-60 chars/line mobile; 60-75 desktop
- `horizontal-scroll` — Never on mobile; content fits viewport
- `spacing-scale` — 4pt/8dp incremental spacing system
- `container-width` — max-w-6xl / 7xl consistent desktop max-width
- `z-index-management` — Layered z-index scale: 0 / 10 / 20 / 40 / 100 / 1000
- `fixed-element-offset` — Fixed navbar/bottom bar reserves safe padding
- `viewport-units` — `min-h-dvh` over `100vh` on mobile
- `visual-hierarchy` — Size, spacing, contrast — not color alone
