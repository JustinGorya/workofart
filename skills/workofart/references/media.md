# Media, Interaction, and Inclusive Design

## 1. Photography first

Visual media is a primary structural element of a page. **For marketing, brand, editorial, and product sites, real photography is the default, and every design contract specifies it.**

- For every section that contains imagery, specify **subject + mood + crop** at minimum (for example: *"weathered fishing boats at dawn, side profile, low contrast"*, *"ceramicist's hands at the wheel, warm side window light, tight crop"*, *"aerial view of a concrete plaza, hard midday shadows"*, *"macro shot of espresso extraction, shallow depth of field"*).
- Do not leave imagery vague ("uses photography"), do not use gray placeholder boxes, and do not substitute CSS gradients or abstract SVG shapes just because the prompt was brief.
- **This rule holds at every `creativity` score.** High `creativity` adds art direction to photography (crops, lighting, duotone, collage, masking). Cyberpunk uses neon street photography; vaporwave uses retro video/print imagery; art deco uses architectural photography; brutalism uses raw physical photography. CSS lighting and texture layer over the photograph rather than replacing it.
- CSS gradient `.thumb-1` divs and pseudo-element illustrations are `IMG-1` tells.
- **Do not pin museum-style caption plates onto every photograph (`CHR-5`).** Add captions only when the image genuinely requires context.

## 2. When to use photography

Landing pages, marketing sites, portfolios, agencies, case studies, editorial publications, blogs, hospitality, travel, fashion, culture, architecture, retail, consumer apps, and most SaaS/B2B sites (people, hardware, workspaces, customer stories).

## 3. When CSS or SVG abstraction is appropriate

Use pure CSS, SVG, or canvas visuals without photography only in these cases:
- Dashboards and data visualization where the chart or metric view is the primary content.
- Technical schematics, system architecture diagrams, and flowcharts.
- Icon sets and small UI glyphs.
- Privacy-sensitive interfaces (medical records, banking portals, encrypted messaging).
- Offline-first tools or strict Content Security Policy (CSP) environments that block external image hosts.
- The user explicitly asks for an abstract, typographic-only, or image-free design.

**High `creativity` is not an exception.** Do not replace photography with abstract gradients simply because the `creativity` score is high.

## 4. Media types and treatments

- **Media types:** real product UI screenshots, editorial photography, lifestyle photography, architectural/location photography, studio product shots, portraits, macro detail shots, aerial/landscape photography, archival imagery, 3D renders (when appropriate to the product), technical diagrams, data visualizations, editorial illustrations, and mixed-media collage.
- **Treatments:** film grain, duotone, cutout subjects, monochrome, editorial crops, diagrammatic overlays, and physical material framing.
- **Icons:** line, solid, duotone, 3D, pixel, technical glyph, or hand-drawn. Keep one consistent icon style across the page.

## 5. Unsplash URL format and reliable photo IDs

When the user does not supply local image assets, use Unsplash URLs:

```text
https://images.unsplash.com/photo-<id>?w=<width>&q=80&auto=format&fit=crop
```

Recommended widths: hero `w=1600`, cards `w=800`, thumbnails `w=400`. For fixed aspect ratios, append `&h=<height>&crop=center`.

**Verified Unsplash photo IDs by category:**
- *Architecture and interiors:* `photo-1487958449943-2429e8be8625`, `photo-1545324418-cc1a3fa10c00`, `photo-1600585154340-be6161a56a0c`, `photo-1556909114-f6e7ad7d3136`
- *People and portraits:* `photo-1494790108377-be9c29b29330`, `photo-1507003211169-0a1dd7228f2d`, `photo-1573496359142-b8d87734a5a2`, `photo-1488161628813-04466f872be2`
- *Nature and landscapes:* `photo-1506905925346-21bda4d32df4`, `photo-1469474968028-56623f02e42e`, `photo-1418065460487-3e41a6c84dc5`, `photo-1441974231531-c6227db76b6e`
- *Food and hospitality:* `photo-1414235077428-338989a2e8c0`, `photo-1517248135467-4c7edcad34c4`, `photo-1555396273-367ea4eb4db5`
- *Technology and hardware:* `photo-1518770660439-4636190af475`, `photo-1620712943543-bcc4688e7485`
- *Fashion and objects:* `photo-1485518882345-15568b007407`, `photo-1542291026-7eec264c27ff`, `photo-1523275335684-37898b6baf30`

Always set explicit `width`/`height` or CSS `aspect-ratio`, write descriptive `alt` text (or `alt=""` for purely decorative images), and give the image wrapper a solid background color from the palette so layout stability holds if an external image fails to load.

---

## 6. Interactive UI states

For web applications, forms, filters, dashboards, onboarding flows, and checkout screens:

- **Core qualities:** immediate state feedback, predictable behavior, easy undo/recovery, low friction, helpful empty states, and visually distinct `hover`, `:focus-visible`, `:active`, `selected`, `:disabled`, `loading`, `error`, and `success` states.
- **Common patterns:** inline editing, stepped forms, live filter/sort, command palettes, contextual action bars, guided empty states, confirmation on destructive actions, non-blocking toasts, and mobile bottom sheets.

## 7. Accessibility checklist

- Text contrast meets WCAG AA (`4.5:1` for normal text, `3:1` for large text), and state changes never rely on color alone.
- Font sizes and line lengths remain comfortable to read across viewports.
- Interactive targets are at least `44x44px` with clearly visible `:focus-visible` states.
- Scroll and ambient motion respect `prefers-reduced-motion` (`references/motion.md` §6).
- DOM order matches visual reading order; form inputs have explicit `<label>` elements and clear error messages.
- Call out contrast or readability trade-offs whenever a direction uses glassmorphism, neumorphism, low-contrast palettes, cyberpunk glow, or dense overlapping layouts.
