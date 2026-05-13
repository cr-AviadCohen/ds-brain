from pathlib import Path

from lint.check_frontmatter import find_violations


def test_missing_wiki_tag_is_violation(tmp_path: Path) -> None:
    p = tmp_path / "Entities" / "People" / "Alice.md"
    p.parent.mkdir(parents=True)
    p.write_text(
        "---\ntitle: Alice\ntype: person\ntags: [person]\nlast_updated: 2026-05-11\n---\nBody.\n",
        encoding="utf-8",
    )
    violations = find_violations(tmp_path)
    assert any("wiki tag" in v.message for v in violations)


def test_proper_frontmatter_passes(tmp_path: Path) -> None:
    p = tmp_path / "Entities" / "People" / "Bob.md"
    p.parent.mkdir(parents=True)
    p.write_text(
        "---\ntitle: Bob\ntype: person\ntags: [person, wiki]\nlast_updated: 2026-05-11\n---\nBody.\n",
        encoding="utf-8",
    )
    violations = find_violations(tmp_path)
    assert not violations


def test_archive_files_excluded(tmp_path: Path) -> None:
    p = tmp_path / "📦 Archive" / "x.md"
    p.parent.mkdir(parents=True)
    p.write_text("no frontmatter\n", encoding="utf-8")
    violations = find_violations(tmp_path)
    assert not violations


def test_readme_files_excluded(tmp_path: Path) -> None:
    p = tmp_path / "Entities" / "People" / "README.md"
    p.parent.mkdir(parents=True)
    p.write_text("no frontmatter\n", encoding="utf-8")
    violations = find_violations(tmp_path)
    assert not violations
