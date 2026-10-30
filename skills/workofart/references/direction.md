# Direction: Palette, Typography, Surfaces, Edges, and Named Styles

## 1. Palette: derive from the brief

Color sets the emotional tone and anchors the brand. Build the palette specifically for the project rather than picking from a preset list.

### 1.1 Method

- Start with **color temperature**: calm, severe, rich, playful, raw, clinical, nocturnal, nostalgic, electric, or earthy.
- Define **functional roles** before hex values: `bg`, `bg-alt`, `fg`, `fg-muted`, `accent`, `rule`, and optional `glow`.
- Use **tinted neutrals** with a clear temperature (bone, porcelain, graphite-blue, lichen gray, smoked plum, warm slate) instead of flat gray or generic beige.
- Scale saturation with the `creativity` score.
- **Give the palette a descriptive name**: e.g., "azulejo blue, lime, and bone" or "rust-iron, kiln cream, and ink".

**Tie the accent color to a concrete detail in the brief.** You should be able to state *"the accent is [hue] because [brief detail]"*:

- **Subject matter**: marine biology -> kelp green or deep teal; indie game tools -> arcade magenta or cathode green; ceramics -> celadon or iron-oxide; archives -> faded library red or oxidized brass.
- **Place**: coastal Portugal -> azulejo blue; Tokyo -> vermilion, shoji cream, and ink; Berlin club/industrial -> concrete and signal yellow; Nordic coast -> lichen and fjord blue.
- **Era**: 1960s Italian print -> primary blue and orange-red; 1990s rave -> acid lime and hot fuchsia; Victorian print -> bottle green and oxblood; 1980s tape -> magenta and cyan.
- **Material**: porcelain -> bone and ink; concrete -> graphite and signal yellow; brass -> patina green; linen -> flax and indigo; velvet -> oxblood and emerald.
- **Tone**: clinical -> signal green and ice cyan; civic -> ink blue and brick; underground -> acid yellow and magenta; pastoral -> sage and dusty rose.

Underused accents worth considering: cobalt, ultramarine, ink blue, brick, terracotta, cinnamon, mustard, ochre, chartreuse, lime, jade, emerald, kelp, sage, teal, sea-glass, fuchsia, magenta, dusty rose, plum, lavender, periwinkle, primary blue, signal yellow, butter, or a strictly monochrome palette with no accent hue.

### 1.2 Usability check

- **Cohesion:** keep one dominant color temperature and a clear contrast hierarchy.
- **Accent discipline:** use one primary accent; keep secondary accents subordinate unless the brief calls for maximalism.
- **Category fit:** SaaS, fintech, healthcare, education, and B2B sites can use bold, distinctive color schemes while still reading as credible for their domain.
- **Contrast:** meet WCAG AA contrast ratios for all text and interactive controls.

### 1.3 Palette families (reference vocabulary, not defaults)

| Family | Typical swatches |
|---|---|
| High-key editorial | Off-white, ink black, one sharp accent (avoid default amber unless justified; see PAL-1) |
| Soft industrial | Concrete, graphite, faded safety orange, pale blue |
| Organic calm | Moss, clay, oat, fog, bark |
| Clinical precision | White, ice blue, graphite, signal green |
| Civic clarity | Cream, navy, brick, muted yellow |
| Cultural magazine | Paper, ultramarine, tomato red, black |
| Frosted technical | Cool grays, arctic blue, violet shadow |
| Raw brutalist | White, black, red oxide, exposed grid rules |
| Warm minimal | Ivory, taupe, espresso, dusty rose |
| Playful utility | Pale yellow, cobalt, mint, black |
| Analog archive | Aged paper, faded ink, olive, rust |
| Marine system | Deep teal, foam, sand, buoy orange |
| Monochrome typographic | Black, white, grayscale, no color accent |
| Pastel mechanical | Powder blue, butter, lilac, machine gray |
| Acid restraint | Neutral base with one acidic lime, chartreuse, or cyan |
| Sun-bleached coastal | Sand, terracotta, sea glass, washed denim |
| Botanical apothecary | Bottle green, parchment, cinnamon, deep wine |
| Risograph print | Fluorescent pink, soft blue, butter yellow, off-white |
| Tropical modernism | Verdant green, mango, cobalt, bone |
| Desert minimalism | Bone, terracotta, sage, charcoal ink |

### 1.4 Overused AI palettes (use only when the brief demands them)

| ID | Palette | Byte signature | Justified only when |
|---|---|---|---|
| PAL-1 | **Light reflex**: off-white + ink + warm orange/amber/coral | `#f6f8fb` / `#0a0a0a` / `#ff6b35` and close variants | The brief involves fire, heat, sunset, citrus, harvest, autumn, sports, a region where orange is culturally central, or an existing brand guideline |
| PAL-2 | **Dark reflex**: deep black + gold/champagne | `--void:#0a0c0e; --gold:#c8a45c` | Nightlife, spirits, watchmaking, fine dining, or noir themes |
| PAL-3 | **Heritage reflex**: bone + racing green + brass, or chalk/linen + ink + oxblood + 16%-alpha hairline | `--bone:#E9E2D1; --racing:#1E3A2F; --brass:#A9814A` or `chalk #ECEAE4 / ink #191A1C / oxblood #6D3239 / rgba(25,26,28,.16)` | Actual heritage motoring, country estates, or bespoke tailoring/craft |
| PAL-4 | **Common startup tropes**: black + neon green/cyan, navy + cyan gradient, purple + blue gradient, gray background + white cards, dark monochrome + one neon accent | Various | The user explicitly asks for that specific look |

**Why `PAL-1`, `PAL-2`, and `PAL-3` appear so often:** Models default to `PAL-1` whenever a prompt mentions "modern", "minimal", "clean", or "SaaS"; `PAL-2` whenever it sees "premium" or "luxury"; and `PAL-3` whenever it sees "heritage", "bespoke", or "by appointment". Together they account for why generated sites look interchangeable.

**When a project calls for a dark theme without noir tropes:** use a colored dark base (deep teal, oxblood, ink blue, smoked plum, warm charcoal) paired with a non-gold highlight.

**Session diversity rule:** never give two unrelated briefs in the same session the same palette family or accent color.

### 1.5 Dark mode guidelines

Choose a dark base when the subject matter is nocturnal, theatrical, cinema-focused, or a specialized technical tool. When designing in dark mode, soften pure white text, layer surface elevations with subtle luminance steps, adjust accent saturation to prevent halation, and use directional lighting rather than simply inverting a light scheme.

---

## 2. Typography: match the content and task

Typography establishes hierarchy, voice, and reading rhythm. Avoid both common AI reflexes: defaulting to generic `Inter`/`Roboto`/system stacks, or defaulting to a high-contrast editorial serif (`Fraunces`, `Playfair`, `Cormorant`, `Instrument Serif`) with a single italicized word in the hero headline.

- **Use 2–3 font families at most**, with clear role separation between display headings, body copy, and UI labels/data. A single variable superfamily can also work well as long as splitting `font-stretch: 125%` vs. `100%` isn't used as a canned formula (`TYP-5`).
- Create headline character through proportion, weight, width, tracking, case, alignment, and scale rather than relying solely on decorative serifs.
- **Give uppercase, letter-spacing, weight, width, and italics a specific job in the hierarchy.** Do not scatter wide-tracked uppercase eyebrows above every heading (`CHR-1`).
- Ensure body and UI fonts remain legible at small sizes and support the required languages, diacritics, and tabular numerals.

### 2.1 Selecting font categories

Pick display and body font categories based on **at least two concrete factors** from the brief: product and task, audience expectations, tone of voice, information density, language/script requirements, cultural or historical context, or existing brand guidelines.

State the rationale as **"[category] because [brief evidence]"** and note two alternative categories that were ruled out.

### 2.2 Font category reference

| Category | Typical qualities |
|---|---|
| Neo-grotesk sans | Controlled, neutral, institutional |
| Warm / quirky grotesk | Direct, independent, approachable without looking childish |
| Geometric sans | Constructed, architectural, modernist |
| Humanist sans | Open counters, legible at small sizes, civic |
| Industrial grotesk | Engineered, compact, utilitarian |
| Extended sans | Wide stance, cinematic, horizontal emphasis |
| Condensed sans | Compact, urgent, poster-ready |
| Low-contrast text serif | Grounded, bookish, built for long reading |
| High-contrast display serif / Didone | Ceremonial, fashion, literary (**high AI-tell risk when overused**) |
| Soft contemporary serif | Warm, editorial, tactile |
| Slab serif | Sturdy, archival, mechanical |
| Monospace / mono hybrid | Technical, tabular, code and data oriented |
| Rounded sans | Friendly, approachable, consumer-facing |
| Variable-width superfamily | Systematic (**watch for `TYP-5` width-split formula**) |

Do not assume "serif = luxury" and "sans = tech." A disciplined grotesk or humanist sans can read as far more refined than an overused Didone serif.

### 2.3 Scaling with `creativity`

- **1–30:** task-focused, moderate scale contrast; system fonts are fine when pure utility calls for them.
- **31–70:** distinct character through font choice, weight contrast, optical sizing, and rhythm.
- **71–100:** dramatic scale contrast (`14px -> 18px -> 72px+`), expressive pairings, variable font axes, and scroll-linked typographic choreography.

### 2.4 Typographic roles

Assign clear families and styles to: **Display**, **Heading**, **Body**, **Label / UI**, **Caption**, and **Data / Monospace**. Use a real display scale on marketing pages rather than capping headings at `24px`, while keeping dense application screens compact.

### 2.5 Display serif rules and role budget (`TYP-4`, `TYP-7`)

Use a high-contrast display serif or mixed roman/italic hero headline only when the brief points to publishing, literature, fashion, fragrance, art/culture, hospitality, ceremony, historical archives, or an existing serif brand identity. Do not reach for `Fraunces` or `Instrument Serif` just because a brief says "agency", "portfolio", or "premium."

- **One-role limit:** a display serif should occupy **at most one role** (either major headlines *or* pull-quotes), while navigation, body text, buttons, and labels use their own voices. Setting three or more component roles in a display serif triggers `TYP-7` regardless of which serif family is chosen. (Exception: a low-contrast text serif used for long-form body copy on a publishing site.)
- **Semantic italics:** use italics for titles, quotations, foreign words, live readings, or genuine contrast of voice. Avoid italicizing a random adjective or verb in the hero headline for decoration.
- **System-wide legibility:** verify that the chosen fonts work across navigation, body copy, numbers, buttons, forms, and mobile viewports.

### 2.6 Overused Google Fonts pool (`TYP-2`)

Generated sites repeatedly pull from the same small set of Google Fonts: **`Inter`, `Space Grotesk`, `Space Mono`, `Oswald`, `IBM Plex Mono`, `Fragment Mono`, `Archivo`, `Fraunces`, `Playfair Display`, `Cormorant`, `EB Garamond`, `Instrument Serif`, `DM Serif Display`**. None of these are forbidden, but if you use one, state why it fits the project better than less-common alternatives.

---

## 3. Surfaces and textures

Surface options include: film grain, mesh gradients, paper tooth, brushed metal, frosted glass blur, ambient light falloff, crisp hairline rules, offset shadows, halftone/risograph patterns, vignettes, and iridescent highlights.

**Limit `backdrop-filter` and `feTurbulence` noise.** Frosted glass nav bars (`NAV-1`) and full-screen `feTurbulence` overlays (`SRF-1`, `SRF-2`) are two of the most common AI tells. Use at most one blur surface or texture layer where it directly supports the visual concept, and vary box-shadows by elevation (`SRF-3`).

---

## 4. Edge and border-radius policy

Decide how corners, borders, dividers, and masks work across the interface rather than rounding every box to `16px` or setting `* { border-radius: 0 }`.

**Available edge treatments:** sharp `0px` rectangles, subtle `2–6px` radii, mixed-radius hierarchy, chamfered/cut corners (`clip-path`), circular/pill tags, asymmetric corners (rounding only one or two corners of a frame), inset wells, stepped corners, ticket notches, or folder tabs.

### Radius tiers

| Radius | Typical fit | Pitfall to avoid |
|---|---|---|
| `0px` | Editorial, industrial, Swiss grids, brutalist, dense data tools | Applying `* { border-radius: 0 }` globally as a reflex (`EDGE-2`) |
| `2–6px` | Professional product UI, fintech, developer tools, B2B | Solid default for technical and commercial interfaces |
| `8–12px` | Consumer SaaS, education, healthcare | Pair with crisp borders so cards don't look mushy |
| `16–24px` | Wellness, lifestyle, playful consumer apps | High AI-template risk when combined with soft shadows on every card (`EDGE-1`) |
| `999px` (pill) | Status badges, filter chips, segmented controls, or a single primary CTA | Never make every card, input, and image a pill |
| Asymmetric / chamfered | Art-directed layouts, hardware/industrial UI, editorial framing | Use consistently across a defined component tier |

**Guidelines:**
- Assign different radius values to cards, buttons, images, inputs, and badges.
- For professional, B2B, fintech, technical, or editorial briefs, default to `0–6px` structural radii rather than `16px+` rounded cards.
- Never pair `16px+` radius + soft drop shadow + white cards + light gray page background unless the user specifically asks for a standard SaaS template.
- Avoid both extremes: all-pill and all-zero-radius are two versions of the same uniformity (`EDGE-1`, `EDGE-2`).
- Use border widths for hierarchy (`1px` subtle dividers, `2px` structural frames, `4px` emphasis) rather than a single global `1px` border (`EDGE-3`, `EDGE-4`).

---

## 5. Style vocabulary

Use a named style when the brief clearly calls for it or the user asks for it by name; otherwise coin a specific 2–4 word direction for the project.

| Style | Core characteristics | Native lever profile (creativity / layout / immersivity) |
|---|---|---|
| Minimalism | Generous whitespace, strict reduction, typographic focus | low / low–mid / low |
| Scandinavian | Warm natural materials, soft daylight, understated typography | low–mid / low / low |
| Swiss / International | Mathematical grid, asymmetric balance, objective photography | mid / mid–high / low |
| Bauhaus | Primary colors, geometric primitives, exposed structure | mid / mid / low–mid |
| Neumorphism | Soft extruded plastic/clay surfaces, subtle dual shadows | mid / low / low |
| Glassmorphism | Translucent frosted planes over vivid backgrounds | mid / mid / mid |
| Editorial / Magazine | Print column hierarchy, pull quotes, dramatic crop changes | mid / high / low–mid |
| Brutalism | Exposed hairlines, raw materials, high-contrast typography | high / mid–high / low–mid |
| Neo-Brutalism | Thick black outlines, flat bright fills, hard offset shadows | high / mid / mid |
| Deconstructivism | Fragmented planes, angled axes, overlapping layers | high / high / mid |
| Constructivism | Diagonal composition, stark red/black/paper contrast | mid–high / high / low–mid |
| Art Deco | Stepped geometry, metallic rules, symmetrical framing | high / mid–high / mid |
| Art Nouveau | Botanical curves, earthen tones, ornate framing | mid–high / mid / low–mid |
| Memphis | Geometric squiggles, terrazzo patterns, clashing primaries | high / mid / mid |
| Pop Art | Halftone dots, bold ink outlines, saturated primaries | high / mid / mid |
| Cyberpunk | High-density HUD overlays, neon accents, dark industrial base | very high / high / high |
| Vaporwave | Early-digital gradients, grid horizons, surreal collage | very high / mid–high / mid–high |
| Y2K / Frutiger Aero | Translucent gloss, chrome highlights, rounded hardware shapes | high / mid / mid–high |
| Space Age | Orbital curves, instrument dials, anodized metal | mid–high / mid / mid–high |
| Futurism | Speed lines, kinetic typography, diagonal momentum | high / high / high |
| Grunge | Distressed textures, torn edges, photocopied grain | high / mid / mid |
| Dark Mode Luxe | Deep dark surfaces with restrained metallic accents (see `PAL-2`) | mid–high / mid–high / mid |
| Retro / Archival | Aged paper stock, period-accurate typography, catalog rules | mid / mid / low–mid |
| Organic / Natural | Earth pigments, botanical photography, soft masks | mid / mid / low–mid |
| Corporate / Enterprise | High clarity, predictable navigation, conservative palette | low / low / low |
| Playful / Toy | Tactile volume, bright primaries, spring-physics interactions | mid–high / mid / mid–high |
| Skeuomorphism | Physical switches, stitched leather, brushed aluminum, dials | mid–high / low–mid / low–mid |
| Claymorphism | Inflated 3D pastel forms, soft inner shadows | mid / low–mid / low–mid |
| Japanese Minimalism | Intentional emptiness, quiet asymmetry, natural textures | low–mid / mid / low |
| Wabi-Sabi | Imperfect textures, weathered tones, unpolished surfaces | mid / mid / low |
| High-Contrast Graphic | Poster-scale typography, stark color blocking | high / high / low–mid |
| Data-Dense Analytical | High-information tables, compact filters, scannable hierarchy | low–mid / low–mid / low |
| Command Center | Multi-pane live status displays, telemetry readouts | mid / mid / low–mid |
| Monochrome Editorial | Single-hue palette, strong typographic scale, dramatic photos | mid / high / low |
| Low-Fi / Indie Web | Hand-crafted HTML feel, personal voice, compact layout | mid / low–mid / low |
| Luxury Tech | Precision machining, subtle lighting, high-contrast product shots | mid–high / mid–high / mid |
| Military / Tactical | Olive/steel tones, stencil markings, modular spec panels | mid / high / low |
| Medical / Clinical | Clean white/ice-blue surfaces, high legibility, calm hierarchy | low / low–mid / low |
| Publishing / Bookish | Long-form serif text, generous margins, footnote rails | low–mid / mid / low |

When operating in the cinematic default band, even quiet styles (such as Swiss International or Japanese Minimalism) are staged as full-viewport scenes and deliberate transitions unless the user asks for a static page.

### Combining styles

When blending two directions, assign each system a clear role:

| Combination | Spatial structure | Surfaces & palette | Motion style |
|---|---|---|---|
| Swiss + Luxury | Strict asymmetric grid | Warm natural materials and restrained contrast | Slow, exact transitions |
| Bauhaus + Neo-Brutalism | Modular geometric blocks | Thick borders and saturated flat fills | Snappy, direct cuts |
| Glassmorphism + Luxury Tech | Layered product stage | Frosted panels with subtle directional light | Smooth camera depth |
| Japanese Minimalism + Wabi-Sabi | Quiet asymmetric spacing | Matte, weathered textures | Sparse, unhurried holds |
| Cyberpunk + Command Center | Dense multi-pane layout | High-contrast telemetry on dark slate | Crisp state updates |
| Editorial + Monochrome | Magazine column hierarchy | Single-hue tonal range | Staged chapter transitions |
