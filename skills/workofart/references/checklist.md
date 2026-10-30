# Quality Checklist

Verify the applicable section before returning any output: **Part A** for design contracts, **Part B** for code builds, and **Part C** for stylesheet/markup audits. Fix any unchecked item before responding.

---

## A. Design contract (`Direct` mode)

**Briefing and levers**
- [ ] Every lever score has a one-line reason tied to a concrete detail in the brief.
- [ ] The posture is stated: **cinematic (default)**, or stepped down with the user's exact words quoted.
- [ ] If the user did not ask for a calm or minimal style, `creativity` is `>= 75`, `layout_structure` is `>= 75`, and `immersivity` is `>= 85`. Industry category, B2B context, or a short prompt did not lower any lever.
- [ ] If the user asked to tone down a specific dimension, only that lever was lowered.
- [ ] All six areas are defined: palette, typography, edge policy, layout, motion (when `immersivity >= 41`), and media.
- [ ] The direction has a specific 2–4 word name tailored to the brief (or a style name from `references/direction.md` §5 that directly fits).
- [ ] Any existing brand assets provided by the user (logo, palette, fonts) are preserved.
- [ ] Accessibility considerations are noted where relevant (low contrast, glassmorphism, neumorphism, heavy motion, overlapping layouts).
- [ ] No implementation code is included (unless `Build` mode was requested).
- [ ] The response ends with the checkpoint question.

**Palette**
- [ ] The palette has a descriptive name (e.g., *"harbour slate, buoy orange, and wet bone"*).
- [ ] The accent hue is tied to a concrete detail in the brief (*"accent is [hue] because [brief signal]"*).
- [ ] Does not use `PAL-1` (off-white + ink + amber/coral) unless the brief involves heat, fire, citrus, autumn, sports, or a brand requirement.
- [ ] Does not use `PAL-2` (black + gold) unless the brief involves nightlife, spirits, watchmaking, fine dining, or noir themes.
- [ ] Does not use `PAL-3` (bone/racing-green/brass or chalk/ink/oxblood) unless the brief is actual heritage motoring, a country estate, or bespoke craft.
- [ ] Does not use `PAL-4` startup tropes unless requested.
- [ ] Does not reuse the same palette family or accent color as an earlier unrelated brief in the same session.
- [ ] Meets WCAG AA contrast requirements.

**Typography**
- [ ] Font categories are justified by task, audience, tone, density, script, or brand guidelines (not vague words like "premium", "modern", or "clean").
- [ ] Two alternative font categories were considered and ruled out.
- [ ] Does not default to a high-contrast serif + neutral sans + single italic hero word (`TYP-4`) without a concrete publishing, fashion, cultural, or heritage signal.
- [ ] Display serif is limited to **at most one role** (headlines *or* pull-quotes), unless the brand is a print publication using a text serif for body copy (`TYP-7`).
- [ ] Italics have a clear semantic role (titles, quotes, live readings, foreign terms) rather than decorative emphasis on a random headline word.
- [ ] Uppercase, letter-spacing, weight, and width each serve a clear hierarchy role.
- [ ] Uses at most 2–3 font families that remain legible across body text, UI labels, numerals, forms, and mobile screens.

**Edges and border radius**
- [ ] Specifies a radius policy (`sharp`, `small`, `mixed`, `large`, `asymmetric`, or `chamfered`) and maps tiers to specific components.
- [ ] Cards, buttons, images, inputs, and badges do not all share a single global border radius (`EDGE-1`, `EDGE-2`).
- [ ] Large radii (`16px+`, `rounded-2xl/3xl`, pill cards) are used only when the brief calls for softness, wellness, playfulness, or consumer mobile UI.
- [ ] Professional, B2B, fintech, technical, and editorial briefs default to `0–6px` structural radii.
- [ ] Avoids both all-pill and global `* { border-radius: 0 }` extremes.

**Layout** (`layout_structure >= 25`)
- [ ] Hero uses a named pattern combined with overlap, full-bleed imagery, offset alignment, depth, or scale contrast.
- [ ] Hero is not a plain 50/50 centered text-left / image-right split or a centered text wall over 3 equal cards.
- [ ] Features are not a uniform 3-up row, 4-up row, or 2x3 grid of identical cards.
- [ ] Contact section is not a symmetric left-info / right-form split.
- [ ] Pricing is not three identical vertical cards with the middle card highlighted.
- [ ] Testimonials and logos are not uniform 3-up or 6-up grids.
- [ ] Adjacent sections do not repeat the same layout skeleton.
- [ ] At `>= 41`: FAQ is not a bare centered accordion stack, and the footer is not 4 equal link columns (`END-1`).
- [ ] Every flagged (⚑) pattern has a direct content reason, and multiple ⚑ patterns are not stacked on the same page without cause.

**Media**
- [ ] Marketing, brand, editorial, and product pages use real photography unless exempted by `references/media.md` §3.
- [ ] Every image-bearing section specifies **subject + mood + crop**.
- [ ] Does not fall back to gray placeholder boxes, CSS gradients (`IMG-1`), or abstract SVG blobs.

**Motion and sequence** (`immersivity >= 41`)
- [ ] Commits to a named motion direction and feel.
- [ ] Defines a clear narrative sequence from opening premise to final CTA.
- [ ] At `>= 56`: maps each section as `beat -> visible change -> handoff`, includes exit transitions on 2+ sections, and places a quiet hold after dense motion sequences.
- [ ] At `>= 71`: includes at least one `~100svh` pinned scroll scene that transforms a central subject (not a horizontal card gallery).
- [ ] At `>= 86` (default): includes a staged opening (`~2s`), **2+ full-viewport pinned scroll scenes** with distinct purposes, and a persistent subject that changes state across acts.
- [ ] Ambient effects (grain, shaders, particles) have a clear atmospheric role and do not replace scroll progression.
- [ ] Includes a complete `prefers-reduced-motion` stepped or static fallback.
- [ ] Avoids dead scroll, scroll hijacking traps, and hidden navigation.

---

## B. Build mode

- [ ] Implements the locked contract faithfully, noting any necessary adjustments.
- [ ] Keeps color tokens in a single source of truth named for the project; no `tailwind.config` to `:root` duplication (`TOK-5`).
- [ ] Loads real web fonts with only the used weights and genuine italics (`font-synthesis: none`), plus metric-compatible fallbacks.
- [ ] Sets `line-height` per typeface (`TYP-8`), uses a whole-step or ratio type scale without half-pixel steps (`TYP-6`), and keeps monospace type on technical/numerical data (`CHR-2`).
- [ ] Varies `clamp()` slopes and container widths by section role (`RHY-1` through `RHY-3`); sets breakpoints where the content needs to reflow (`BASE-5`).
- [ ] Applies tiered border radii and border widths (`EDGE-1` through `EDGE-4`); uses at most one blur surface and one texture overlay (`SRF-1`, `SRF-2`, `NAV-1`).
- [ ] Assigns 2–3 distinct hover behaviors by component class (`HOV-1` through `HOV-5`) and styles `:focus-visible` on all interactive controls.
- [ ] At default `immersivity` (85+), implements the contract's pinned scroll scenes with a normalized `0..1` scroll playhead rather than simple fade-in classes.
- [ ] Uses a differentiated easing hierarchy (`MOT-2`, `MOT-3`, `MOT-9`) and animates only `transform` and `opacity`.
- [ ] Provides a clean `prefers-reduced-motion` layout (`BASE-3`) and responsive mobile adaptations.
- [ ] Loads working photography URLs in every image-bearing section with `aspect-ratio`, descriptive `alt` text, and solid wrapper backgrounds.
- [ ] Meets WCAG AA contrast, semantic landmark rules, keyboard navigation parity, `44x44px` touch targets, labeled form fields, and skip-link standards (`BASE-4`).
- [ ] Contains zero self-justifying `/* NOT X */` comments (`META-2`, `META-3`), zero fake random reference numbers (`LIVE-4`), and zero decorative clocks/tickers (`LIVE-1` through `LIVE-3`).
- [ ] `python scripts/scan.py` was run on the output (or, where code cannot run, Part C was checked by hand and the user was told) and all remaining matches are verified as intentional contract decisions.

---

## C. 27-point stylesheet and markup audit check

Each "yes" below is a candidate AI tell. Matching 8 or more across a site indicates the shared AI skeleton:

1. Are variables named `--bg/--surface/--accent` (`TOK-1`) or `--paper/--ink/--rule` (`TOK-3`)?
2. Is the accent color the default amber-on-cream (`PAL-1`) or black-and-gold (`PAL-2`) without a direct brief reason?
3. Is the navigation a sticky `backdrop-filter: blur(10–16px)` bar with `.scrolled` (`NAV-1`, `NAV-2`), or a sticky bar with a `2–4px solid` ink border (`NAV-3`)?
4. Is the hero a `92–100vh` centered text wall over stacked `radial-gradient` backgrounds (`HERO-1`), or a flat paper background under a fixed `feTurbulence` noise overlay (`SRF-1`, `SRF-2`)?
5. Is the main grid `repeat(auto-fit, minmax(240–300px, 1fr))` (`GRID-1`), `repeat(3–4, 1fr)` bordered cells (`GRID-2`), or `repeat(6, 1fr)` with a single `span 3` bento cell (`GRID-3`)?
6. Does every interactive element use the same hover effect (`translateY(-4px)` lift `HOV-1` or ink/paper swap `HOV-2`)?
7. Do all shadows come from one of the three stock formulas (`SRF-3` through `SRF-5`)?
8. Does every section use the same `clamp(3–4rem, 8–9vw, 6–8rem)` padding and `1.6` body line-height (`RHY-1`, `RHY-2`, `TYP-8`)?
9. Are there any `/* NOT X */` comments in CSS, HTML, or JS (`META-2`)?
10. Does a single `IntersectionObserver` with `rootMargin: '0px 0px -8% 0px'` fade in every section (`MOT-4`)?
11. Are `tailwind.config` color hexes duplicated inside `:root` (`TOK-5`)?
12. Are sections labeled with `§ I`, `§ II`, or `Est. MCMLXII` (`CHR-4`)?
13. Is `Fraunces` with `font-optical-sizing: auto` and one italicized headline word used as the hero font (`TYP-4`)?
14. Was `Fraunces` swapped for `Playfair Display`, `Cormorant`, `EB Garamond`, or `Instrument Serif` in the exact same formula (`TYP-7`)?
15. Is a display serif applied to three or more component roles across the page (`TYP-7`)?
16. Is there a looping `.ticker-track { animation: ticker 46s linear infinite }` duplicated via `innerHTML +=` (`LIVE-1`)?
17. Is there a horizontal pin-scroll section driven by `innerHeight + dist` and `translate3d(-p*dist, 0, 0)` (`GRID-4`)?
18. Are there defensive comments explaining why a CSS rule is acceptable (`/* not a translateY lift */`, `/* the one place linear easing belongs */`) (`META-3`)?
19. Were `:root` variables removed in favor of seven fixed natural color keys (`chalk, linen, ink, graphite, mist, oxblood, hairline`) in `tailwind.config` (`TOK-7`)?
20. Does the typography split a single variable grotesque across `font-stretch: 125%` and `100%` with custom `410`/`560` weights (`TYP-5`)?
21. Do buttons duplicate their label text in two stacked `<span>` elements for an odometer hover roll (`HOV-5`)?
22. Does the page include decorative `.odo` digit columns, a live `Intl.DateTimeFormat` clock (`Europe/Zurich`), or `Math.random()` reference numbers (`LIVE-2` through `LIVE-4`)?
23. Are the hero headline, overlay menu, blockquote, and process steps all staircase-indented (`pl-[6vw]`, `pl-[12vw]`) with one accent-colored line (`HERO-3`)?
24. Is the feature or inventory section built as `LOT 01..04` rows crossfading `[data-pane]` views in a sticky sidebar (`GRID-6`)?
25. Does the stylesheet use a half-pixel font-size scale (`text-[8.5px]`, `9.5px`, `10.5px`) on tracked uppercase monospace labels (`TYP-6`)?
26. Does sample copy invent hyper-specific numbers (`42,116 KM`, `214-point inspection`, `DELIVERY N°1,406`) (`LIVE-4`)?
27. Are bordered caption plates pinned to the corners of photos (`CHR-5`), followed by a full-bleed quote interlude (`END-3`) and a `SET IN X & Y` colophon (`END-4`)?
