# The Three Levers

Every design contract sets three independent 1–100 parameters. Higher numbers indicate stronger, more committed design choices rather than arbitrary complexity. Because the three levers are independent, an experimental layout with understated colors is valid, and so is bold visual styling with minimal motion.

**Default ranges start high.** Unless the user asks for a calmer or more traditional style, every project starts in the Bold and Avant-garde bands across all three levers (§4). The lower bands are used when the user asks for them.

| Band | Label | Behavior |
|---|---|---|
| 1–20 | Conventional | Familiar utility layouts (used on request) |
| 21–40 | Polished | Standard structure with one distinct layout move per section (used on request) |
| 41–60 | Distinct | Custom visual identity and guided scroll flow (used on request) |
| 61–80 | Bold | Strong, unconventional composition and motion (floor of the default) |
| 81–100 | Avant-garde | Full art direction and scroll-choreographed scenes (default band) |

---

## 1. `creativity`: visual character

Controls typography character, color palette, surface treatments, ornament, and edge styling.

| Score | Visual character |
|---:|---|
| 1 | OS-default UI: system sans-serif, neutral grays, plain borders, standard shadows. |
| 25 | Clean and specific: tinted neutrals, an accent color tied to a detail in the brief, and a deliberate font pairing. |
| 50 | Distinct identity: custom color palette, clear typographic hierarchy, intentional surface treatments, and art-directed photography. |
| 75 | Bold: strong brief-derived typography, layered surfaces, committed color palette, and heavily art-directed photography. |
| 100 | Full stylistic statement (e.g., cyberpunk, brutalist, art deco): strong lighting, custom surface treatments, mixed typographic roles, and dramatic framing. |

- **1–20**: used only when the user asks for plain utility UI.
- **21–40**: familiar structure, but already free of default AI palettes and font reflexes.
- **41–60**: clear visual point of view; used when the user asks to keep styling restrained.
- **61–80**: committed visual styling. High scores do not imply an editorial serif; font category stays independent of the score.
- **81–100**: expressive art direction. Real photography remains primary, with lighting, color grading, and surface treatments layered over it.

**`creativity` controls commitment, not font category, and never replaces photography with CSS gradients.** High creativity means stronger art direction on the photography (subject, crop, lighting, collage, duotone, masking), not falling back to abstract SVG blobs.

---

## 2. `layout_structure`: spatial composition

Controls grid construction, asymmetry, scale contrast, overlap, full-bleed imagery, and section variety.

| Score | Spatial structure |
|---:|---|
| 1 | Standard template: centered hero + 2 buttons -> 3 equal cards -> testimonial row -> CTA block. Symmetric and boxed. |
| 25 | Modified standard layout: familiar page flow with one deliberate compositional change per section. |
| 50 | Custom composition: asymmetric splits, one oversized anchor element per section, and varied section silhouettes. |
| 75 | Overlapping layers, full-bleed media, broken-grid alignments, strong scale contrast, and full-viewport frames. |
| 100 | Fully art-directed layout: overlapping planes, off-axis elements, poster-scale typography, and sections that transition directly into the next scene. |

**Key thresholds:**

- **1–20**: standard section templates are allowed when requested. Still include at least one distinct compositional detail.
- **21–24**: familiar section layouts are allowed if each major section includes a clear structural adjustment.
- **25–100**: boilerplate section templates (`references/layout.md` §6) are off the table. Spatial ambition scales with the score.

---

## 3. `immersivity`: scroll choreography and motion

Controls how strongly the page behaves as a **directed sequence rather than a static document**. It measures scroll-driven state changes first, and raw animation count second.

| Score | Motion behavior |
|---:|---|
| 1 | Static document with essential UI state feedback only. |
| 25 | Subtle entrance transitions that clarify reading hierarchy. |
| 50 | Guided progression: clear opening, development, and resolution, with a recurring visual motif and scroll-linked transitions. |
| 75 | Scroll-choreographed sequence: distinct acts, at least one full-viewport pinned scene where scroll drives the playhead, and a clear transition into the CTA. |
| 100 | Full interactive sequence: staged opening, 2+ full-viewport scroll scenes, a subject that transforms across acts, deliberate pacing with quiet holds, and a complete `prefers-reduced-motion` presentation. |

- **1–20 Static** | **21–40 Sequential** (subtle reveals, no pinned scenes) | **41–60 Guided narrative** (named motion direction and sequence required) | **61–80 Scene-based** (scroll-linked state changes and one full-viewport scene at 71+) | **81–100 Interactive cinema** (2+ full-screen scroll scenes at 86+, the default).

**High `immersivity` requires contrast in pacing, not constant movement.** A quiet full-screen hold before a transition carries more weight than five simultaneous background loops.

**Match the style of motion to the brief.** Two projects at score 90 should move differently depending on what they are: a crisp product assembly sequence for a developer tool, a chapter-based documentary layout for editorial, or slow lighting shifts for a hotel. Commit to a named motion direction (`references/motion.md` §3) and a clear sequence (`references/motion.md` §4).

---

## 4. Setting the lever values

**Start in the default ranges, and step down only when the user asks.**

| Lever | Default range |
|---|---:|
| `creativity` | 75–90 |
| `layout_structure` | 75–92 |
| `immersivity` | 85–98 |

Pick specific values inside these ranges based on the brief (Step 3), unless the user provides explicit numbers (Step 1) or asks for a calmer style (Step 2).

**Step 1: Explicit numbers.** If the user specifies numbers, use them directly and set the remaining levers from the brief.

**Step 2: User intent words.** Lower a lever only when the user's prompt asks for it, and lower only the dimension they mentioned:

| User prompt | `creativity` | `layout_structure` | `immersivity` |
|---|---:|---:|---:|
| "basic", "simple", "minimal", "no-frills" | 10–30 | 10–30 | 10–25 |
| "calm", "classic", "classical", "traditional", "conventional", "understated", "quiet" | 25–45 | 21–45 | 21–45 |
| "clean but modern", "polished", "professional and calm" | 40–55 | 40–55 | 35–55 |
| "no animation", "keep it static", "reduced motion" | default | default | 1–20 |
| "subtle motion", "light animation" | default | default | 30–50 |
| "keep the styling clean / restrained" | 30–45 | default | default |
| "standard layout", "conventional structure" | default | 20–40 | default |
| "professional" (alone), "premium", "B2B", "enterprise-grade" | default (sets a precise, product-led style) | default | default |
| "creative", "different", "modern" | default | default | default |
| "unconventional", "experimental", "wild", "avant-garde", "cinematic", "fullscreen scroll scenes" | 88–100 | 88–100 | 92–100 |

"Professional" or "B2B" by itself is not a request for a plain template; it calls for a sharp, disciplined product sequence.

**Step 3: Choose exact values within the default range using the brief.**
- *Which lever leads:* let the project's strongest trait push one lever toward the top of its range (a hardware or software product with moving parts pushes `immersivity` to 95+; an archive or publication pushes `layout_structure` to 90+; a fashion or music release pushes `creativity` to 90+).
- *Industry sets the style of execution:* SaaS/B2B -> product assembly and workflow proof; fintech/legal -> crisp, mechanical cuts; hospitality/wellness -> slow lighting transitions and long holds; consumer/brand -> tactile, kinetic composition; editorial -> chapter-based progression; developer tools -> terminal or architecture diagram transforming across scroll states.
- *Tone sets motion feel:* clinical/archival -> smooth or mechanical timing with long holds; playful -> spring physics; theatrical -> staged camera depth; industrial -> hard cuts.
- *High content density:* use a strong opening set piece for each major chapter while keeping the reading columns inside each chapter clean and legible.
- *Functional interfaces* (dashboards, admin panels, app shells): keep `creativity` and `layout_structure` high, and apply `immersivity` to view transitions, state changes, and onboarding rather than scroll-jacking the workspace.

**Step 4: Sanity check before locking the numbers.**
- Does each number point to a specific detail in the brief?
- Did any lever drop below the default range without the user asking for a calmer design? If so, bring it back into the default range.
- Did you reuse the exact same numbers from an earlier, unrelated brief? Adjust the leading lever to reflect what makes this project different.
- Remember that high `creativity` never replaces real photography with abstract CSS gradients (`references/media.md` §1).

**Step 5: Record the posture and numbers in the contract** with a short reason for each:
- *"Posture: cinematic (default) | Levers: creativity 82, layout_structure 86, immersivity 94 (the product's hardware assembly sequence drives the scroll timeline)."*
- *"Posture: stepped down on immersivity | Levers: creativity 80, layout_structure 84, immersivity 18 (user requested 'no animation')."*

---

## 5. Lever combinations

- **All three high (default):** full scroll-choreographed experience. Requires strict attention to performance, `prefers-reduced-motion` fallbacks, and text contrast.
- **High `creativity` + lowered `layout_structure`:** expressive typography, color, and motion inside a familiar layout structure (when the user requests a standard layout).
- **Lowered `creativity` + high `layout_structure`:** restrained color and typography paired with adventurous grid composition (e.g., Swiss international or architectural grids).
- **High `immersivity` + lowered `creativity`:** understated styling carrying a full scroll-driven product sequence.
- **High `creativity` and `layout_structure` + lowered `immersivity`:** a bold, art-directed static page (when the user requests no animation).
- **Dense dashboards:** keep pinned scroll scenes out of the active workspace; put motion into view transitions, filters, and state feedback.
- **Luxury briefs:** express high scores through slower pacing, larger scale contrast, and full-bleed photography rather than extra decorative widgets.
