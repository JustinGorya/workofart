#!/usr/bin/env python3
"""workofart scan: search a site's CSS, markup, and scripts for AI-skeleton tells.

Reports candidate matches keyed to the tell IDs in references/tells.md. A match
is a byte pattern to inspect in context, not an automatic failure.

Usage:
    python scripts/scan.py <file-or-dir> [...] [--all] [--json] [--max N]

Python 3.10+, standard library only. Exit code is 0 unless arguments are invalid.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from dataclasses import dataclass

EXTENSIONS = {
    ".css", ".scss", ".sass", ".less", ".html", ".htm", ".js", ".mjs", ".cjs",
    ".ts", ".jsx", ".tsx", ".vue", ".svelte", ".astro",
}
SKIP_DIRS = {"node_modules", ".git", ".next", ".nuxt", ".svelte-kit", "dist", "build", ".cache", "coverage"}
MAX_FILE_BYTES = 2_000_000

GENERATIONS = ("template", "paper-ink", "heritage", "atelier")

SLOTS = {
    "PAL": "Palette", "TOK": "Token layer", "TYP": "Typography", "RHY": "Rhythm & measure",
    "BASE": "Base layer (mostly keep)", "SRF": "Surface & texture", "EDGE": "Radius & borders",
    "NAV": "Navigation", "HERO": "Hero", "GRID": "Listing & grid", "HOV": "Hover grammar",
    "MOT": "Reveal & easing", "CHR": "Chrome & labels", "LIVE": "Liveness flourish",
    "IMG": "Imagery", "END": "Footer & closers", "META": "Convergence & confession",
}


@dataclass(frozen=True)
class Rule:
    tell: str
    sev: str            # H / M / L
    gens: str           # e.g. "template", "paper-ink+heritage+atelier", "all"
    label: str
    pattern: re.Pattern


def r(tell: str, sev: str, gens: str, label: str, pattern: str, flags: int = re.I) -> Rule:
    return Rule(tell, sev, gens, label, re.compile(pattern, flags))


LINE_RULES: list[Rule] = [
    # Palette
    r("PAL-1", "H", "template", "amber-on-cream light reflex bytes", r"#(?:f6f8fb|ff6b35)\b"),
    r("PAL-2", "H", "template", "black + gold dark reflex", r"#c8a45c\b|--(?:void|gold)\s*:"),
    r("PAL-3", "H", "heritage+atelier", "heritage palette bytes (bone/racing/brass or chalk/ink/oxblood)",
      r"#(?:e9e2d1|1e3a2f|a9814a|eceae4|f5f3ee|191a1c|6d3239)\b|rgba\(\s*25\s*,\s*26\s*,\s*28\s*,\s*0?\.16\s*\)"),
    r("PAL-5", "M", "template+paper-ink", "::selection accent recipe", r"::selection"),
    # Tokens
    r("TOK-1", "H", "template", "generic :root buckets (--bg/--surface/--accent/--muted)", r"--(?:bg|surface|accent|muted)\s*:"),
    r("TOK-2", "H", "template", "--radius:16px / generic --ease token", r"--radius\s*:\s*16px|--ease\s*:\s*cubic-bezier"),
    r("TOK-3", "H", "paper-ink", "--paper/--ink name collapse", r"--(?:paper|ink)(?:-soft|-faint)?\s*:"),
    r("TOK-4", "M", "paper-ink", "--rule hairline token", r"--rule\s*:"),
    r("TOK-6", "H", "heritage", "heritage naturals (--bone/--racing/--brass/--soot/--haze)", r"--(?:bone|racing|brass|soot|haze)\s*:"),
    r("TOK-7", "H", "atelier", "atelier Tailwind naturals (chalk/linen/graphite/mist/oxblood/hairline)",
      r"\b(?:chalk|linen|graphite|mist|oxblood|hairline)\s*:\s*['\"](?:#|rgba)"),
    # Typography
    r("TYP-1", "M", "template", "system font stack", r"system-ui\s*,\s*-apple-system"),
    r("TYP-2", "H", "paper-ink", "Google Fonts dependency / reflex font pool", r"fonts\.googleapis\.com"),
    r("TYP-2", "H", "paper-ink", "Google Fonts dependency / reflex font pool",
      r"Space[+ ]Mono|Space[+ ]Grotesk|\bOswald\b|IBM[+ ]Plex[+ ]Mono|Fragment[+ ]Mono|\bInter\b(?=[:'\"+,&\s])"),
    r("TYP-4", "H", "heritage", "Fraunces / optical-sizing prestige serif", r"\bFraunces\b|font-optical-sizing\s*:\s*auto"),
    r("TYP-5", "H", "atelier", "width-axis split / hand-tuned weights",
      r"font-stretch\s*:\s*125%|\bw(?:410|560)\b|font-weight\s*:\s*410\b|ital,wdth,wght"),
    r("TYP-6", "M", "atelier", "half-pixel font-size ladder", r"text-\[\d+\.5px\]|font-size\s*:\s*\d+\.5px"),
    r("TYP-7", "H", "heritage+atelier", "prestige serif face (count its component roles)",
      r"Playfair|Cormorant|EB[+ ]Garamond|Instrument[+ ]Serif|Libre[+ ]Caslon|\bMarcellus\b|DM[+ ]Serif"),
    r("TYP-8", "M", "template+paper-ink", "universal body line-height 1.6", r"line-height\s*:\s*1\.6\s*(?:;|}|!)"),
    # Rhythm
    r("RHY-2", "M", "all", "cohort clamp() anchor",
      r"\b11vw\b|clamp\(\s*20px\s*,\s*[45]vw|clamp\(\s*1\.25rem\s*,\s*4vw\s*,\s*4\.5rem\s*\)|clamp\(\s*5rem\s*,\s*10vw\s*,\s*10rem\s*\)|clamp\(\s*1\.9rem\s*,\s*4\.3vw"),
    r("RHY-2", "M", "atelier", "Tailwind clamp() gutter/pad chanted through sections", r"p[xy]-\[clamp\("),
    r("RHY-3", "M", "template+paper-ink", "--maxw-style cap in the 1140–1249px band",
      r"--(?:maxw|max-w|measure|sheet|app-max|container)\s*:\s*1(?:1[4-9]\d|2[0-4]\d)px"),
    # Base
    r("BASE-3", "M", "all", "reduced-motion blanket (!important nuke)", r"animation(?:-duration)?\s*:\s*(?:none|0\.?0*1?m?s)\s*!important"),
    r("BASE-5", "L", "template", "canned breakpoint cascade width", r"max-width\s*:\s*(?:960|980|760|768|820|860|560|600|640)px"),
    # Surface
    r("SRF-1", "H", "paper-ink", "fixed full-page overlay pseudo-element", r"body::?(?:before|after)"),
    r("SRF-2", "H", "paper-ink", "canned feTurbulence grain", r"feTurbulence|fractalNoise"),
    r("SRF-4", "M", "template", "soft glow shadow 0 18px 50px", r"0\s+18px\s+50px"),
    r("SRF-5", "M", "paper-ink", "hard offset brick shadow",
      r"box-shadow\s*:\s*\d+px\s+\d+px\s+0(?:px)?\s+(?:var\(--ink\)|#000\b|black)"),
    r("SRF-6", "M", "template", "gradient-clipped text", r"background-clip\s*:\s*text|text-fill-color\s*:\s*transparent"),
    r("SRF-7", "M", "paper-ink", "text-stroke headline effect", r"-webkit-text-stroke"),
    # Edge
    r("EDGE-1", "M", "template+paper-ink", "pill-pole radius", r"border-radius\s*:\s*(?:999|9999|100|44)px"),
    r("EDGE-3", "M", "template", "universal 1px var(--line) divider", r"1px\s+solid\s+var\(--(?:line|border|rule)\)"),
    r("EDGE-4", "M", "paper-ink", "universal 2px ink border", r"2px\s+solid\s+var\(--ink\)"),
    # Nav
    r("NAV-1", "H", "template", "glass nav blur 10–16px", r"backdrop-filter\s*:\s*blur\(\s*1[0-6]px"),
    r("NAV-2", "M", "template", ".scrolled toggle", r"['\"]scrolled['\"]|\.scrolled\b"),
    r("NAV-3", "H", "paper-ink+heritage", "solid sticky bar + hard ink rule", r"border-bottom\s*:\s*[2-4]px\s+solid\s+var\(--ink\)"),
    r("NAV-4", "M", "atelier", "vertical rail (writing-mode / w-[76px])", r"writing-mode\s*:\s*vertical-rl|\bw-\[76px\]"),
    # Hero
    r("HERO-1", "M", "template", "radial-gradient hero wall / 92–100vh hero",
      r"radial-gradient\(\s*circle at \d+%\s+\d+%|min-height\s*:\s*(?:9[2-9]|100)vh"),
    r("HERO-2", "M", "heritage", "mousemove pointer parallax", r"['\"]mousemove['\"]"),
    r("HERO-3", "H", "atelier", "staircase indent (pl-[Nvw])", r"\bpl-\[\d+(?:\.\d+)?vw\]"),
    # Grid
    r("GRID-1", "M", "template", "auto-fit minmax(240–300px) card grid", r"repeat\(\s*auto-fit\s*,\s*minmax\(\s*(?:2[4-9]\d|300)px"),
    r("GRID-2", "M", "paper-ink", "fixed repeat(3|4,1fr) grid", r"repeat\(\s*[34]\s*,\s*1fr\s*\)"),
    r("GRID-3", "H", "paper-ink", "6-column bento", r"repeat\(\s*6\s*,\s*1fr\s*\)"),
    r("GRID-4", "H", "heritage", "pin-scroll math (innerHeight + dist / translate3d progress)",
      r"innerHeight\s*\+\s*\w*dist|translate3d\(\s*\$\{[^}]*dist"),
    r("GRID-5", "H", "heritage", "specimen / legend markers", r"specimen|legend-key|data-key\s*="),
    r("GRID-6", "H", "atelier", "LOT ledger / data-pane", r"data-lot|data-pane|\bLOT\s0\d\b"),
    r("GRID-7", "M", "heritage", "<dl> spec sheet", r"<dl\b"),
    r("GRID-8", "M", "paper-ink", "multi-column / dotted leader", r"column-count\s*:|border-bottom\s*:\s*\d+px\s+dotted"),
    # Hover
    r("HOV-1", "M", "template", "translateY lift", r"translateY\(\s*-\s*[2-8]px\s*\)"),
    r("HOV-3", "H", "heritage", "four-verb pack (scale 1.05 / saturate .7x)", r"saturate\(\s*0?\.7\d\s*\)|scale\(\s*1\.05\s*\)"),
    r("HOV-4", "M", "heritage", "left-origin scaleX wipe", r"scaleX\(\s*0\s*\)"),
    r("HOV-5", "H", "atelier", "odometer roll (translateY(-100%) / span+span)", r"translateY\(\s*-100%\s*\)|span\s*\+\s*span"),
    # Motion
    r("MOT-1", "M", "template", "template easing cluster",
      r"cubic-bezier\(\s*0?\.22\s*,\s*(?:1|0?\.61)\s*,|cubic-bezier\(\s*0?\.2\s*,\s*0?\.8\s*,\s*0?\.25"),
    r("MOT-2", "H", "all", "canonical soft-exit tweener family",
      r"cubic-bezier\(\s*0?\.2\s*,\s*0?\.7\d?\s*,\s*0?\.2\s*,\s*1\s*\)|cubic-bezier\(\s*0?\.16\s*,\s*(?:0?\.84|1)\s*,\s*0?\.3"),
    r("MOT-4", "H", "template+paper-ink", "IntersectionObserver -8% rootMargin", r"rootMargin\s*:\s*['\"]0px 0px -8% 0px"),
    r("MOT-4", "H", "all", "IntersectionObserver reveal engine — blanket or beat-driven?", r"new\s+IntersectionObserver"),
    r("MOT-5", "H", "template+paper-ink", "entrance catalogue magnitudes", r"perspective\(\s*900px\s*\)|rotateY\(\s*80deg\s*\)"),
    r("MOT-6", "H", "all", "scroll set-piece engine (getBoundingClientRect / getTotalLength)",
      r"getTotalLength|getBoundingClientRect"),
    r("MOT-7", "M", "heritage", "--ry/--rd reveal vars / threshold .22", r"--r[yd]\b|threshold\s*:\s*0?\.22\b"),
    r("MOT-8", "M", "atelier", "[data-rv] catalogue / threshold .3", r"data-rv|threshold\s*:\s*0?\.3\b"),
    r("MOT-9", "M", "atelier", "atelier canonical easing pair",
      r"cubic-bezier\(\s*0?\.62\s*,\s*0?\.04|cubic-bezier\(\s*0?\.07\s*,\s*0?\.7\s*,"),
    # Chrome
    r("CHR-1", "M", "all", "eyebrow kicker / wide uppercase tracking",
      r"\.eyebrow\b|letter-spacing\s*:\s*0?\.[234]\d?em|tracking-\[\.(?:1[2-9]|2\d)em\]"),
    r("CHR-2", "H", "paper-ink", "field-note chrome (data-count / off-axis rotate)", r"data-count|rotate\(\s*-(?:1\.5|2|2\.5|3)deg\s*\)"),
    r("CHR-4", "H", "heritage", "§ / Roman-numeral chrome", r"§\s?[IVX]+\b|\bEst\.\s?M[CDLXVI]+\b|\bMMXX[IVX]*\b"),
    r("CHR-5", "M", "atelier", "floating spec-plate caption", r"absolute\s+-?bottom-5\s+-?(?:right|left)-5"),
    # Liveness
    r("LIVE-1", "H", "heritage", "ticker tape / innerHTML self-duplication", r"\bticker\b|innerHTML\s*\+="),
    r("LIVE-2", "H", "atelier", "rolling odometer digits", r"\.odo\b|odo-col"),
    r("LIVE-3", "H", "atelier", "live clock (Intl.DateTimeFormat / timeZone)", r"Intl\.DateTimeFormat|timeZone\s*:|data-clock"),
    r("LIVE-4", "M", "atelier", "Math.random() — check for fabricated reference IDs", r"Math\.random\(\)"),
    # Imagery
    r("IMG-1", "M", "template", "numbered gradient placeholder 'image'",
      r"\.(?:thumb|img|photo|media|cover)-?\d+\b[^{]*\{[^}]*gradient"),
    # Footer
    r("END-1", "L", "template+paper-ink", "footer 1.4/1.6fr 1fr 1fr", r"(?:1\.4|1\.6)fr\s+1fr\s+1fr"),
    r("END-2", "L", "heritage", "giant footer wordmark clamp(…17vw…)", r"clamp\(\s*3\.5rem\s*,\s*17vw"),
    r("END-3", "L", "atelier", "scrim-quote gradient bytes", r"rgba\(\s*20\s*,\s*20\s*,\s*22\s*,"),
    r("END-4", "L", "atelier", "typeface colophon", r"\bSET IN\b"),
    # Meta
    r("META-2", "H", "paper-ink", "/* NOT X */ confession", r"/\*\s*NOT\b", 0),
    r("META-3", "M", "heritage+atelier", "self-narrating comment",
      r"/\*[^*]*\b(?:not a |the one place|unlike the|instead of the|deliberately|applied sparingly|carries both voices|paints instantly|cohort)"),
]


def file_level_hits(text: str, path: str) -> list[tuple[Rule, int, str]]:
    """Checks that need the whole file rather than one line."""
    out: list[tuple[Rule, int, str]] = []

    def line_of(idx: int) -> int:
        return text.count("\n", 0, idx) + 1

    tw = re.search(r"tailwind\.config", text)
    root = re.search(r":root\s*\{[^}]*--[\w-]+\s*:\s*#", text)
    if tw and root:
        out.append((r("TOK-5", "H", "heritage", "tailwind.config AND :root colour tokens in one file (mirror?)", r""),
                    line_of(root.start()), ":root { … } alongside tailwind.config"))

    m = re.search(r"\*\s*,\s*\*::?before\s*,\s*\*::?after\s*\{[^}]*border-radius\s*:\s*0", text, re.I)
    if m:
        out.append((r("EDGE-2", "M", "paper-ink", "border-radius:0 folded into universal reset", r""),
                    line_of(m.start()), m.group(0)[:80]))

    m = re.search(r":hover\s*\{[^}]*background(?:-color)?\s*:\s*var\(--ink\)[^}]*color\s*:\s*var\(--paper\)", text, re.I)
    if m:
        out.append((r("HOV-2", "H", "paper-ink", "ink↔paper inverse-video hover", r""), line_of(m.start()), m.group(0)[:80]))

    beziers = len(re.findall(r"cubic-bezier\(", text))
    if beziers >= 3 and not re.search(r"\bease-in\b(?!-out)|\blinear\b(?!-gradient)|steps\(", text):
        out.append((r("MOT-3", "H", "all", f"{beziers} cubic-beziers, no ease-in / linear / steps anywhere", r""),
                    1, "(whole file)"))

    serif_roles = len(re.findall(r"font-serif\b|var\(--font-(?:serif|display)\)", text))
    if serif_roles >= 3:
        out.append((r("TYP-7", "H", "heritage+atelier", f"serif/display face referenced {serif_roles}× — check how many roles it owns", r""),
                    1, "(whole file)"))

    low = text.lower()
    if path.lower().endswith((".html", ".htm")) and "<body" in low and "<img" not in low and "<picture" not in low:
        out.append((r("IMG-1", "M", "template", "markup with no <img> at all", r""), 1, "(whole file)"))
    return out


def iter_files(paths: list[str]):
    for p in paths:
        if os.path.isfile(p):
            yield p
        elif os.path.isdir(p):
            for root, dirs, files in os.walk(p):
                dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
                for f in files:
                    if os.path.splitext(f)[1].lower() in EXTENSIONS:
                        yield os.path.join(root, f)
        else:
            print(f"warning: not found: {p}", file=sys.stderr)


def scan(paths: list[str]):
    hits = []  # dicts
    files = 0
    for path in iter_files(paths):
        try:
            if os.path.getsize(path) > MAX_FILE_BYTES:
                continue
            with open(path, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except OSError:
            continue
        files += 1
        for i, line in enumerate(text.splitlines(), 1):
            for rule in LINE_RULES:
                m = rule.pattern.search(line)
                if m:
                    start = max(0, m.start() - 30)
                    hits.append(dict(tell=rule.tell, sev=rule.sev, gens=rule.gens, label=rule.label,
                                     file=path, line=i, excerpt=line[start:start + 110].strip()))
        for rule, ln, excerpt in file_level_hits(text, path):
            hits.append(dict(tell=rule.tell, sev=rule.sev, gens=rule.gens, label=rule.label,
                             file=path, line=ln, excerpt=excerpt))
    return files, hits


def gen_tags(gens: str) -> set[str]:
    if gens == "all":
        return set()
    return set(gens.split("+"))


def tell_sort_key(tell: str):
    prefix, _, num = tell.partition("-")
    order = list(SLOTS)
    return (order.index(prefix) if prefix in order else 99, int(num) if num.isdigit() else 0)


def report(files: int, hits: list[dict], show_all: bool, max_per: int) -> str:
    distinct = {h["tell"]: h for h in hits}
    high = sorted(t for t, h in distinct.items() if h["sev"] == "H")
    gens = defaultdict(set)
    for t, h in distinct.items():
        for g in gen_tags(h["gens"]):
            gens[g].add(t)

    lines = [f"workofart scan — {files} file(s), {len(hits)} candidate hit(s), "
             f"{len(distinct)} distinct tell(s), {len(high)} HIGH"]
    if gens:
        lines.append("generation signal: " + " · ".join(f"{g} ×{len(gens[g])}" for g in GENERATIONS if g in gens))
    if len(distinct) >= 8 or len(high) >= 5:
        lines.append("indicative: LIKELY CARRIES THE SKELETON — confirm by reading each hit in context")
    elif distinct:
        lines.append("indicative: some tells present — read each hit; slot-defining HIGH tells matter most")
    else:
        lines.append("indicative: no byte-level tells found — still read structure, serif roles and narrative by hand")
    lines.append("")

    by_slot = defaultdict(list)
    for h in hits:
        by_slot[h["tell"].split("-")[0]].append(h)
    for slot in SLOTS:
        if slot not in by_slot:
            continue
        lines.append(f"== {slot} · {SLOTS[slot]} ==")
        per_tell = defaultdict(list)
        for h in by_slot[slot]:
            per_tell[h["tell"]].append(h)
        for tell in sorted(per_tell, key=tell_sort_key):
            group = per_tell[tell]
            h0 = group[0]
            lines.append(f"  {tell} [{h0['sev']} {h0['gens']}] {h0['label']} — {len(group)} hit(s)")
            shown = group if show_all else group[:max_per]
            for h in shown:
                lines.append(f"      {os.path.relpath(h['file'])}:{h['line']}  {h['excerpt']}")
            if len(group) > len(shown):
                lines.append(f"      … {len(group) - len(shown)} more (use --all)")
        lines.append("")
    lines.append("Each hit is a candidate. Justified by the brief → keep (no explanatory comment). "
                 "Reflex → change the slot, not the filler. See references/tells.md.")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("paths", nargs="+", help="files or directories to scan")
    ap.add_argument("--all", action="store_true", help="show every hit, not just the first few per tell")
    ap.add_argument("--max", type=int, default=3, help="hits shown per tell (default 3)")
    ap.add_argument("--json", action="store_true", help="emit JSON instead of text")
    args = ap.parse_args()

    files, hits = scan(args.paths)
    if args.json:
        print(json.dumps({"files": files, "hits": hits}, indent=2))
    else:
        out = report(files, hits, args.all, args.max)
        sys.stdout.buffer.write((out + "\n").encode("utf-8", errors="replace"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
