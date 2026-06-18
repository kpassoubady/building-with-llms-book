Update `CHANGELOG.md` after making changes to the bookbuilder project.

Follow the [Keep a Changelog](https://keepachangelog.com) format.

## Steps

1. **Identify what changed** — review `git diff` or `git log` to note the specific changes.

2. **Open `CHANGELOG.md`** and add entries under the `[Unreleased]` section using the appropriate category:

| Category | Use for |
|---|---|
| `### Added` | New features |
| `### Changed` | Changes in existing functionality |
| `### Deprecated` | Soon-to-be removed features |
| `### Removed` | Removed features |
| `### Fixed` | Bug fixes |
| `### Security` | Vulnerability fixes |

## Entry guidelines

- One line per change, present tense ("Add", "Fix", "Update")
- Reference the specific module or function when helpful
- Replace `N/A` placeholder with real entries; remove empty categories

## Example

```markdown
## [Unreleased]

### Added
- EPUB generation with Pandoc integration (`formats.py`)
- GFM preprocessing for admonitions, blockquote lists, and titled lists (`gfm.py`)

### Fixed
- kbd tag XHTML compliance for EPUB validation (`formats.py:_balance_kbd_tags`)
- Image spaces in EPUB filenames now sanitized before Pandoc conversion
```

## When to update

- After adding new features or CLI options
- After fixing bugs
- After modifying the PDF, EPUB, or DOCX pipelines
- After updating dependencies in `pyproject.toml`
- After making breaking changes to the API or config schema
