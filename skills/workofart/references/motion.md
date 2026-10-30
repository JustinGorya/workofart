# Motion: Scroll Choreography and Immersivity

Motion controls **when** information enters, **what changes state on screen**, **how one scene transitions into the next**, and where the page speeds up or pauses. At low `immersivity` the page behaves as a static document; at high `immersivity` scroll acts as a timeline playhead driving a sequence of scenes.

Two common failure modes to avoid:
1. **Decoration without sequence:** sprinkling fade-ups, floating particles, magnetic buttons, and mouse parallax onto a stack of unrelated sections. Define the narrative sequence first (§4), map motion to specific section beats (§5), and verify the band requirements (§7).
2. **Unrequested timidity:** shipping a static page where sections merely fade in on scroll when the user never asked for a calm layout. Unless the user asks to tone motion down, build for the default interactive band (`immersivity` 85–98).

---

## 0. Default motion profile (`immersivity` 85–98)

When the user has not requested a calm or static page, `immersivity` defaults to **85–98** and includes:

- **A staged opening:** the initial viewport renders complete and legible, then transitions within ~2 seconds into the opening scene as the user begins scrolling.
- **Two or more full-viewport pinned scroll scenes** with distinct roles (for example: *problem state -> product assembly -> live proof*), each pinned across enough scroll distance (`200–500vh`) to step through clear state changes on a central subject.
- **A persistent visual subject or motif:** an object, interface view, photograph crop, or geometric element that carries across scenes so transitions feel continuous.
- **Scene-level choreography:** every major section has a planned entrance, active state, and transition into the next section.
- **Camera and depth:** scale shifts, crop expansion, layered foreground/background depth, and full-bleed media tied to scroll progress.
- **Typographic choreography at key transitions:** headlines that scale, mask, or align with the scene's state change.
- **Pacing contrast:** dense scroll sequences followed by quiet, stable holds, leading into a calm final CTA.
- **A complete `prefers-reduced-motion` fallback** that preserves every step of the sequence as static frames.

The brief dictates the *style* of motion (crisp mechanical cuts for fintech vs. slow atmospheric dissolves for hospitality); only an explicit user request lowers the *amount*.

---

## 1. Six motion layers

1. **Entrance / reveal:** opacity, translation, clip-path/mask wipes, scale from origin, or staggered groups.
2. **Exit / departure:** receding, collapsing, or handing off into the next frame.
3. **Camera / depth:** multi-plane scroll parallax, push-in/pull-back scaling, crop expansion, and perspective shifts.
4. **Scroll-pinned scenes:** full-viewport stages (`min-height: 100svh`) where normalized scroll progress (`0..1`) drives state changes on a central subject.
5. **Continuity:** shared elements, matching crops, or color/shape handoffs connecting adjacent sections.
6. **Ambient / reactive:** subtle lighting shifts, film grain, canvas shaders, or pointer feedback. Ambient effects support the atmosphere and never replace the main scroll sequence.

---

## 2. Motion feel

Pick one primary feel for the contract:
- **Smooth:** long durations, gentle deceleration; suited to hospitality, editorial, and luxury.
- **Snappy:** short durations (`120–220ms`), crisp deceleration, zero overshoot; suited to developer tools, fintech, and productivity apps.
- **Elastic:** spring physics with controlled overshoot; suited to playful consumer products and games.
- **Cinematic:** staged camera movements, long holds, and deliberate cuts; suited to launches, storytelling, and brand campaigns.
- **Mechanical:** linear or stepped timing with instant cuts; suited to industrial, hardware, and brutalist directions.

---

## 3. Motion directions

At `immersivity >= 41`, name a motion direction from the list below or coin a specific 2–4 word description:

| Direction | Behavior | Typical feel |
|---|---|---|
| Editorial cinema | Slow staged reveals, generous pauses, chapter transitions | mid–high / cinematic |
| Product keynote | Pinned hardware or UI assembly, exact snap states | high / snappy |
| Brutalist cuts | Instant state switches, stepped timing, zero easing softness | low–mid / mechanical |
| Vaporwave drift | Horizontal marquees, chromatic shifts, scanline transitions | mid–high / smooth |
| Tactile interface | Spring-loaded controls, responsive surface elevation | mid–high / elastic |
| Mechanical command | Uniform timing, telemetry updates, instrument readouts | low–mid / mechanical |
| Generative ambient | Reactive canvas or particle field framing a central subject | very high / cinematic |
| Cinema noir | High-contrast lighting shifts, deep parallax, slow reveals | mid–high / cinematic |
| Festival showcase | Full-bleed shader transitions, expressive kinetic typography | max / playful |
| Print-aware | Clean initial entrance, then rock-steady reading columns | low–mid / smooth |
| Split-text stage | Choreographed typographic locks and phrase transitions | mid–high / cinematic or snappy |
| Quiet luxury | One unhurried transformation per act, long holds | mid / smooth |
| Industrial conveyor | Step-by-step mechanical progression across the viewport | high / mechanical |
| Playful toy | Bouncy spring physics, oversized tactile reactions | mid–high / elastic |
| Kinetic showcase | Split text + pinned scroll scenes + reactive cursor + canvas | high–max (**avoid using as an unexamined default**) |

Do not bolt the generic kinetic showcase pack (split text + magnetic cursor + floating particles + looping marquee) onto every project. Match the motion architecture to what the product actually does.

---

## 4. Sequence architecture (`immersivity >= 41`)

State the page's **narrative sequence** in one sentence in the contract:

> **Opening premise -> tension / problem -> discovery -> transformation / proof -> climax -> resolution / CTA**

For each major section, define:
1. **Role:** what this step communicates.
2. **Visible change:** what physically changes on screen as the user scrolls.
3. **Handoff:** how this section transitions into the next.
4. **Pacing:** whether the section accelerates, holds steady, or simplifies.

| `immersivity` band | Structural requirements |
|---|---|
| 41–55 | Clear opening premise, ordered progression, resolution, and one recurring visual motif |
| 56–70 | Three-part arc; every section has a defined beat and transition; at least one scroll-linked state change crosses a section boundary |
| 71–85 | Distinct acts, one full-viewport pinned scroll scene (`~100svh`), a primary transformation before the CTA, and a calm resolution |
| 86–100 | Staged opening, multiple acts, 2+ full-viewport pinned scroll scenes with distinct purposes, a transforming central subject, deliberate quiet holds, and a stable closing CTA |

**Rules for full-viewport pinned scenes (`>= 71`):**
- Use a `~100svh` sticky stage inside a `200–500vh` scroll container.
- Every scroll segment must visibly advance the state of the subject (revealing internal structure, updating live data, shifting camera angle, or resolving a comparison).
- Provide clear orientation cues (step indicators, chapter labels, or a progress bar).
- **Avoid dead scroll:** if `300px` of scrolling produces no visible state change, shorten the scroll track.
- **Never trap the user:** standard wheel scroll, trackpad, touch, keyboard navigation, and `prefers-reduced-motion` must all reach every piece of content cleanly.
- A horizontal pin-scroll that simply slides static cards sideways without changing state is a tell (`GRID-4`), not a set piece.

---

## 5. Section beats (`immersivity >= 56`)

Map each section as `[beat] -> [visible change] -> [handoff]`:
- **Opening:** title and hero subject lock into place; first scroll initiates the sequence.
- **Tension:** scattered inputs or before-state elements show the friction the product solves.
- **Discovery:** pinned product or subject view steps through its key layers or capabilities.
- **Proof:** before/after comparison or real metrics resolve on screen.
- **Climax:** primary full-viewport transformation completing the story arc.
- **Resolution / CTA:** motion settles, distractions clear, and the call to action holds steady.

---

## 6. Stillness, purpose, and accessibility

- **Deliberate holds (`>= 65`):** follow dense scroll sequences with calm, stable sections so the user can read and act. Include roughly one calm hold for every 2–3 motion-heavy scenes.
- **Clear purpose:** every animation should either advance the sequence, clarify structural hierarchy, show causal connection between states, or provide immediate UI feedback.
- **`prefers-reduced-motion`:** provide a clean stepped or static presentation that keeps all content, headings, and state comparisons intact without relying on a destructive `* { animation: none !important }` reset (`BASE-3`).

---

## 7. Minimum requirements by band

- **1–20 (Static):** instant state feedback only; no decorative animation.
- **21–40 (Sequential):** clean hover/focus transitions and subtle group entrances.
- **41–55 (Guided):** named motion direction, one-sentence sequence, recurring motif across 3+ moments, multi-layer opening entrance, and at least one cross-section transition.
- **56–70 (Journey):** all of the above, plus `[beat -> change -> handoff]` mapping for every section, one scroll-linked state transformation, exit transitions on 2+ sections, and at least one deliberate quiet hold.
- **71–85 (Cinematic):** all of the above, plus at least one `~100svh` pinned scroll scene that transforms a central subject, varied pacing across acts, and a quiet hold before or at the CTA.
- **86–100 (Interactive cinema, default):** all of the above, plus a staged opening (`~2s`), **2+ full-viewport pinned scroll scenes** with different roles, a persistent subject that transforms across acts, and a complete `prefers-reduced-motion` stepped fallback.

---

## 8. Opening viewport check (`immersivity >= 41`)

Ensure the initial frame renders legible and complete before JavaScript runs.
- **41–60:** staged entrance establishes typographic hierarchy and introduces the visual motif; scrolling immediately reveals the next beat.
- **61–80:** opening frame sets the subject; first scroll visibly changes the scene state.
- **81–100:** staged opening sets the premise and hands off directly into the first scroll-driven scene.

---

## 9. Motion tells to avoid (`immersivity >= 41`)

- **Identical fade-ups on every block:** using one `opacity: 0 -> 1` + `translateY(30–40px)` observer across the entire page (`MOT-4`, `MOT-5`, `MOT-7`, `MOT-8`).
- **Single hover effect everywhere:** applying the same `translateY(-4px)` lift, ink/paper swap, or odometer text roll to every link, button, and card (`HOV-1` through `HOV-5`).
- **Ambient noise replacing structure:** relying on a looping marquee, floating particles, or a `feTurbulence` overlay instead of scroll-linked progression.
- **Decorative "live" widgets:** adding a looping ticker, fake odometer counter, `Europe/Zurich` live clock, or `Math.random()` reference ID when the site has no real live data (`LIVE-1` through `LIVE-4`).
- **Unrequested downshifting:** building a plain fade-in page when the user never asked for a calm or static design.

---

## 10. Easing and timing hierarchy (`MOT-1`, `MOT-2`, `MOT-3`, `MOT-9`)

Generated stylesheets routinely route every transition through a single custom bezier curve (such as `cubic-bezier(.2, .7, .2, 1)` or `cubic-bezier(.62, .04, .22, .96)`) and never use `ease-in` or `linear`. Build a differentiated timing scale instead:

- **Direct UI actions (hover, press, toggle):** `120–200ms` with crisp `ease-out`.
- **Entrances:** `350–600ms` with deceleration suited to the motion feel.
- **Scroll-scrubbed timelines:** bind directly (`linear`) to the `0..1` scroll playhead, shaping individual sub-beats along the timeline.
- **Exits and dismissals:** `150–300ms` with `ease-in` so departing elements accelerate cleanly off screen.
- **Ambient loops:** long durations with `linear` or sine timing, paused when offscreen via `IntersectionObserver`.
- **Mechanical / brutalist transitions:** `steps()` or instant `0ms` state changes.

---

## 11. Performance guardrails

| Band | Concurrent animations | Target frame rate (desktop / mobile) | Heavy effects budget |
|---|---|---|---|
| 1–20 | 0 decorative | 60 / 60 | None |
| 21–40 | ~4 | 60 / 60 | Lightweight CSS transitions |
| 41–60 | ~8 | 60 / 60 | Light scroll parallax, simple cross-section transitions |
| 61–80 | ~12 | 60 / 60 | One full-viewport scroll timeline |
| 81–100 | ~16 (max 8 on mobile) | 60 / 30+ | 2+ scroll timelines; canvas/WebGL only with mobile fallback |

If frame rate drops, simplify expensive paint/composite effects (such as large blurs or heavy shaders) before cutting the structural scroll beats.
