"""Validate the installable package and local documentation links.

Contributor dependency: python -m pip install -r requirements-dev.txt
"""
from __future__ import annotations

import ast
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "workofart"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate() -> tuple[int, int]:
    entry = SKILL / "SKILL.md"
    discovered = list((ROOT / "skills").rglob("SKILL.md"))
    require(discovered == [entry], "Expected exactly one discoverable skill")
    require(not (ROOT / "SKILL.md").exists(), "Root SKILL.md would shadow the packaged skill")
    text = entry.read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    require(match is not None, "Missing YAML frontmatter")
    meta = yaml.safe_load(match.group(1))
    require(isinstance(meta, dict), "Frontmatter must be a YAML mapping")
    name = meta.get("name", "")
    require(isinstance(name, str) and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) is not None,
            "Invalid skill name")
    require(name == SKILL.name and len(name) <= 64, "Skill name must match its directory")
    desc = meta.get("description", "")
    require(isinstance(desc, str) and 0 < len(desc.strip()) <= 1024, "Invalid discovery description")
    require(meta.get("license") == "MIT", "Missing package license metadata")
    require((SKILL / "LICENSE").read_bytes() == (ROOT / "LICENSE").read_bytes(),
            "Installed package must include the repository license")
    require(len(text.splitlines()) < 500, "Entrypoint too long; move detail into references")
    files = [p for p in SKILL.rglob("*") if p.is_file() and "__pycache__" not in p.parts]
    size = sum(p.stat().st_size for p in files)
    require(size < 300_000, "Skill package exceeds its 300 KB source budget")
    for path in files:
        rel = path.relative_to(SKILL)
        require(not path.is_symlink(), f"Package must not depend on symlinks: {rel}")
        require(rel.as_posix() in {"SKILL.md", "LICENSE"}
                or (rel.parts[0] == "references" and path.suffix == ".md")
                or (rel.parts[0] == "scripts" and path.suffix == ".py"),
                f"Non-runtime file in installed package: {rel}")
        content = path.read_text(encoding="utf-8")
        for ref in re.findall(r"`((?:references|scripts)/[\w./-]+\.(?:md|py))`", content):
            require((SKILL / ref).is_file(), f"Broken skill resource path in {rel}: {ref}")
        require(not re.search(r"(?:file:///|[A-Za-z]:[/\\])Users[/\\]", content),
                f"Machine-specific path in {rel}")
        if path.suffix == ".py":
            ast.parse(content, filename=str(path))

    docs = [ROOT / "README.md", ROOT / "CONTRIBUTING.md", *list((ROOT / "docs").rglob("*.md"))]
    for doc in docs:
        content = doc.read_text(encoding="utf-8")
        targets = re.findall(r"\]\(([^)]+)\)", content) + re.findall(r'\bsrc="([^"]+)"', content)
        for target in targets:
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            path = (doc.parent / unquote(url.path)).resolve()
            require(path.is_relative_to(ROOT) and path.exists(),
                    f"Broken documentation link in {doc.relative_to(ROOT)}: {target}")
    return len(files), size


if __name__ == "__main__":
    try:
        count, size = validate()
    except (ValueError, OSError, SyntaxError, yaml.YAMLError) as exc:
        raise SystemExit(f"Validation failed: {exc}") from exc
    print(f"Valid: one skill, {count} runtime files, {size:,} bytes; local resource and documentation links resolve.")
