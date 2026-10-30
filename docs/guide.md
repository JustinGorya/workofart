# Design, build, and audit

[Back to the README](../README.md). Scanner commands below run from the repository root.

## The problem

When we gave a model nine unrelated briefs (a portfolio, a coffee shop, a gym, a restaurant, a charity, a band, a photographer, a travel agency, and a blog), all nine came back with the same underlying code: the same `:root` token block, frosted glass nav, radial-gradient hero, `auto-fit` card grid, `translateY(-4px)` hover lift, and blanket `prefers-reduced-motion` reset. A second independent run of nine brands produced the same structure.

Telling the model what to avoid did not fix the convergence. Whenever a specific pattern was banned, the model replaced it with a new default in the exact same structural slot. Across four iterations, the outputs clustered into four recognizable styles documented in [`references/tells.md`](../skills/workofart/references/tells.md):

| Generation | Typical patterns | What stayed the same |
|---|---|---|
| **Template** | `:root` token block, frosted glass nav, radial hero background, `auto-fit` card grid, `translateY(-4px)` hover | Baseline layout and component structure |
| **Paper / ink** | `--paper` and `--ink` variables, `border-radius: 0` reset, fixed `feTurbulence` noise overlay, inverted hover states | Every structural slot |
| **Editorial heritage** | `Fraunces` with a single italic accent word, `§ I` section markers, looping marquee ticker, horizontal pin-scroll, CSS comments justifying why a rule isn't a template | Every structural slot |
| **Atelier ledger** | Width-axis grotesque (`font-stretch: 125%`), vertical left rail nav, staircase-indented headlines, odometer hover rolls, live timezone clock, `LOT 01` spec tables | Every structural slot |

Negative prompts only trigger the next costume. `workofart` fixes this by making the AI tie every layout and styling slot to a concrete detail in the brief before writing code, then auditing the resulting structure.

## Modes

| Mode | Trigger | Output | Follow-up |
|---|---|---|---|
| **Direct** (default) | Design questions: direction, palette, typography, layout, motion | A [design contract](#example-design-contract) where every choice points to a detail in the brief | Stops and asks whether to adjust the direction or build it |
| **Build** | `"build it"`, `"implement"`, `"code it"` | Production code implementing the locked contract | Runs `scripts/scan.py` on its own output before returning, or checks the tell index by hand where code cannot run |
| **Audit** | `"does this look AI-generated?"`, `"audit ./site"`, or sharing CSS/HTML to review | A [report](#example-audit-output) naming the matched generation, tell count, and `file:line` fixes | Waits for confirmation before rewriting files |

### Prompt examples

- `"Give me a design direction for a ceramics studio landing page"` -> runs **Direct** mode and returns a design contract without writing code.
- `"Make the palette warmer and tighten the hero layout"` -> updates the contract in **Direct** mode.
- `"Build it"` -> switches to **Build** mode, writes the frontend, and checks it with the scanner (or by hand where code cannot run).
- `"Audit ./src for AI tells"` or a pasted stylesheet -> runs **Audit** mode and returns `file:line` findings.

## Three calibration levers

Every design contract scores three independent 1–100 parameters based on the brief:

- **`creativity`**: palette, typography character, surface treatments, and edges.
- **`layout_structure`**: grid construction, asymmetry, overlap, and section pacing.
- **`immersivity`**: scroll choreography, scene transitions, and motion.

| Band | Label | Behavior |
|---|---|---|
| 1–20 | Conventional | Standard utility layouts. Used only when requested. |
| 21–40 | Polished | Familiar page structure with one distinct layout change per section. Used on request. |
| 41–60 | Distinct | Custom palette, named section patterns, and guided scroll progression. Used on request. |
| 61–80 | Bold | Overlapping layers, full-bleed imagery, strong scale contrast, and scene-based motion. |
| 81–100 | Avant-garde | Full-viewport scroll scenes and choreographed transitions. |

### Default posture and stepping down

Unless you ask for a restrained or traditional layout, `workofart` defaults to high values (`creativity` 75–90, `layout_structure` 75–92, `immersivity` 85–98): a staged opening, two or more full-viewport scroll scenes, a visual subject that changes state as you scroll, and custom section layouts. The subject matter determines the style of motion (for example, crisp UI assembly for a developer tool vs. slow lighting transitions for hospitality), not how much care goes into the layout.

To dial it back, state what you want simplified:
- Words like *"calm"*, *"classic"*, or *"minimal"* lower all three levers.
- *"No animation"* or *"static"* lowers only `immersivity`.
- *"Standard layout"* lowers only `layout_structure`.

Full rules are in [`references/levers.md`](../skills/workofart/references/levers.md).

## The 17 slot families

[`references/tells.md`](../skills/workofart/references/tells.md) tracks 85 specific byte patterns grouped into 17 structural slots, each rated by severity (`H`, `M`, `L`) with a concrete fix:

| Prefix | Slot | What it checks |
|---|---|---|
| `PAL` | Palette | Whether the color scheme comes from the subject matter rather than default amber-on-cream, black-and-gold, or racing-green palettes |
| `TOK` | Token layer | Single source of truth for variables, named for the project rather than `--bg`/`--surface` or `--paper`/`--ink` |
| `TYP` | Typography | Font choices tied to use case and script, avoiding reflex `Fraunces` italic words or single-font width-axis tricks |
| `RHY` | Rhythm & scale | Fluid `clamp()` scales and line widths varied by content type instead of one global formula |
| `BASE` | Base layer | Standard resets, focus rings, and skip links (flagged as baseline engineering to keep, not strip) |
| `SRF` | Surface & texture | Purposeful shadows and textures instead of pasted `feTurbulence` noise or three-layer radial glows |
| `EDGE` | Radius & borders | Mixed border radii and border weights by component role instead of all-16px or all-0px rules |
| `NAV` | Navigation | Navigation layout fitted to the page content rather than default sticky blur bars or 76px vertical rails |
| `HERO` | Hero | Hero composition with real imagery and layout hierarchy instead of centered gradient walls or staircase text |
| `GRID` | Listing structure | Grids sized for the actual items instead of automatic 3-up cards, 6-column bentos, or fake `LOT` ledgers |
| `HOV` | Hover grammar | Component-specific hover states instead of global `translateY(-4px)` lifts or duplicated-span text rolls |
| `MOT` | Reveal & easing | Scroll timelines and varied easing curves instead of one `IntersectionObserver` fading in every block |
| `CHR` | Chrome & labels | Meaningful section headings instead of `§ I` markers, fake Roman numerals, or monospace eyebrows everywhere |
| `LIVE` | Liveness flourishes | Clocks, tickers, and counters used only when backed by real live data |
| `IMG` | Imagery | Real photography with subject, mood, and crop specifications instead of CSS gradient placeholders |
| `END` | Footers | Closing sections designed as part of the page rather than boilerplate 4-column link grids |
| `META` | Convergence | Self-justifying CSS comments (`/* NOT 3-up */`, `/* not a translateY lift */`) and anti-template copy |

No pattern is permanently banned. An editorial serif, a bento grid, or a dark-and-gold palette is fine when the project actually calls for it. The audit flags patterns when they show up together as an unexamined default.

## Example design contract

Abbreviated output from **Direct** mode:

```markdown
## Design contract: tidal monitoring instrument

Posture: cinematic (default)
Levers: creativity 78 (working harbour utility) | layout_structure 84
(live station readout rather than a card dashboard) | immersivity 94
(scroll tracks the rising and falling tide)

Direction: tidal instrument

Palette: harbour slate, buoy orange, wet bone
- Accent: buoy orange, used only on active water-level alerts and primary actions,
  matching channel marker visibility against dark water.

Typography
- Context: shift logs, METAR weather strings, hydrographic tables
- Display: slab serif | Body/UI: humanist sans | Data: tabular monospace
- Serif role: section headers only. Italic role: live sensor readings.

Hero: instrument bezel framing a full-bleed harbour photograph

Motion:
- Sequence: slack water -> gauge wake-up -> surge -> seawall hold
- Scene 1: the waterline rises across the viewport on scroll, submerging
  the harbour photo while updating the depth gauge
- Scene 2: peak surge hits the seawall threshold, readings stabilize,
  and the frame settles onto the station access CTA
- Reduced motion: steps through the four tide states as static frames with captions
```

See [`SKILL.md`](../skills/workofart/SKILL.md) for the full contract specification.

## Example audit output

Abbreviated output from **Audit** mode:

```markdown
Verdict: carries the shared skeleton (editorial heritage) | 14 tells matched (5 high)

Slot fixes
1. TOK-5 token layer: tailwind.config colors duplicated in :root (src/tokens.css:8)
   -> keep a single source of truth and name variables after the project's actual UI roles.
2. TYP-4 typography: Fraunces with a single italic word in the hero (src/hero.css:31)
   -> restrict the display serif to one role (headers or pull-quotes) and remove decorative italics.
3. MOT-4 reveal engine: single IntersectionObserver at -8% rootMargin on every section (app.js:44)
   -> render above-the-fold and primary content immediately; tie scroll animations to specific transitions.

Surface fixes
4. CHR-4 chrome: "§ I" and "§ II" section markers (index.html:96)
   -> replace with plain section headings or remove.

Keep: box-sizing reset, :focus-visible outlines, skip link, fluid clamp() typography
```

Matching 8 or more tells usually indicates a generated template, even if the color palette was customized. See [`references/audit.md`](../skills/workofart/references/audit.md) for the full audit workflow.

## Standalone scanner

[`scripts/scan.py`](../skills/workofart/scripts/scan.py) runs on Python 3.10+ with the standard library and requires no third-party packages:

```bash
python skills/workofart/scripts/scan.py path/to/site            # grouped summary, top hits per tell
python skills/workofart/scripts/scan.py path/to/site --all      # print every match
python skills/workofart/scripts/scan.py path/to/site --max 10   # max matches shown per tell (default: 3)
python skills/workofart/scripts/scan.py path/to/site --json     # JSON output
```

- Scans `.css`, `.scss`, `.sass`, `.less`, `.html`, `.htm`, `.js`, `.mjs`, `.cjs`, `.ts`, `.jsx`, `.tsx`, `.vue`, `.svelte`, and `.astro` files.
- Ignores `node_modules`, `.git`, `.next`, `.nuxt`, `.svelte-kit`, `dist`, `build`, `.cache`, and `coverage` directories.
- Outputs candidate matches with `file:line` locations. Matches are starting points for inspection, not automatic failures.
