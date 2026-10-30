# Build Mode: Implementing a Locked Contract

Build mode runs when the user explicitly asks for code. Treat the design contract as locked: implement its decisions directly rather than redesigning on the fly. If building exposes a practical issue with the contract (for example, a scroll sequence that conflicts with the content or a font missing required characters), flag the issue before improvising.

## 1. Tech stack

- Use the repository's existing stack. Inspect `package.json` and project files before adding dependencies.
- When starting from scratch with no stack specified, use semantic HTML, CSS, and vanilla JS. Add a framework only if requested or clearly required by the project.
- **At default `immersivity` (85+), use real scroll timeline control:** GSAP + ScrollTrigger (plus Lenis when smooth scroll fits the motion style), Framer Motion (`useScroll` / `useTransform`) in React, or native scroll-driven animations / `requestAnimationFrame` progress calculations. In vanilla builds, load GSAP/Lenis from a CDN if needed. Do not downgrade pinned scroll set pieces into simple fade-in reveals.
- When `immersivity` is below 56, avoid extra animation libraries unless already installed; use CSS transitions, `IntersectionObserver`, and `requestAnimationFrame`.

## 2. Tokens: single source of truth

- Name CSS custom properties or theme keys after **the project's domain and UI roles** (e.g., `--kiln`, `--slip`, `--glaze-celadon`, `--rule-heavy`). Avoid generic sets like `--bg/--surface/--accent`, `--paper/--ink/--rule`, or `chalk/linen/mist/oxblood` (`TOK-1` through `TOK-7`).
- Define only the variables the design actually uses.
- **Keep one source of truth.** In Tailwind projects, define colors in the Tailwind config and reference them via `theme()` or generated variables. Never duplicate `tailwind.config` color hexes into `:root` (`TOK-5`).
- Do not set a single global `--maxw: 1180px` or `1240px` across the whole site. Size containers by content type: `45–58ch` for body copy, modular widths for media grids, and natural widths for data tables (`RHY-3`).

## 3. Typography

- Use the exact font categories and roles specified in the contract. Do not swap in `Inter` or `Fraunces` out of convenience.
- Load real fonts with only the needed weights, subsets, and genuine italics. Set `font-synthesis: none` so the browser never fakes bold or italic weights.
- Define role variables (`--font-display`, `--font-body`, `--font-data`) with metric-compatible fallback stacks and deliberate `font-display` settings.
- Set `line-height` per typeface and role (tight for display headings, open for body copy, compact for UI controls) rather than a global `line-height: 1.6` on `body` (`TYP-8`).
- Use clear whole-pixel or ratio-based type scales. Avoid arbitrary half-pixel steps like `8.5px`, `9.5px`, `10.5px` (`TYP-6`).
- Respect the single-role limit for display serifs (`references/direction.md` §2.5).
- **Restrict monospace fonts to technical data:** numbers, code snippets, timestamps, and tabular specs. Do not set navigation links, section headers, captions, and eyebrows all in monospace (`CHR-1`, `CHR-2`).
- Load one or two purposeful font families rather than pulling an entire variable weight/width range unused (`TYP-2`).
- Test typography across hero headlines, body paragraphs, buttons, numerals, form inputs, and mobile viewports.
- If a specified font is unavailable, substitute a font from the **same typographic category** and note the substitution in your response.

## 4. Rhythm and layout

- Use `clamp()` with **different slopes for different roles**: compact for headers, generous for hero displays, tight for dense data rows. Avoid repeating the exact same `clamp()` padding and gap formula on every section (`RHY-1`, `RHY-2`).
- Place media-query breakpoints where the layout actually needs to adapt rather than pasting a boilerplate `960px / 768px / 600px` cascade (`BASE-5`). Use CSS container queries when a component's layout depends on its container width.
- Build the section patterns named in the contract. Include a flagged (⚑) pattern only when justified in the contract.

## 5. Edges, borders, and surfaces

- Apply the contract's **radius tiers** across component types (different radii for cards, buttons, images, inputs, and badges). Avoid both a global `* { border-radius: 0 }` reset and a universal `16px` radius (`EDGE-1`, `EDGE-2`).
- Use border widths to show hierarchy (`1px` subtle dividers, `2px` structural frames, `4px` primary anchors) rather than applying `1px solid var(--line)` everywhere (`EDGE-3`, `EDGE-4`).
- Scale shadows with elevation rather than reusing one shadow formula (`SRF-3`).
- Use at most one `backdrop-filter` surface and one surface texture where they fit the design. Do not paste the boilerplate `feTurbulence` data URI (`SRF-2`).

## 6. Hover and interaction states

- Define **two or three hover/active behaviors** suited to the project and assign them by component type (for example: underline offset on text links, crop shift on media tiles, fill change on primary buttons). Keep them consistent within each component class.
- Avoid applying a single `translateY(-4px)` lift, ink/paper inversion, left-origin `scaleX` wipe, or duplicated-span text roll across every interactive element (`HOV-1` through `HOV-5`).
- Style `:focus-visible`, `:active`, `:disabled`, and (where applicable) loading, error, and success states.

## 7. Motion implementation

Build the contract's **section beats as a coordinated timeline** rather than attaching isolated fade-in classes.

- **Normalized playhead:** drive each scroll scene from a `0..1` progress value so typography, layout shifts, and media stay synchronized.
- **Full-viewport pinned scenes:** use an outer scroll track (`200–500vh` depending on beat count) containing a `position: sticky; top: 0; min-height: 100svh` stage that progresses through distinct states (`setup -> shift -> proof -> resolve`). Keep all text accessible in the DOM.
- **Visual continuity:** carry a visual element across scene boundaries using shared coordinates, CSS custom properties, View Transitions, or matching crops.
- **Scroll reveals:** use `IntersectionObserver` selectively for supporting elements. Do not wrap every section in a single observer at `-8%` rootMargin (`MOT-4`, `MOT-7`, `MOT-8`). Render above-the-fold content immediately.
- **Depth:** drive any parallax from the scroll playhead inside `requestAnimationFrame` rather than attaching a generic `mousemove` listener to the hero (`HERO-2`).
- **Easing hierarchy** (`references/motion.md` §10): assign distinct easing curves to UI feedback, entrances, scroll-linked transforms, exits (`ease-in`), and ambient loops (`linear`). Do not route every transition through a single `cubic-bezier` variable (`MOT-2`, `MOT-3`, `MOT-9`).
- **Performance:** animate `transform` and `opacity`. Avoid animating layout properties (`width`, `height`, `top`, `left`), large `box-shadow` values, or `filter: blur()`. Ensure the initial frame renders cleanly before JS runs.

**`prefers-reduced-motion` (`BASE-3`):** handle reduced motion thoughtfully instead of nuking all CSS transitions with `* { animation: none !important; transition: none !important }`. Render reveal targets in their final visible positions, keep short opacity/color state feedback on interactive controls, and present pinned scroll scenes as stepped static frames so no content is lost.

**Mobile adaptation:**

| Desktop interaction | Mobile equivalent |
|---|---|
| Cursor-tracked highlight | Scroll-position or tap state |
| Multi-layer parallax | Reduced-distance scroll parallax |
| Long pinned scroll scene | Shorter sticky track (`150–250vh`) or stepped vertical sequence |
| Horizontal scroll section | Native swipe container or vertical stepped sequence |
| Heavy canvas / WebGL scene | Lightweight video/canvas or art-directed static frames |
| Hover-only detail | Tap toggle with visible trigger |

Never trap scroll, hide scroll progress, or require long stretches of wheel movement where nothing changes on screen.

## 8. Imagery

Every image-bearing section must have a working image `src` (`references/media.md` §5). Set explicit `width`/`height` or `aspect-ratio`, write descriptive `alt` text (`alt=""` for decorative images), apply a clean background color to the image wrapper, and set `fetchpriority="high"` on the hero image with `loading="lazy"` below the fold.

## 9. Accessibility

Use semantic landmarks (`<header>`, `<main>`, `<nav>`, `<section>`, `<footer>`), ordered heading levels, `<button>` for actions, `<a href>` for navigation, WCAG AA text contrast, visible `:focus-visible` outlines, full keyboard operability, `44x44px` minimum touch targets, labeled form fields, and a skip link (`BASE-4`).

## 10. Copy and comments

- **Never write self-justifying comments** (`META-2`, `META-3`), such as `/* NOT 3-up */`, `/* not a translateY lift */`, or `/* the one place linear easing belongs */`. Write comments only for non-obvious layout math, browser quirks, or timeline coordinates.
- Never write marketing copy claiming the site is "not a template."
- **No fake precision (`LIVE-4`):** do not invent `Math.random()` reference numbers (`HV-2841`) or fake inspection counts (`214-point check`, `42,116 KM`) unless provided by the user. Make sample data clearly readable as realistic sample content.
- **No decorative live widgets (`LIVE-1` through `LIVE-3`):** include clocks, tickers, or counters only when displaying real live data required by the brief.

## 11. Pre-delivery self-audit

1. Run `python scripts/scan.py <output-files-or-dir>`. Where code cannot run, check it by hand against `references/checklist.md` Part C and `references/tells.md`, and say that the scanner was not run.
2. Review every match: if the contract explicitly called for that pattern, keep it; if it slipped in by reflex, rework the structural slot.
3. Re-run `scripts/scan.py` (or repeat the manual check) until all remaining matches are intentional contract choices.
4. Return the code along with a 1–2 sentence note covering any implementation details decided outside the contract, any font substitutions, and any Unsplash photo IDs used outside the reference list.
