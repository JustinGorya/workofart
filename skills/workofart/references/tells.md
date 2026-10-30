# Tell Index: Shared AI Layout and Styling Patterns by Slot

When given nine unrelated website briefs (a portfolio, coffee shop, gym, restaurant, charity, band, photographer, travel agency, and blog), a model generated all nine on top of the exact same structural CSS and HTML skeleton. A second independent run of nine brands produced the same result. Whenever specific patterns were forbidden in the prompt, the model substituted a new default in the exact same structural slot:

| Generation | Patterns introduced | What stayed unchanged |
|---|---|---|
| **Template** | `:root` token block, frosted glass nav, radial-gradient hero wall, `auto-fit` card grid, `translateY(-4px)` hover lift, blanket `prefers-reduced-motion` reset | Baseline layout and component slots |
| **Paper / ink** | Token names changed to `--paper/--ink/--rule`; radius changed from `16px` to `0` on `*`; frosted nav swapped for solid bar with `2–4px` ink border; radial glow swapped for fixed `feTurbulence` noise overlay; hover lift swapped for ink/paper color inversion | Every structural slot |
| **Editorial heritage** | Tailwind natural colors duplicated in `:root`; `Fraunces` with a single italic accent word; `§ I` section markers; looping marquee ticker; horizontal pin-scroll; annotated specimen diagram; left-origin `scaleX` wipes; CSS comments justifying why a rule isn't a template | Every structural slot |
| **Atelier-ledger** | `:root` block removed in favor of `tailwind.config` natural colors; width-axis grotesque (`font-stretch: 125%`); `76px` vertical rail nav; staircase-indented headlines; odometer-roll hover buttons; rolling digit columns; live `Europe/Zurich` clock; `LOT 01` ledger rows crossfading a sticky spec pane; invented provenance numbers | Every structural slot |

Negative prompts simply shift the output from one generation to the next. Audit the structural slots rather than chasing isolated rules.

**Severity ratings:** **H** = appeared in 6+ sites or defines a core layout slot | **M** = appeared in 3–5 sites | **L** = appeared in 1–2 sites as a direct replacement for a forbidden pattern. **Keep** = normal engineering hygiene to leave intact.

---

## PAL: Palette

| ID | Sev | Generation | Byte / structural pattern | Fix |
|---|---|---|---|---|
| PAL-1 | H | template | Light reflex: off-white + ink + amber/coral (`background:#f6f8fb; color:#0a0a0a; accent:#ff6b35`), often accompanied by a `/* NOT amber */` comment | Tie the accent hue to a concrete detail in the brief (`references/direction.md` §1.4) |
| PAL-2 | H | template | Dark reflex: `--void:#0a0c0e; --gold:#c8a45c` applied across unrelated restaurants, photographers, and bands | Use only for nightlife, spirits, watchmaking, fine dining, or noir themes |
| PAL-3 | H | heritage + atelier | Heritage reflex: `--bone:#E9E2D1; --racing:#1E3A2F; --brass:#A9814A`, or `chalk #ECEAE4 / linen #F5F3EE / ink #191A1C / graphite #4A4B4E / mist #7F7E78 / oxblood #6D3239 / hairline rgba(25,26,28,.16)` | Use only for actual heritage motoring, country estates, or bespoke craft |
| PAL-4 | M | template | Common startup palettes: black + neon green/cyan, navy + cyan, purple + blue, gray background + white cards, dark monochrome + one saturated accent | Use only when explicitly requested |
| PAL-5 | M | template + paper-ink | `::selection { background: var(--accent); color: var(--paper/crema/bone) }` repeated across 7–8/9 sites | Fine to include; ensure the foreground/background pair matches the project palette |

## TOK: Token layer

| ID | Sev | Generation | Byte / structural pattern | Fix |
|---|---|---|---|---|
| TOK-1 | H | template | Identical `:root { --bg; --surface; --accent; --muted; --radius; --maxw; --font-sans; --ease }` buckets in the same order | Name tokens after the project's domain and include only variables that are used |
| TOK-2 | H | template | `--accent:#8b6bff; --radius:16px; --maxw:1180px; --ease:cubic-bezier(.22,.61,.36,1)` | Replace generic token presets with project-specific role names |
| TOK-3 | H | paper-ink | `--paper:#f5f5f0; --ink:#000` (used in 8/9 sites) plus `--ink-soft/--ink-faint` | Name color variables for the specific project rather than reusing `--paper`/`--ink` |
| TOK-4 | M | paper-ink | `--rule: 2px solid var(--ink)` or `--rule: rgba(ink,.16)` used as the single border token | Use distinct border widths for hierarchy (`1px`, `2px`, `4px`) |
| TOK-5 | H | heritage | `tailwind.config` `theme.extend.colors` (`bone/racing/brass/soot/haze`) duplicated byte-for-byte into `:root` | Keep a single source of truth |
| TOK-6 | H | heritage | Five fixed natural color names (`--bone --racing --brass --soot --haze`) | Choose color roles and names based on the project |
| TOK-7 | H | atelier | `tailwind.config` only (with `:root` omitted) defining seven fixed keys: `chalk, linen, ink, graphite, mist, oxblood, hairline` | Let the number of color tokens and their names follow the actual UI |

## TYP: Typography

| ID | Sev | Generation | Byte / structural pattern | Fix |
|---|---|---|---|---|
| TYP-1 | M | template | `system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif` with no `@font-face`, or naming `Inter` without loading it | Load the actual web fonts specified in the design contract |
| TYP-2 | H | paper-ink | Repeatedly drawing from the same small Google Fonts pool: `Space Mono`, `Oswald`, `EB Garamond`, `Playfair Display`, `Cormorant` | Choose typefaces for the specific project and load only the weights used |
| TYP-3 | M | paper-ink | Single Google Fonts `css2` URL loading display + body + mono paired with a generic `ui-monospace / Helvetica Neue / Arial` fallback | Select font roles intentionally and configure metric-compatible fallbacks |
| TYP-4 | H | heritage | `family=Fraunces:ital,opsz,wght@0,9..144,300...` + `Inter` + `IBM+Plex+Mono`, `.font-display { font-optical-sizing: auto }`, and a single italic word in the hero headline | Use a high-contrast display serif only when justified by the brief (`references/direction.md` §2.5) |
| TYP-5 | H | atelier | `family=Archivo:ital,wdth,wght@0,100,410;0,125,560...&family=Fragment+Mono` with `.w-wide { font-stretch: 125% }`, `.w-norm { font-stretch: 100% }`, and `fontWeight: { w410: '410', w560: '560' }` | Use standard font weights and avoid relying on a single variable width-axis split as a formula |
| TYP-6 | M | atelier | Arbitrary half-pixel font sizes (`text-[8.5px]`, `9.5px`, `10.5px`, `11.5px`, `13.5px`, `14.5px`, `15.5px`) on monospace labels | Use a clean whole-pixel or ratio-based type scale with legible minimums |
| TYP-7 | H | heritage + atelier | **Serif dominance:** a display serif (`Fraunces`, `Playfair Display`, `Cormorant Garamond`, `EB Garamond`, `Instrument Serif`, `Libre Caslon`, `Marcellus`, `DM Serif Display`) applied to **3+ component roles** (hero, blockquote, nav wordmark, eyebrows, footer) | Restrict a display serif to a single role (headlines *or* pull-quotes), unless the site is a print publication using a text serif for body copy |
| TYP-8 | M | template + paper-ink | `body { line-height: 1.6 }` across 8/9 sites | Set `line-height` per typeface and component role |

## RHY: Rhythm, scale, and measure

| ID | Sev | Generation | Byte / structural pattern | Fix |
|---|---|---|---|---|
| RHY-1 | M | all | Uniform `clamp()` formulas: hero `clamp(2.5–3.6rem, 6–12vw, 5–9rem)`, gutters `4–5vw`, section padding `7–10vw` | Vary fluid `clamp()` slopes by section role and content density |
| RHY-2 | M | all | Repeated spacing constants across unrelated sites: `11vw`, `150px` cap, `clamp(20px,5vw,72px)`, or Tailwind `px-[clamp(1.25rem,4vw,4.5rem)]` + `py-[clamp(5rem,10vw,10rem)]` on every section | Set padding and scale per section rather than repeating one global wrapper |
| RHY-3 | M | template + paper-ink | Global `--maxw: 1140–1240px` (`1240px` in 7/9 sites), sometimes renamed `--measure`, `--sheet`, or `--app-max` | Size containers by content type (`45–58ch` for prose, modular widths for grids) |

## BASE: Base layer (baseline engineering to keep)

| ID | Sev | Generation | Byte / structural pattern | Fix |
|---|---|---|---|---|
| BASE-1 | M | all | `*,*::before,*::after { box-sizing: border-box }` + `* { margin: 0; padding: 0 }` | **Keep.** Standard CSS reset |
| BASE-2 | M | all | `html { scroll-behavior: smooth }` + `scroll-padding-top: var(--nav-h)` | **Keep.** Standard anchor behavior |
| BASE-3 | M | all | `@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; scroll-behavior: auto !important } }` | Keep the media query, but replace the blanket `*` nuke with clean static states and preserved focus/state feedback |
| BASE-4 | L | atelier | Accessibility helpers: `sr-only focus:not-sr-only` skip link, `:focus-visible` outline, `aria-live="polite"` | **Keep.** Standard accessibility engineering |
| BASE-5 | L | template | Fixed breakpoint cascade (`@960/980px -> 2 cols`, `@760–860px -> hamburger`, `@560–640px -> 1fr`) | Set breakpoints where the layout actually needs to reflow |

## SRF: Surfaces, textures, shadows, and heading effects

| ID | Sev | Generation | Byte / structural pattern | Fix |
|---|---|---|---|---|
| SRF-1 | H | paper-ink | `body::before { position: fixed; inset: 0; z-index: 9000; pointer-events: none; background-image: ...; mix-blend-mode: multiply; opacity: .3 }` | Use a texture overlay only when it directly serves the visual concept |
| SRF-2 | H | paper-ink | Inline SVG `feTurbulence type='fractalNoise' baseFrequency='0.8–0.85' numOctaves='2' stitchTiles='stitch'` data URI | Avoid pasting the boilerplate `feTurbulence` string across projects |
| SRF-3 | H | all | Three recycled shadow formulas: soft `0 20–40px 40–80px -18/-40px`, glow `0 10–12px 26–30px -10/-12px`, or hard brick `6–10px 6–10px 0` | Tune shadow elevation to the specific surface hierarchy |
| SRF-4 | M | template | `box-shadow: 0 18px 50px rgba(...)` applied to every card and button | See `SRF-3` |
| SRF-5 | M | paper-ink | `box-shadow: 10px 10px 0 var(--ink)` hard offset shadow | Use only on neo-brutalist or print-cutout designs where it fits |
| SRF-6 | M | template | `.hero-title { background: linear-gradient(...); -webkit-background-clip: text; -webkit-text-fill-color: transparent }` | Rely on typographic scale, weight, and solid color contrast |
| SRF-7 | M | paper-ink | Formulaic headline `text-shadow` (`0 0 4px` phosphor, `5px 5px 0` riso) or `-webkit-text-stroke` + `color: transparent` | Use headline effects sparingly and only when tied to the brief |

## EDGE: Border radius and borders

| ID | Sev | Generation | Byte / structural pattern | Fix |
|---|---|---|---|---|
| EDGE-1 | M | template + paper-ink | All-pill (`999px/100px/44px`) vs. all-square (`0px` + offset shadow) extremes | Use a tiered radius policy across component types |
| EDGE-2 | M | paper-ink | `* { border-radius: 0 }` placed in the universal reset | Assign radii by component role rather than locking `*` to `0` |
| EDGE-3 | M | template | `border-bottom: 1px solid var(--line)` used as the sole divider style | Vary border weights (`1px`, `2px`, `4px`) to show hierarchy |
| EDGE-4 | M | paper-ink | `2px solid var(--ink)` applied uniformly to every card and section | Mix border weights intentionally |

## NAV: Navigation layout

| ID | Sev | Generation | Byte / structural pattern | Fix |
|---|---|---|---|---|
| NAV-1 | H | template | `position: sticky; top: 0; backdrop-filter: blur(10–16px); background: rgba(...,.55); border-bottom: 1px solid transparent` | Use frosted glass only when translucency fits the surface design |
| NAV-2 | M | template | `.scrolled` / `.is-open` class toggled on `window.scrollY` to add frost | Tie header transitions to the page's layout and scroll sequence |
| NAV-3 | H | paper-ink + heritage | `.masthead { position: sticky; background: var(--paper); border-bottom: 2–4px solid var(--ink) }`, often with a "by appointment" subtitle | Choose header geometry based on link structure and page flow |
| NAV-4 | M | atelier | Fixed `writing-mode: vertical-rl` left rail (`w-[76px]`) with tracked monospace links and a live clock, collapsing into a staircase overlay menu below `lg` | Derive navigation placement from the content rather than defaulting to a `76px` vertical rail |

## HERO: Hero layout

| ID | Sev | Generation | Byte / structural pattern | Fix |
|---|---|---|---|---|
| HERO-1 | M | template | `min-height: 92–100vh` centered text over 2–3 stacked `radial-gradient(circle at 80% 20%, ...)` backgrounds + `.btn-primary`/`.btn-ghost` + `.hero-stats` | Build the hero around real photography or product UI |
| HERO-2 | M | heritage | `mousemove` listener driving `translate3d(${x*-12}px, ${y*-12}px, 0) scale(1.05)` on the hero image | Tie hero motion to scroll progress or scene state rather than a generic mouse-tilt listener |
| HERO-3 | H | atelier | `lg:w-[57%]` image / `lg:w-[56%]` text split with `block whitespace-nowrap` headline lines indented at `pl-[6vw]` / `pl-[12vw]`, repeated on menu items and process steps, with one `text-oxblood` line | Use progressive line indentation only for a single composition when justified |

## GRID: Listing and feature grids

| ID | Sev | Generation | Byte / structural pattern | Fix |
|---|---|---|---|---|
| GRID-1 | M | template | `grid-template-columns: repeat(auto-fit, minmax(240–300px, 1fr)); gap: 24–28px` | Set explicit column proportions suited to the items |
| GRID-2 | M | paper-ink | `repeat(3–4, 1fr)` grid of `border: 2px solid var(--ink)` cells | Vary cell sizes and grid proportions by content |
| GRID-3 | H | paper-ink | `repeat(6, 1fr)` bento with one `.cell--feat` spanning 3x2, paired with a `1.05–1.35fr / 1fr` split and `1.4–1.6fr 1fr 1fr` footer | Use a bento layout only when one item genuinely dominates, and customize the span layout |
| GRID-4 | H | heritage | Horizontal pin-scroll (`viewport.style.height = (innerHeight + dist) + 'px'` + `translate3d(${-p*dist}px, 0, 0)`) | Use horizontal pin-scroll only when tracking a continuous panorama or transforming subject |
| GRID-5 | H | heritage | `.specimen-frame` with `.marker[data-key]` (`i/ii/iii` pills) + `.legend-key` + `.hot` hover toggle | Include an annotated diagram only when the product has real physical or architectural parts |
| GRID-6 | H | atelier | `[data-lot]` rows (`LOT 01..04`, `P.O.R. / CHF 289,000`) crossfading stacked `[data-pane]` elements (`grid-area: 1/1; opacity: 0 -> .on`) in a sticky `aside` | Structure listings around the project's actual catalog or features |
| GRID-7 | M | heritage | `<dl><dt>Chassis</dt><dd>GT/047/IHC</dd>...</dl>` paired with a 3-stat strip | Use specification tables only for real product parameters |
| GRID-8 | M | paper-ink | `column-count: 2; column-rule: 1–2px solid` + dotted `.leader` lines + drop caps | Use multi-column text flow only where long-form reading or menus benefit from it |

## HOV: Hover states

| ID | Sev | Generation | Byte / structural pattern | Fix |
|---|---|---|---|---|
| HOV-1 | M | template | `.btn { border-radius: 999px }` + `:hover { transform: translateY(-2px to -4px) }` + `translateX` arrow shift | Define component-specific hover states |
| HOV-2 | H | paper-ink | `:hover { background: var(--ink); color: var(--paper) }` used as the sole hover effect across 7/9 sites | Differentiate hover states across links, buttons, and media cards |
| HOV-3 | H | heritage | `:hover .img { transform: scale(1.05); filter: saturate(.78) brightness(.9) }` + `scaleX` rule draw + `.meta { transform: translateX(10px) }`, often with a comment stating it is not a `translateY` lift | Keep card hover interactions focused rather than bundling four effects on every card |
| HOV-4 | M | heritage | `.link::after { transform: scaleX(0); transform-origin: left center }` + `.btn::before` `scaleX` fill on `cubic-bezier(.65,0,.35,1)` | Vary link and button hover treatments |
| HOV-5 | H | atelier | `.roll:hover .blk { transform: translateY(-100%) }` + `.blk span+span { position: absolute; top: 100% }` with every button label duplicated in the DOM (`<span>SEND REQUEST →</span><span aria-hidden="true">SEND REQUEST →</span>`) on `.42s cubic-bezier(.62,.04,.22,.96)` | Avoid duplicating button text across the DOM for global odometer hover rolls |

## MOT: Scroll reveals and easing

| ID | Sev | Generation | Byte / structural pattern | Fix |
|---|---|---|---|---|
| MOT-1 | M | template | Easing presets `cubic-bezier(0.22,1,0.36,1)`, `(.22,.61,.36,1)`, `(.2,.8,.25,1)` | See `MOT-2` |
| MOT-2 | H | all | Single soft-exit bezier (`cubic-bezier(.2,.7,.2,1)`, `(.2,.72,.2,1)`, or `(.16,.84,.3,1)`) applied to every transition on the page | Assign different easing curves to UI feedback, entrances, exits, and scroll timelines |
| MOT-3 | H | all | Complete absence of `ease-in` and `linear` outside marquee tickers | Use `ease-in` for exits and `linear` for scroll-scrubbed timelines and ambient loops |
| MOT-4 | H | template + paper-ink | `new IntersectionObserver(fn, { threshold: 0.12–0.18, rootMargin: '0px 0px -8% 0px' })` (`-8%` identical across 6/9 sites) | Render primary and above-the-fold content immediately; tie reveals to specific section beats |
| MOT-5 | H | template + paper-ink | 7-class entrance utility pack: rise `translateY(34–40px)`, slide `translateX(±30–46px)`, wipe `inset(0 100% 0 0)`, scale-blur `scale(.86–.92) blur(4–8px)`, stamp `rotate(±7deg)`, flip `rotateY(80deg)`, SVG `stroke-dashoffset` | Use 1–2 cohesive transition styles tied to the project's motion direction |
| MOT-6 | H | all | Single canned `getBoundingClientRect()` + `requestAnimationFrame` widget (SVG line draw via `getTotalLength()` or scroll-rotate badge) | Build scroll scenes that transform the actual subject matter |
| MOT-7 | M | heritage | `.reveal { transform: translateY(var(--ry,14px)); transition: opacity var(--rd,.8s) cubic-bezier(.16,1,.3,1) var(--d,0s) }` at `threshold: 0.22` | Changing the observer threshold from `0.15` to `0.22` leaves the global fade-up pattern unchanged |
| MOT-8 | M | atelier | `[data-rv]` attributes (`fade`, `mask`, `track` `letter-spacing: .14em -> .01em`, `lift` `clip-path: inset(0 0 100% 0)`) with `var(--d)` stagger at `threshold: 0.3` + `unobserve()` | Replace global `[data-rv]` observer blankets with scene-specific scroll choreography |
| MOT-9 | M | atelier | Pairing `cubic-bezier(.62,.04,.22,.96)` and `cubic-bezier(.07,.7,.09,1)` for every transition | Use a full timing hierarchy including standard `ease-out` and `ease-in` |

## CHR: Chrome and section labels

| ID | Sev | Generation | Byte / structural pattern | Fix |
|---|---|---|---|---|
| CHR-1 | M | template + paper-ink | `.eyebrow { text-transform: uppercase; letter-spacing: .2–.42em; font-size: .7–.8rem; color: var(--accent) }` or monospace `TAPE 01` / `N°1` tags above every heading | Include section labels only when they add real context |
| CHR-2 | H | paper-ink | Vertical monospace side rail (`writing-mode: vertical-rl; transform: rotate(180deg)`) + `[data-count]` numbers + rotated `-1.5deg` to `-3deg` note cards | Keep monospace type on technical/numerical data; write labels in a natural voice |
| CHR-3 | M | paper-ink | Registration ticks, coordinates, and `1px solid var(--rule)` crosshairs framing every section | Use technical coordinate chrome only on engineering, mapping, or instrument interfaces |
| CHR-4 | H | heritage | `§ I`, `§ II`, `Est. MCMLXII`, `xi·MMXXV` section markers | Use plain section titles; reserve numbering for genuinely ordered sequences |
| CHR-5 | M | atelier | Corner caption plates (`absolute bottom-5 right-5 border border-hairline bg-chalk px-4 py-3`, e.g., `"ON THE FLOOR — 19"`, `"RESTITCHED IN-HOUSE, 148 HRS"`) pinned to every photo | Add captions only where an image needs explanation |

## LIVE: Decorative "live" widgets

| ID | Sev | Generation | Byte / structural pattern | Fix |
|---|---|---|---|---|
| LIVE-1 | H | heritage | `.ticker-track { animation: ticker 46s linear infinite }` + `ticker.innerHTML += ticker.innerHTML` seam loop | Remove decorative marquee tickers unless displaying a real feed |
| LIVE-2 | H | atelier | `.odo { display: inline-flex; overflow: hidden; height: 1em }` + `.odo-col` of `<i>0..9</i>` spans at `translateY(-${digit}em)` | Use rolling digit counters only for live numerical readouts |
| LIVE-3 | H | atelier | `Intl.DateTimeFormat('en-GB', { timeZone: 'Europe/Zurich', ... })` + `setInterval(tick, 1000)` + `OPEN NOW — CLOSES 18:00 / OPENS TODAY 10:00 / BY APPOINTMENT` status dot | Include live timezone clocks and open/closed indicators only when requested by the brief |
| LIVE-4 | M | atelier | `'HV-' + (2400 + Math.floor(Math.random()*700))` fake file IDs and invented hyper-specific numbers (`42,116 KM`, `214-point inspection`, `DELIVERY N°1,406 — OBERALP PASS, 07:14`) | Never generate random reference IDs or fabricated provenance numbers |

## IMG: Imagery

| ID | Sev | Generation | Byte / structural pattern | Fix |
|---|---|---|---|---|
| IMG-1 | M | template | `.thumb-1 { background: linear-gradient(135deg, #..., #...) }` numbered placeholder divs with no real `<img>` elements | Use real, art-directed photography (`references/media.md`) |

## END: Footers and closing sections

| ID | Sev | Generation | Byte / structural pattern | Fix |
|---|---|---|---|---|
| END-1 | L | template + paper-ink | `grid-template-columns: 1.6fr 1fr 1fr [1fr]` + `.footer-bottom { border-top; display: flex; justify-content: space-between }` | Design the footer layout around the actual closing links and action |
| END-2 | L | heritage | Viewport-wide footer wordmark (`font-size: clamp(3.5rem, 17vw, 15rem)`) with an italicized ampersand | Match the footer scale and typography to the brand |
| END-3 | L | atelier | Full-bleed `min-h-[78vh]` photograph with dark bottom-to-top scrim gradient and a bottom-left quote with monospace attribution (`R. EKSTRÖM · GOTHENBURG — 964 TURBO, DELIVERED 2023`) | Include a full-bleed quote interlude only when the page narrative calls for it |
| END-4 | L | atelier | `SET IN ARCHIVO & FRAGMENT MONO` colophon beside the copyright notice | Reserve typeface colophons for type foundries, editorial publications, or personal design portfolios |

## META: Convergence and self-justifying comments

| ID | Sev | Generation | Byte / structural pattern | Fix |
|---|---|---|---|---|
| META-1 | H | paper-ink + heritage + atelier | Multiple tells from a single generation co-occurring across tokens, typography, nav, hero, grid, and hover slots | Re-derive the structural slots from the brief rather than swapping individual surface tokens |
| META-2 | H | paper-ink | Explicit negative comments (`/* NOT amber */`, `/* NOT 3-up */`, `/* NOT 50/50 */`, `/* NOT the 100px pill */`, `/* NOT off-white+ink */`) | Delete self-justifying comments and design directly from the brief |
| META-3 | M | heritage + atelier | Defensive comments explaining why a rule is allowed (`/* not a translateY lift */`, `/* the one place linear easing belongs */`, `/* reveals — four gestures, applied sparingly; the hero paints instantly */`) | Omit defensive commentary; comment only non-obvious implementation mechanics |

---

**Interpreting matches:** Matching **8 or more tells** across a codebase strongly indicates that the page shares the default AI skeleton, even if the hex colors were changed.
