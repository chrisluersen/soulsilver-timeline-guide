# SoulSilver Guide — Design System

Light-cool "SoulSilver / Lugia" theme. Extracted from `soulsilver-guide.html` (2026-08-25, restyled).

## Core tokens

```css
:root{
  --bg:#eef1f6;          /* silver-blue canvas — SoulSilver / Lugia cool */
  --bg-2:#e3e8f0;
  --surface:#ffffff;     /* cards, nav, chips */
  --surface-2:#f2f5fa;   /* elevated surfaces */
  --ink:#1d2632;         /* primary text */
  --muted:#56606d;       /* secondary text */
  --muted-2:#8791a0;     /* tertiary text */
  --line:#d8dfea;        /* hairline borders */
  --accent:#5f7fae;      /* Lugia steel-blue */
  --accent-strong:#46679b;
  --accent-ink:#ffffff;
  --danger:#c44536;
  --radius:14px;
  --shadow:0 10px 28px rgba(29,38,50,.10);
  --font-d:'Baloo 2','Space Grotesk',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  --font-b:system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif;
  --mono:ui-monospace,'Cascadia Code',Consolas,monospace;
}
```

## Type roles

| Role | Font | Size | Use |
|---|---|---|---|
| Display / hero | Baloo 2 (700) | clamp(2rem,5vw,3.2rem) | page title |
| Section heading | Baloo 2 | ~1.55rem | section anchors |
| Body | system-ui | 1rem / 1.6 | paragraphs |
| Kicker | Baloo 2 700, .78rem, uppercase, .14em | — | section eyebrows |

Baloo 2 is loaded from Google Fonts with graceful fallback to Space Grotesk/system-ui (offline-safe).

## Palette roles

- **--accent (steel-blue)** = brand moment. Used for: kickers, nav links, table headers (Serebii-style), timeline dots, card hover borders, callout left borders.
- **--fire/water/grass/elec/psych/ghost/poison/bug/fight/ice/fly** = type chips (canonical Pokémon type colors, white text on light; elec/ice keep dark text).
- **#e3350d** = Poké Ball red. Used only for: the brand Poké Ball dot and the hero watermark.

## Signature motifs

- **Poké Ball brand dot** — `.brand .dot` is a CSS-drawn Poké Ball (red top, white bottom, black band + button) via a `linear-gradient` + `::after`.
- **Hero Poké Ball watermark** — `header.hero::after` renders a 240px outline Poké Ball (steel-blue SVG data-URI) at 12% opacity, right side.
- **Serebii-style table headers** — `th` = steel-blue bg, white uppercase text; even rows get a `#f7f9fc` zebra stripe.
- **Badges (tier S/A/B)** — soft-tint chips: green/amber/blue pastel bg with dark text (light-theme versions).

## Layout decisions

- **Sticky nav** — `position:sticky;top:0`, translucent `rgba(238,241,246,.88)` + `backdrop-filter:blur(10px)`, hairline bottom border.
- **Hero** — soft blue + faint red radial glows (`.hero::before`), kicker → h1 → lede → chip spread.
- **Cards** — 14px radius, white surface, hairline border, soft shadow on hover.
- **Tables** — hairline rows, zebra stripes, steel-blue headers, `:hover` row tint.
- **Callouts** — white card with left accent border; `.callout.crit` = danger red border + `#fdf5f3` tint.
- **Responsive** — `@media (max-width:640px)` collapses grids; `prefers-reduced-motion` respected.

## Where used / source

- Source file: `C:\Users\chris\AppData\Local\hermes\wiki\plans\soulsilver-guide.html`
- Live URL: `https://soulsilver.localhost`
