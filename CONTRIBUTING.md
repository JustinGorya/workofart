# Contributing

The installable package is `skills/workofart/`. Keep its instructions, references, scanner, and license self-contained: installing it must not require files from the repository's `docs/`, `tools/`, or `tests/` directories.

## Local checks

Use Python 3.10+ and Node.js 22.20+ for the install smoke test:

```bash
python -m pip install -r requirements-dev.txt
python tools/validate.py
python -m unittest discover -s tests -v
npx skills add ./skills --list
```

To test installation, run the following from a temporary project directory and pass an absolute path to this checkout. Replace `<target>` with any `--agent` value the skills CLI accepts (it lists them when you leave out `--agent`). CI uses one fixed target in `.github/workflows/validate.yml`. This creates a project-local install; do not use `-g` for tests.

```bash
npx skills add /absolute/path/to/workofart --skill workofart --agent <target> --copy -y
```

The skill must work anywhere skills are supported, including environments that cannot run code. Keep every mode usable from the Markdown alone; the scanner is an accelerator, not a requirement.

Run the installed `scripts/scan.py` against a fixture or site outside the skill directory. Changes to package paths should be tested through the real CLI as well as the local checks.

## Adding an AI tell

Add the finding to `skills/workofart/references/tells.md` and implement an appropriate candidate check in `skills/workofart/scripts/scan.py`. Include:

1. A reproducible byte or markup pattern and its structural slot.
2. When the pattern is justified by a brief, and when it acts as a recurring default.
3. A practical fix that changes the design decision rather than swapping one default for another.
4. A regression test using a small source fixture.

Update documented counts when the index changes. The scanner reports candidates for contextual review; a byte match alone does not establish that a design is generated or inappropriate. Preserve baseline accessibility, focus states, and reduced-motion support.

## Media and releases

README images live in `docs/assets/` and are not installed with the skill. The skill ZIP, large videos, campaign exports, and optional production sources belong in GitHub release assets. Rebuild `workofart.zip` whenever the skill changes. It must hold a single top-level `workofart/` folder; from the repository root, this writes it to the ignored `.local/` directory:

```bash
python -c "import shutil; shutil.make_archive('.local/workofart', 'zip', 'skills', 'workofart')"
```

Keep the package free of credentials, machine-specific paths, generated frames, and third-party runtime dependencies. The package validator, scanner tests, and actual CLI install smoke test run in GitHub Actions.

## Directory listing

skills.sh discovers skills in the standard `skills/<name>/SKILL.md` layout. Its [FAQ](https://skills.sh/docs/faq) describes automatic listing through CLI installations; listing and ranking are up to skills.sh. No npm publication or extra discovery manifest is needed for this repository layout.
