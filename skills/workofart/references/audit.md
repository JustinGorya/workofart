# Audit Mode: Detection Workflow

An audit answers one question: **does this codebase share the default AI layout and styling skeleton, or was its structure designed for its content?** Changing hex codes from `#c6ff00` to `#c8a45c` does not change the underlying structure. Evaluate structural slots, not surface colors.

Audit outputs a **verdict and a `file:line` fix list**. Do not rewrite files until the user asks.

## 0. Gather the files

- **Local files:** run `python scripts/scan.py <path>` across `.css`, `.scss`, `.html`, `.js/.ts`, `.jsx/.tsx`, `.vue`, `.svelte`, and `.astro` files.
- **Live URL:** download the HTML, linked stylesheets, and scripts into a temporary folder and run the scanner on that directory. Treat downloaded files as static data and do not execute untrusted scripts. If you cannot fetch the URL, ask the user to paste or attach the HTML and stylesheets.
- **Pasted code:** inspect it directly, or save it to a scratch file and run `scripts/scan.py`. Cite line numbers within the snippet in place of `file:line`.
- **Where code cannot run:** read the files directly, use the patterns in §3 as search terms, and work through `references/checklist.md` Part C. Say that the scanner was not run.

`scripts/scan.py` reports **candidate matches** with `file:line` locations and tell IDs. Because regex matches bytes rather than context, inspect each hit in the source file and also check structural patterns that regex cannot catch (such as serif role count, adjacent sections repeating the same layout, or missing scroll continuity).

**Check markup and JS alongside CSS.** Newer generated pages (especially the `atelier-ledger` pattern) often omit `:root` blocks entirely, placing color tokens inside an inline `tailwind.config` script, arbitrary Tailwind classes (`w-[76px]`, `text-[9.5px]`), and small inline `<script>` blocks. Inspect `class` attributes, Tailwind config objects, and scripts just as closely as stylesheets.

## 1. Inspect in structural order

1. **Tokens:** Check variable names and roles: `--bg/--surface/--accent/--radius:16px` (`template`), `--paper/--ink/--rule` (`paper/ink`), natural color names duplicated between `tailwind.config` and `:root` (`editorial heritage`), or seven fixed natural color buckets in `tailwind.config` (`atelier-ledger`). Check for `--ease: cubic-bezier(.2,.7,...)` and `--maxw: 1140px–1240px`.
2. **Reset:** Standard `*,*::before,*::after { box-sizing: border-box }` and `* { margin: 0 }` are normal engineering (keep them), but check if `border-radius: 0` was put on the universal `*` selector (`paper/ink`).
3. **Body:** Universal `line-height: 1.6`, `overflow-x: hidden`, and `html { scroll-behavior: smooth }`. Check whether the page uses a bare system font stack without `@font-face`, the `Fraunces` + `Inter` + `IBM Plex Mono` trio (`editorial heritage`), or `Archivo` with non-standard `410` / `560` weights (`atelier-ledger`).
4. **Surface textures:** Fixed full-screen `body::before` overlays with inline SVG `feTurbulence` (`baseFrequency='0.8'`, `numOctaves='2'`). In `editorial heritage` and `atelier-ledger`, check if the background texture slot was swapped for a looping marquee ticker or mousemove hero parallax.
5. **Navigation:** Frosted glass (`backdrop-filter: blur(10–16px)` + `.scrolled` toggle), sticky bar with a `2–4px` solid ink bottom border, "by appointment" masthead, or a `76px` `writing-mode: vertical-rl` left rail with a full-screen overlay menu.
6. **Hero:** `92–100vh` centered text over stacked radial gradients with two pill buttons and gradient-clipped stat numbers (`template`); flat paper background with noise overlay (`paper/ink`); mousemove-parallax image with a `Fraunces` headline containing one italic word (`editorial heritage`); or a 57%/56% split with staircase-indented uppercase lines at `clamp(2.9rem,7vw,6.9rem)`, one oxblood line, and a corner caption plate (`atelier-ledger`).
7. **Grids:** `repeat(auto-fit, minmax(240–300px, 1fr))` (`template`); `repeat(3–4, 1fr)` with `2px solid` borders (`paper/ink`); `repeat(6, 1fr)` bento with one spanned cell (`paper/ink`); horizontal pin-scroll + annotated specimen + `<dl>` spec table (`editorial heritage`); or `lg:grid-cols-12` with `col-start` staircases and `LOT 01..04` rows crossfading a sticky spec pane (`atelier-ledger`). Check for `1.6fr 1fr 1fr` footers.
8. **Hover states:** Global `translateY(-4px)` + shadow (`template`); ink/paper color inversion (`paper/ink`); left-origin `scaleX` underline wipes + 4-part card hover (`editorial heritage`); or duplicated `<span>` odometer text rolls on `cubic-bezier(.62,.04,.22,.96)` (`atelier-ledger`).
9. **Headings, labels, and serif usage:** Gradient-clipped hero titles (`template`); `text-shadow` or `-webkit-text-stroke` (`paper/ink`); uppercase `.eyebrow` labels at `.2–.42em` tracking; monospace `TAPE 01` / `N°1` tags; `§ I` and `Est. MCMLXII` markers (`editorial heritage`); or half-pixel monospace plates (`text-[8.5px]` to `text-[10.5px]`) paired with `font-stretch: 125%` headings (`atelier-ledger`). **Count how many component roles use a serif font:** three or more roles is `TYP-7`.
10. **Comments, reveal observers, and runtime scripts:** Check for `/* NOT` comments (`META-2`) and self-justifying comments (`META-3`). Check whether `prefers-reduced-motion` nukes all transitions with `* { animation: none !important }`. In JS, look for `IntersectionObserver` with `rootMargin: '0px 0px -8% 0px'` or thresholds `0.22` / `0.3`, `ticker.innerHTML += ticker.innerHTML`, `Intl.DateTimeFormat` + `setInterval(..., 1000)` live clocks, and `Math.random()` reference numbers.

Finally, step back to evaluate the page flow: do adjacent sections repeat the same layout? Does the page follow `nav -> hero -> about -> 3-up cards -> CTA -> footer` regardless of content? Are the images real photographs?

## 2. Generation signatures

| Generation | Characteristic combination of tells |
|---|---|
| **Template** | `--bg/--surface/--accent`, `--radius: 16px`, frosted glass nav + `.scrolled`, radial-gradient hero wall, `auto-fit` card grid, pill buttons + `translateY` hover, gradient text, CSS gradient thumbnails, `-8%` observer |
| **Paper / ink** | `--paper/--ink/--rule`, `* { border-radius: 0 }`, sticky bar with `2–4px` ink border, fixed `feTurbulence` noise overlay, bordered cell grid or 6-col bento, ink/paper hover swap, hard offset brick shadow, `Space Mono` / `Oswald`, `/* NOT X */` comments |
| **Editorial heritage** | Tailwind colors duplicated in `:root`, `Fraunces` + single italic accent word, `§ I` section markers, looping marquee ticker, horizontal pin-scroll, annotated specimen markers, `<dl>` spec table, left-origin `scaleX` wipes, mousemove hero parallax, self-justifying CSS comments |
| **Atelier-ledger** | `tailwind.config`-only natural colors (`chalk`/`ink`/`oxblood`/`hairline`), width-axis grotesque with `410`/`560` weights, `76px` vertical rail nav, staircase-indented headline, odometer-roll buttons, rolling digit columns, live timezone clock, `LOT` ledger + sticky spec pane, half-pixel monospace sizes, random reference IDs, photo caption plates, full-bleed quote interlude, `SET IN X & Y` colophon |

Sites often mix two generations (for example, `paper-ink + atelier-ledger`). Name whichever generations match.

## 3. Manual grep patterns

Run these from a shell, or use them as search patterns when reading files directly.

```bash
# tokens & palette
grep -nE -- '--(bg|surface|accent|muted|radius|maxw|paper|ink|rule|bone|racing|brass|soot|haze)\b' -r .
grep -nE 'theme\s*:\s*\{|extend\s*:\s*\{|colors\s*:' -r .
# typography
grep -nE 'fonts\.googleapis|Fraunces|Playfair|Cormorant|EB\+?\s?Garamond|Instrument\+?\s?Serif|Space\+?\s?Mono|Oswald|Archivo|Fragment\+?\s?Mono|font-stretch|font-optical-sizing' -r .
# easing & scroll observers
grep -nE 'cubic-bezier\(\s*\.2\s*,\s*\.7|cubic-bezier\(\.62,\.04|cubic-bezier\(\.07,\.7|IntersectionObserver|rootMargin|threshold' -r .
# surfaces, nav, hover
grep -nE 'feTurbulence|backdrop-filter|background-clip:\s*text|translateY\(-[0-9]|scaleX\(0\)|writing-mode:\s*vertical' -r .
# decorative runtime widgets & self-justifying comments
grep -nE 'Intl\.DateTimeFormat|setInterval|Math\.random|innerHTML\s*\+=|style\.transform|/\*\s*(NOT|not a)' -r .
# atelier-ledger Tailwind classes and data attributes
grep -nE 'px-\[clamp\(|py-\[clamp\(|pl-\[[0-9.]+vw\]|text-\[[0-9]+\.5px\]|tracking-\[\.[0-9]+em\]|w-\[76px\]|data-(rv|lot|pane|clock)' -r .
```

## 4. Report format

```markdown
**Verdict:** carries the shared skeleton ([generation(s)]) | [N] tells matched ([H] high severity)
   or
**Verdict:** does not carry the shared skeleton ([one-sentence reason why the structure reads as custom-designed])

**Slot fixes** (structural changes, ordered by severity)
1. NAV-3 (navigation): found `border-bottom: 3px solid var(--ink)` on sticky `.masthead` (`site.css:42`) -> redesign navigation layout around the site's actual content: [concrete recommendation].
2. ...

**Surface fixes**
- ...

**Keep**: box-sizing reset, considered `prefers-reduced-motion` handling, fluid `clamp()` typography, `:focus-visible` states.

Would you like me to apply these slot fixes, or establish a new design contract first?
```

**Guidelines for the fix list:**
- Cite the exact code matched and its `file:line` location.
- Propose fixes that change how the structural slot works rather than swapping one default token or font for another.
- If the codebase never had a brief-specific direction to begin with, recommend running **Direct** mode to establish a design contract before editing CSS.
- Matching **8 or more tells** (or hitting multiple high-severity slots across tokens, nav, hero, grid, hover, and reveals) confirms the shared skeleton is present.
- Never flag baseline engineering (`BASE-1`, `BASE-2`, `BASE-4`) as errors; list them under **Keep**.
