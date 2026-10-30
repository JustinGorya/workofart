---
name: workofart
description: Design and build distinctive frontends, or audit existing CSS, HTML, JSX, and Tailwind for recurring AI design patterns. Use for website, landing page, app, dashboard, and portfolio design; art direction, typography, layout, and scroll choreography; or requests to identify and fix templated AI output. Provides Direct, Build, and Audit modes with a brief-derived design contract and a Python scanner.
license: MIT
---

# Work of Art

This skill operates in three modes:
- **Direct** defines what a design should look and behave like from the brief, before any code is written.
- **Build** implements a locked design contract and checks its own output before delivery.
- **Audit** inspects existing code at the byte and structure level to spot default AI patterns.

Why all three belong together: AI-generated websites converge on a single underlying layout and CSS skeleton across unrelated prompts. When told to avoid specific defaults, models swap the forbidden values for new defaults in the exact same structural slots. Four generations of this convergence are cataloged in `references/tells.md`. Avoiding generic output requires deriving each structural slot from the project brief first, and then auditing the slots rather than chasing a growing ban list.

**Default posture: cinematic and ambitious.** Unless the user asks for something restrained, design every page as a directed experience: a staged opening, full-viewport scroll scenes where scroll drives the timeline, layouts that use overlap, full-bleed imagery, and strong scale contrast, and motion that carries a clear sequence from opening frame to final call to action. Users do not need to ask for more ambition or motion. They only need to say when they want something calmer, classical, minimal, or static, in which case the skill steps down on the specific dimensions requested (§2.1).

---

## 0. Modes

| Mode | Activates when | Output | Next step |
|---|---|---|---|
| **Direct** (default) | Any design question: direction, aesthetic, palette, typography, layout, motion, "what should this feel like?", "lock the direction" | A design contract (§4) | **Stop.** End with the checkpoint question. Do not write code. |
| **Build** | Explicit build request: "build it", "implement", "code it", "make it real", "convert to React/HTML/Tailwind" | Production code from a locked contract | Run the self-audit (§5) before delivering. |
| **Audit** | "Does this look AI-generated?", "clean up the AI tells", "why does this feel templated?", or when the user provides CSS, markup, or a URL to evaluate | Verdict + numbered fix list (§6) | Offer to apply fixes. |

**Mode transitions:**
- Follow-up design tweaks after a contract ("warmer palette", "different hero") stay in **Direct** mode. Revise and output the updated contract.
- If the user asks to build right away with no prior contract ("build me a landing page for a ceramics studio"), write a **compact inline contract** first (posture, levers, palette, typography, edge, hero, media, motion sequence, set pieces: one line each), then write the code in the same response.
- During **Build**, treat the contract as locked. If implementation exposes a flaw in the contract, flag it before improvising.
- **Audit** never rewrites files unprompted. Deliver the report first and apply fixes on request.

---

## 1. Core rules

1. **Tie every decision to the brief.** Every choice must complete the sentence *"X because [concrete brief detail]"* (subject matter, audience, task, place, era, physical material, lighting, content density, or existing brand assets). Words like "premium", "modern", "clean", "creative", "elegant", or "different" are not brief signals.
2. **Design slots, not isolated tokens.** Every page has a recurring set of structural slots: token definitions, display typography, navigation geometry, hero layout, feature/listing grid, hover states, scroll reveals, section labels, interactive flourishes, and footer. Renaming `--bg` to `--paper`, swapping `Inter` for `Fraunces`, or replacing a `translateY` hover with an odometer text roll leaves the slot unchanged. Decide how each slot should work for this project, or whether the slot is needed at all.
3. **No pattern is permanently banned, but every pattern must be earned.** An amber-on-cream palette, an editorial serif, a bento grid, a horizontal pin-scroll, or a live timezone clock can each be the right choice when the project's subject matter calls for it. Using a pattern because the brief demands it is a design decision; using it as a fallback to look "designed" is a tell.
4. **Do not design by inverting the tell index.** Treating `references/tells.md` as a checklist of things to invert while designing simply produces the next predictable template. Design from the brief first, then use the tell index afterward as a check.
5. **Never write self-justifying comments or copy.** Do not write CSS or JS comments like `/* NOT 3-up */` or `/* not a translateY lift */`, and do not write marketing copy bragging that the page is not a template (META-2, META-3).
6. **Keep baseline engineering intact.** Box-sizing resets, `prefers-reduced-motion` handling, fluid `clamp()` typography, CSS custom properties, `:focus-visible` states, and skip links are standard engineering hygiene. Keep them; put the creative work into layout, imagery, typography, and interaction.
7. **Use real photography and sequence-driven motion.** Named, art-directed photography beats CSS gradients and abstract SVG shapes. A clear narrative sequence is what makes heavy scroll motion coherent rather than noisy.
8. **Connect scenes with a single through-line.** Five unrelated visual effects make a demo reel; five scenes that track one transforming subject make a cohesive page. Contrast dense, motion-heavy sequences with quiet holds so the page can breathe.
9. **Only the user lowers the ambition.** Industry category, B2B context, or a short prompt never lower the levers automatically. Those factors change the *style* of execution (for example, crisp mechanical transitions for a financial tool vs. slow atmospheric cuts for a hotel), not the level of craft. Lower the levers only when the user asks for calm, classic, minimal, or static output.
10. **Preserve existing brand systems.** When the user supplies a logo, color palette, fonts, or brand guidelines, use them faithfully. Channel the creative work into layout composition, pacing, imagery, and motion rather than inventing a competing identity.

**When choosing between two readable options, prefer:** the more ambitious composition, a full-viewport scene over a stacked block, a full-bleed photograph over a framed box, scroll as a timeline playhead over simple fade-ins, a visual subject that changes state over background decoration, and deliberate pauses between heavy motion sequences.

---

## 2. The three levers

Every design contract sets three independent 1–100 parameters:

| Band | Label | Behavior |
|---|---|---|
| 1–20 | Conventional | Standard utility templates allowed. Used only when requested. |
| 21–40 | Polished | Familiar page structure with one distinct layout choice per section. Used when the user asks for calm or classic output. |
| 41–60 | Distinct | Custom palette, named section patterns, and guided scroll progression. Used when the user asks to tone things down. |
| 61–80 | Bold | Overlap, full-bleed imagery, scale jumps, art-directed photography, and scene-based motion. **Floor of the default.** |
| 81–100 | Avant-garde | Full art direction, scroll-driven timelines, and multiple full-screen scenes. **Default band.** |

- **`creativity`**: palette, typography character, surface treatments, and edge styling. Controls how committed the visual direction is, not which font category is chosen.
- **`layout_structure`**: grid behavior, asymmetry, overlap, full-bleed usage, and section variety. At `>= 25`, standard AI section templates are off the table unless requested.
- **`immersivity`**: scroll-driven state changes and motion choreography. At `>= 41`, commit to a named motion direction and a clear sequence; at `>= 71`, include at least one full-viewport pinned scroll scene; at `>= 86`, include two or more.

### 2.1 Default ranges and stepping down

**Default (when the user has not asked for calm or minimal output):** `creativity` **75–90**, `layout_structure` **75–92**, `immersivity` **85–98**. Pick exact numbers based on the brief's strongest signals, staying within those ranges. By default, include a staged opening, **two or more full-viewport scroll set pieces**, a recurring visual subject that changes state across sections, custom scene compositions, and a clear transition into the final CTA.

**Stepping down based on user instructions:**

| User request | Adjustment |
|---|---|
| "calm", "classic", "classical", "traditional", "conventional", "understated", "quiet" | All three levers move to **21–45**; no pinned scroll scenes unless requested |
| "minimal", "simple", "clean and simple", "basic", "no-frills" | All three levers move to **10–30**; one deliberate layout choice per section |
| "no animation", "static", "subtle motion", "reduced motion" | **`immersivity` only** moves to **1–25**; `creativity` and `layout_structure` stay at default |
| "calm layout", "standard structure" | **`layout_structure` only** moves to **20–40**; the other two stay at default |
| "keep the styling clean / restrained" | **`creativity` only** moves to **30–45**; `layout_structure` and `immersivity` stay at default |
| Explicit numbers | Use the exact numbers requested |

A request about a single dimension lowers only that lever. For example, *"calm motion with an unconventional layout"* sets `85 / 85 / 25`, not `35 / 35 / 35`.

**Functional interfaces** (dashboards, admin tools, application shells) keep high `creativity` and `layout_structure`, while expressing `immersivity` through spatial view transitions, state changes, and entry choreography rather than long scroll timelines that get in the way of daily use.

See **`references/levers.md`** for full scoring rules.

---

## 3. Structural slot map

How the four AI skeleton generations (`template` -> `paper/ink` -> `editorial heritage` -> `atelier-ledger`) fill each slot by default, and what justifies a choice in that slot. Tell IDs reference `references/tells.md`.

| Slot | Recurring AI defaults across generations | When a choice is justified |
|---|---|---|
| **Palette** | Off-white + ink + amber/coral (light); black + gold (dark); bone + racing green + brass or chalk + ink + oxblood (heritage); navy + cyan, purple + blue, gray + white cards | The accent color traces to a specific detail in the brief (e.g., *"kelp green for marine biology"*). Use heritage palettes only for actual heritage motoring, estates, or bespoke craft. (PAL-1…4) |
| **Token layer** | `--bg/--surface/--accent/--radius:16px` -> `--paper/--ink/--rule` -> Tailwind colors duplicated in `:root` -> `:root` deleted with seven fixed natural color names in `tailwind.config` | Variable names reflect the project's domain, the number of variables matches actual usage, and colors live in a single source of truth. (TOK-*) |
| **Typography** | `Inter`/system stack -> `Space Mono` + `Oswald` -> `Fraunces` with a single italic accent word -> single grotesque split across `font-stretch: 125%` and `100%` | Font categories match the task, audience, script, or brand. A display serif is restricted to **one role** (headlines *or* pull-quotes) unless the brand is genuinely print-based. (TYP-*) |
| **Edge / radius** | `16px` radius + soft shadow everywhere -> `border-radius: 0` on `*` -> all-pill vs. all-square extremes | A tiered radius policy where cards, buttons, inputs, badges, and images have distinct edge treatments. (EDGE-*) |
| **Surface / texture** | Stacked radial-gradient hero wall -> fixed full-screen `feTurbulence` noise overlay -> mousemove parallax photo | At most one texture or blur surface where it fits the subject matter. (SRF-*) |
| **Navigation** | Frosted glass bar + `.scrolled` toggle -> sticky bar with `2–4px` ink border -> "by appointment" masthead -> `76px` vertical left rail + overlay | Navigation layout follows the page structure and link count (top bar, dock, rail, or inline header). (NAV-*) |
| **Hero** | Centered text over radial gradients + 2 buttons -> 50/50 split -> `Fraunces` italic statement -> staircase-indented uppercase lines | A named hero layout combined with overlap, full-bleed imagery, offset alignment, or scale contrast. (HERO-*) |
| **Listings / features** | `auto-fit` card grid -> 3–4 bordered cells -> 6-column bento with one `span 3` cell -> annotated specimen -> `LOT 01` rows crossfading a sticky spec pane | Grid structure matches the items being shown. Use a bento layout only when one item truly dominates; use diagrams or spec sheets only for real parts and specs. (GRID-*) |
| **Proof / pricing / contact** | 3-up avatar quote cards, uniform logo grid, 3 equal pricing cards with the middle highlighted, left-info / right-form split | Custom section patterns from `references/layout.md` §4 (standard templates allowed only at `layout_structure <= 20`). |
| **Hover states** | Global `translateY(-4px)` + shadow -> ink/paper color swap -> 4-verb hover bundle -> duplicated-label odometer roll | Two or three distinct hover behaviors assigned by component type and used consistently. (HOV-*) |
| **Reveals / easing** | Single `IntersectionObserver` at `-8%` rootMargin -> `--ry/--rd/--d` at `0.22` threshold -> 4-gesture `[data-rv]` at `0.3` threshold; one `cubic-bezier` curve for all transitions | Above-the-fold and primary content renders immediately; scroll reveals follow section transitions; easing curves vary by interaction type. (MOT-*) |
| **Chrome / labels** | Tracked uppercase accent eyebrows -> monospace vertical side rails -> `§ I` / `Est. MCMLXII` markers -> `8.5px–10.5px` monospace caption plates | Section labels convey real information; monospace type stays on numbers, code, and timestamps. (CHR-*) |
| **Liveness flourishes** | Scroll-drawn SVGs -> duplicated-DOM marquee tickers -> odometer digit columns + live `Europe/Zurich` clock + `Math.random()` reference IDs | Live widgets appear only when backed by real schedules, inventory, or live data from the brief. (LIVE-*) |
| **Imagery** | CSS gradient `.thumb-1` boxes -> abstract SVG blobs -> museum caption plates pinned to every photo | Real photography with specified subject, mood, and crop in every image-bearing section. (IMG-*) |
| **Footer / closers** | `1.6fr 1fr 1fr` columns + copyright bar -> giant italic wordmark -> full-bleed quote interlude + `SET IN X & Y` colophon | Footer layout fits the content and closes the page cleanly. (END-*) |

**Patterns flagged with ⚑ in `references/layout.md`:** Several layout patterns (dominant-cell bento, annotation rails, sticky spec panes, exploded diagrams, horizontal pin-scroll, staircase headlines) are useful patterns that also became frequent AI fallback choices. Only use a ⚑ pattern when the content genuinely calls for it and you pair it with a custom layout adjustment.

---

## 4. Direct mode: the design contract

Analyze the brief, then output the contract using the structure below.

1. **Read the brief:** identify the product, audience, context of use, tone, content density, industry norms, visual references, and any existing brand assets. Infer missing details and state your assumptions directly inside the contract rather than stopping to ask preliminary questions.
2. **Set the three levers** (§2, `references/levers.md`). Start in the default ranges (§2.1) and lower a lever only if the user's prompt asks for it. Tie each number to a detail in the brief.
3. **Define the six core areas:** palette, typography, edges, layout, motion (when `immersivity >= 41`), and media (`references/direction.md`, `references/layout.md`, `references/motion.md`, `references/media.md`).
4. **Give the direction a 2–4 word name** tailored to the brief (e.g., *kiln-glaze utility*, *civic risograph*, *tidal instrument*), or use a style name from `references/direction.md` §5 if it fits directly.
5. **Check the slot map (§3).** Verify that every slot choice has a concrete reason from the brief rather than falling back on a default filler.
6. **Format the output.** For narrow questions (*"what palette works for a retiree fintech app?"*), output only the relevant section. For full project briefs, output the complete contract:

```markdown
## Design contract: [project]

**Posture**: cinematic (default) | stepped down: [which levers] because the user requested "[exact words]"
**Levers**: creativity N ([reason]) | layout_structure N ([reason]) | immersivity N ([reason])
**Direction**: [2–4 words]

**Palette**: [descriptive name, e.g. "azulejo blue, lime, and bone"]
- Temperature / mode: [ ... ] | Accent: [hue] because [brief signal]
- Roles: bg, bg-alt, fg, fg-muted, accent, rule (descriptive color names, not hex codes)

**Typography**
- Context: [task / audience / content / script / brand signal]
- Display: [category + real font family] | Body/UI: [category + real font family] | Data: [if needed]
- Hierarchy contrast: [weight / width / optical size / case / scale / placement]
- Alternatives considered: [two categories and why they were ruled out]
- Serif role: [none | single role: ___ because ___] | Italic role: [specific semantic job | none]

**Edge policy**: [sharp / small / mixed / large / asymmetric / chamfered] and how each tier maps to components

**Layout**: [one-sentence summary of spatial structure]
- Hero: [pattern] + [structural adjustment]
- Sections *(layout_structure >= 41)*: features [pattern] | proof [pattern] | pricing [pattern] | CTA [pattern], detailing how each scene is composed and transitions into the next
- Flagged (⚑) patterns used: [content justification]

**Motion** *(immersivity >= 41)*: direction [name] | feel [smooth / snappy / elastic / cinematic / mechanical]
- Premise: [the opening tension or question]
- Sequence: [opening -> shift -> proof -> resolution] | Recurring motif: [element that carries across scenes]
- Ambient layer: [grain / light shift / particles / shader / none] and its role
- Section beats *(>= 56)*: [section: beat -> visible change -> handoff], one line per section; Climax: [primary transformation]
- Pinned set pieces *(>= 71; 2+ at >= 86)*: [act, purpose, central subject, scroll states, exit] | Orientation cue: [chapter marker / progress / anchor]
- Quiet holds *(>= 65)*: [where the motion pauses so the user can read or act]
- Reduced-motion fallback: [how the sequence works as static frames or stepped states]

**Media**: [photography (Unsplash / local) | product UI | illustration | diagram | CSS/SVG abstraction only under media.md §3 rules]
- Hero: [subject + mood + crop] | Each image section: [subject + mood + crop]

**Brief-specific anchor**: [one sentence naming the design decision that only makes sense for this specific project]
```

7. **End with the checkpoint question:** *"That covers the direction. Would you like to adjust the palette, layout, or motion, or should I build it?"*

---

## 5. Build mode

Implement the locked contract faithfully. Full implementation details are in **`references/build.md`**:

- **Stack:** use the project's existing stack. If starting fresh with no stack specified, use semantic HTML, CSS, and vanilla JS. At default `immersivity` (85+), use a real scroll timeline (GSAP + ScrollTrigger, Lenis if smooth scrolling fits, Framer Motion in React, or native scroll-driven animations / `requestAnimationFrame` progress calculations). Below `immersivity` 56, stick to CSS transitions and native APIs unless a library is already installed.
- **Tokens:** maintain a single source of truth named in the project's domain vocabulary. Never duplicate `tailwind.config` colors into `:root`.
- **Typography:** load real fonts with only the required weights and genuine italics (`font-synthesis: none`), set appropriate fallbacks and `font-display`, and keep monospace type restricted to technical/numerical data.
- **Imagery:** every image-bearing section must load a real photograph (`references/media.md` §5) with explicit `aspect-ratio` or dimensions, descriptive `alt` text, and a clean container background fallback. Never use CSS gradient divs as image stand-ins.
- **Motion:** drive scroll scenes from a normalized `0..1` progress value rather than attaching an identical `IntersectionObserver` fade-in to every block. Animate `transform` and `opacity`, vary easing curves by action type, and provide a clean `prefers-reduced-motion` layout.
- **CSS structure:** vary fluid `clamp()` scales and max-widths by content role, choose breakpoints where the layout actually needs to reflow, use border widths for hierarchy, and omit self-justifying comments.
- **Accessibility:** include semantic landmarks, WCAG AA contrast, `:focus-visible` outlines, full keyboard navigation, `44x44px` minimum touch targets, and labeled form controls.

**Pre-delivery check:** run `python scripts/scan.py <output-dir-or-files>` and inspect every match. Where code cannot run, check the output by hand against `references/checklist.md` Part C and `references/tells.md`, and say that the scanner was not run. Keep patterns that were explicitly chosen in the contract; rework any slot that fell back to an unexamined default. Include a brief 1–2 sentence note covering any implementation choices made outside the contract.

---

## 6. Audit mode

Full workflow, grep patterns, and generation signatures are in **`references/audit.md`**, with the full tell table in **`references/tells.md`**.

1. **Scan:** run `python scripts/scan.py <path>` on the target files (`.css`, `.html`, `.js/.ts`, `.jsx/.tsx`, `.vue`, `.svelte`, `.astro`). For a live URL, download the HTML and stylesheets to a temporary folder first; if you cannot fetch it, ask the user to paste or attach the source. Where code cannot run, work through `references/checklist.md` Part C and `references/tells.md` by hand. Scanner matches are candidates to verify in context. For pasted code, cite line numbers within the snippet in place of `file:line`.
2. **Inspect in structural order:** tokens -> reset -> body -> surface textures -> nav -> hero -> grids -> hover states -> headings/labels/serif usage -> scroll observers, inline scripts, and comments. On Tailwind sites, check `class` attributes, inline `tailwind.config` blocks, and script tags.
3. **Evaluate structure over colors:** changing hex codes does not change a shared layout skeleton.
4. **Format the report:**

```markdown
**Verdict:** carries the shared skeleton ([template | paper-ink | editorial-heritage | atelier-ledger | mixed]) | [N] tells matched ([H] high severity)
   or
**Verdict:** does not carry the shared skeleton. [One-sentence summary of what makes the structure distinct.]

**Slot fixes (structural changes, ordered by severity)**
1. [ID] [slot]: found `exact value` (`file:line`) -> fix: [concrete structural change for this slot]
...

**Surface fixes**
...

**Keep**: [baseline engineering worth keeping: resets, focus states, skip links, fluid type]
```

Matching **8 or more tells** (or matching several high-severity structural slots across tokens, nav, hero, grid, hover, and reveals) indicates a shared template skeleton. End the report by asking: *"Would you like me to apply these slot fixes, or establish a new design contract first?"*

---

## 7. Pre-response checklist

See **`references/checklist.md`** for the complete verification lists (Part A for contracts, Part B for builds, Part C for the 27-point skeleton check). Before sending any response, verify:

- [ ] Every lever score, accent color, font category, and flagged (⚑) pattern is tied to a concrete detail in the brief.
- [ ] Unless the user asked for a calmer style, `creativity` and `layout_structure` are `>= 75`, `immersivity` is `>= 85`, and the design includes a staged opening and 2+ full-viewport scroll scenes.
- [ ] None of the reflex palettes (`PAL-1` through `PAL-4`) are used without a direct subject-matter reason, and unrelated briefs in the same session do not share an accent color.
- [ ] Display serifs are limited to a single role, italics have a clear semantic function, and typography works across body copy, UI controls, numbers, and mobile screens.
- [ ] Border radii follow a multi-tier policy rather than all-16px or all-0px rules.
- [ ] At `layout_structure >= 25`, no section uses a boilerplate category template, and adjacent sections do not repeat the same layout structure.
- [ ] At `immersivity >= 41`, the motion has a named direction, a clear sequence, a transforming subject, and a working `prefers-reduced-motion` presentation.
- [ ] Every image-bearing section specifies (in Direct) or loads (in Build) real photography, unless exempted by `references/media.md` §3.
- [ ] Neither the code nor the copy contains self-justifying `/* NOT X */` comments or anti-template bragging.
- [ ] In Build and Audit modes, `scripts/scan.py` was executed (or, where code cannot run, the tell index was checked by hand) and every match was reviewed.

---

## 8. Guardrails

- **No code in Direct mode.** Wait for an explicit build prompt before generating implementation files.
- **Do not downshift on your own.** Do not fall back to a static, stacked-block layout just because a brief is short or corporate. Only the user's words lower the levers.
- **Do not reject appropriate patterns out of hand.** When a common pattern genuinely fits the project, use it and state the reason in one line.
- **No house style.** Derive palette, typography, layout, and motion fresh for each project.
- **Do not stall on missing specs.** Make reasonable assumptions, state them in the contract, and move forward.
- **No unprompted rewrites in Audit mode.** Present the audit findings first and wait for confirmation before editing files or rewriting code.

---

## Resource paths

All `references/` and `scripts/` paths in this skill are relative to the directory containing this `SKILL.md`, not the user's project. Resolve the skill installation directory before reading references or running `python <skill-directory>/scripts/scan.py <project-path>`. The scanner needs Python 3.10+ and only the standard library. It reports candidates for review; it does not edit project files. Everything else in the skill is plain Markdown, so the modes work the same where code cannot run.

## Reference files

| File | Contents |
|---|---|
| `references/levers.md` | Scoring rules and band requirements for `creativity`, `layout_structure`, and `immersivity` |
| `references/direction.md` | Palette derivation, typography rules, surface treatments, edge policies, and style vocabulary |
| `references/layout.md` | Hero and section patterns (including ⚑ flagged patterns) and layout pitfalls by band |
| `references/motion.md` | Scroll sequences, motion directions, band minimums, and easing rules |
| `references/media.md` | Photography requirements, Unsplash URL patterns and photo IDs, interaction states, accessibility |
| `references/build.md` | Implementation standards for HTML, CSS, JS, fonts, images, and scroll timelines |
| `references/tells.md` | All 85 AI layout and CSS tells organized across 17 structural slots |
| `references/audit.md` | Step-by-step audit workflow, grep commands, and generation signatures |
| `references/checklist.md` | Full QA checklists for contracts, builds, and stylesheet audits |
| `scripts/scan.py` | Zero-dependency Python scanner for detecting candidate tells with `file:line` output |
