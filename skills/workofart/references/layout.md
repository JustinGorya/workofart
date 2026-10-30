# Layout: Section Patterns, Composition, and Pitfalls

Assign each major section a **specific layout pattern** before writing code. **Adjacent sections should never repeat the same grid skeleton**, which is the clearest visual giveaway of a templated page.

⚑ **= Pattern also tracked in `references/tells.md`.** AI models frequently use these patterns as fallback alternatives to a 3-up card grid. Use a ⚑ pattern only when (a) the project's content genuinely calls for it and (b) you customize its proportions or behavior.

---

## 1. Hero patterns

- **Centered Monument**: high-ceremony centered focal point. Requires a distinct compositional anchor (oversized typography, full-bleed photography, or a central physical object) so it does not turn into a generic centered text wall (`HERO-1`).
- **Asymmetric Product Split**: 25/75, 60/40, or 70/30 split paired with full-bleed edges, overlapping layers, vertical offset, or depth. Changing column percentages alone is not enough.
- **Editorial Masthead**: magazine-cover layout with oversized title, issue/context metadata, side column, and photography crossing grid lines.
- **Poster Hero**: single viewport-filling typographic statement where navigation, CTAs, and supporting details sit as compact peripheral elements.
- **Media-First Hero**: full-bleed photograph, video, or interactive canvas carrying the opening frame, with text anchored in a corner, rail, or overlay panel.
- **Instrument / Workspace Hero**: live interactive product surface or telemetry view right in the opening viewport.
- **Layered Depth Hero**: background photography, display typography, and foreground cutouts stacked across distinct Z-planes.
- **Diagonal / Kinetic Hero**: off-axis composition or directional flow built around movement.
- **Split Narrative Hero**: primary claim on one side paired with an interactive before/after or stepped sequence on the other.
- **Quiet Luxury Hero**: generous negative space, understated typography, and a single striking photograph.
- ⚑ **Staircase Headline (`HERO-3`)**: lines of text indented progressively across the viewport. Use only for a single headline where the rhythm fits the subject; never repeat staircase indentation across headlines, menus, blockquotes, and process steps on the same page.

## 2. Feature and listing patterns

- **Anchor Feature + Satellites**: one primary feature showcase surrounded by smaller supporting items in an asymmetric layout.
- ⚑ **Dominant Cell Bento (`GRID-3`)**: multi-cell grid where one item spans 2–4x the area of the others. Use only when one capability genuinely outranks the rest, and avoid the boilerplate `repeat(6, 1fr)` + single `span 3` formula.
- **Progressive Stack**: vertical sequence where items vary in width, horizontal offset, and media framing.
- **Tabbed Product Stage**: persistent interactive product view that updates as the user steps through accompanying descriptions.
- **Comparison Strip**: direct side-by-side or split-screen contrast (before/after, manual/automated, raw/processed).
- **Use-Case Map**: capabilities arranged spatially around a central workflow or architectural diagram.
- **Editorial Feature Essay**: narrative column with pull quotes, inline figures, and wide media breaks.
- **Capability Matrix**: structured specification table broken up by a larger visual callout.
- **Alternating Depth Panels**: sequence alternating between full-bleed imagery and focused text columns with varied alignments.
- ⚑ **Exploded Product Anatomy (`GRID-5`)**: diagram with numbered callout pins and detail descriptions. Use only when the product has real physical or architectural components to inspect.
- ⚑ **Exposed Coordinate Grid (`CHR-3`)**: visible grid hairlines and ruler ticks. Limit to a single layer when the subject is engineering, cartography, or instrumentation.
- ⚑ **Catalog Ledger + Sticky Detail Pane (`GRID-6`)**: selectable table rows that update a sticky preview pane. Use only for a real multi-item catalog or inventory, not for three generic marketing features.

## 3. Story and process patterns

- **Timeline Spine**: chronological or causal progression anchored by a prominent milestone.
- **Sticky Chapter Layout**: pinned visual or section header on one side while narrative beats scroll past on the other.
- **Annotated Article**: primary column paired with margin notes, citations, and small figures.
- **Full-Viewport Scroll Scenes**: sequential stages where each section shifts lighting, scale, and alignment.
- **Before / After Stage**: interactive scrubber, split frame, or state transition comparing two conditions.
- **Quote as Structural Anchor**: a single pivotal statement or figure scaled up as the visual centerpiece of a section.
- **Process Sequence**: connected steps laid out with directional flow across the viewport.
- **Case-Study Mosaic**: asymmetric layout combining project title, photography, outcome metrics, and client quote.
- ⚑ **Horizontal Pin-Scroll (`GRID-4`)**: vertical scroll translated into horizontal movement across a wide stage. Use only when the content is a continuous panorama, timeline, or transforming subject; do not use it just to slide three feature cards sideways.

## 4. Pricing, Social Proof, CTAs, and App Views

- **Pricing:** Featured Plan Landmark (one primary offer paired with compact secondary tiers), Comparison Table + Context Rail, Tier Ladder, Interactive Price Calculator, or Editorial Pricing (prose explanation + single clear rate).
- **Social proof:** Hero Case Study + Evidence, Varied-Scale Quote Wall, Customer Story Strip (context -> problem -> metric -> quote), Logo Integration, Before/After Proof, or ⚑ Full-Bleed Quote Interlude (`END-3`, used only when a narrative pause is earned).
- **Closing / CTA:** Poster CTA, Product-in-Hand CTA, Asymmetric Two-Path Choice, Quiet Invitation, Immediate-Value Checklist, or Final Scene Resolution.
- **Application / dashboard views:** Command Center, Canvas + Inspector Rail, Triage Inbox + Detail Pane, Map-First Workspace, Telemetry Cockpit, or Focused Document Shell.

## 5. Compositional techniques

Use full-viewport frames, overlapping section transitions, sticky layers, poster-scale typography, masked image windows, full-bleed photography, deliberate negative space, and varied section density. Let the content dictate the page order: a band's website can open directly with tour dates and audio; a charity can open with the active campaign; a restaurant can put the menu and hours up front. You do not have to follow `nav -> hero -> about -> 3-up cards -> CTA -> footer`.

---

## 6. Layout pitfalls by lever band

Unless the user explicitly requested a conventional template (`layout_structure <= 20`), avoid these boilerplate section layouts:

**At `layout_structure >= 25`, avoid:**
- **Hero:** vertically centered 50/50 text-left / image-right splits with no overlap, bleed, or scale contrast; centered headline + subtitle + 2 pill buttons above 3 equal cards.
- **Features:** 3-up or 4-up equal-width cards with identical icon + heading + paragraph stacks; uniform 2x3 card grids.
- **Contact:** symmetric left-info / right-form columns centered in a standard container; plain centered form card on a flat background.
- **Pricing:** three identical vertical cards with the middle card scaled up or badged "Most Popular".
- **Social proof:** 3 equal avatar + quote cards in a row; uniform 4- or 6-column grayscale logo grids.
- **Overall page:** repeating equal-height, equal-padding centered containers down the entire document.

**At `layout_structure >= 41`, also avoid:**
- **FAQ:** a bare centered stack of identical accordion bars with no supporting structure.
- **Footer:** 4 equal link columns above a copyright bar (`END-1`).

**At `layout_structure >= 50`, also avoid:**
- `Hero -> features -> testimonials -> CTA` where every section shares the same container width and vertical padding.
- Unbroken 12-column grids where no image or heading ever crosses a boundary.

**Flagged (⚑) pattern limit:** if two or more ⚑ patterns appear on the same page without direct content justification, the layout has slipped into the `editorial heritage` or `atelier-ledger` template (`META-1`).

---

## 7. Adjusting familiar layouts (`layout_structure 1–24`)

When the user asks for a calm or traditional layout (`1–24`), familiar structures are appropriate. Give each section one deliberate compositional detail so it still feels considered: shift the column ratio (`65/35` or `75/25`), bleed an image to the viewport edge, overlap a caption across a photo boundary, offset two columns vertically, or leave one column intentionally open.

## 8. Scene composition at default (`layout_structure 75–92`)

At the default band, treat the page as a sequence of composed frames rather than stacked blocks:
- Open with a full-viewport frame that establishes the visual world.
- Compose each section with deliberate depth, overlap, full-bleed media, or scale contrast.
- Connect adjacent sections so an element, crop, or axis from one frame leads into the next.
- Include 2+ pinned scroll stages built around a changing subject.
- End with a stable closing frame where the user can act on the CTA without distraction.

Keep complex layouts readable by:
1. Running **one coherent spatial idea** through the page rather than mixing five unrelated layout tricks.
2. **Alternating density** (following a dense, layered stage with an open, quiet frame).
3. **Keeping body copy on a stable, high-contrast plane** with comfortable line lengths (`45–58ch`) and a clear reading order.
