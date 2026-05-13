from pathlib import Path

from lint.check_stale_links import find_stale_links


def test_link_to_missing_page_flagged(tmp_path: Path) -> None:
    p = tmp_path / "Entities" / "People" / "Alice.md"
    p.parent.mkdir(parents=True)
    p.write_text("Worked with [[Ghost]].\n", encoding="utf-8")
    stale = find_stale_links(tmp_path)
    assert any(s.target == "Ghost" for s in stale)


def test_link_to_existing_page_ok(tmp_path: Path) -> None:
    (tmp_path / "Entities" / "People").mkdir(parents=True)
    (tmp_path / "Entities" / "People" / "Alice.md").write_text(
        "Worked with [[Bob]].\n", encoding="utf-8"
    )
    (tmp_path / "Entities" / "People" / "Bob.md").write_text("hi", encoding="utf-8")
    stale = find_stale_links(tmp_path)
    assert not stale


def test_link_inside_fenced_code_block_ignored(tmp_path: Path) -> None:
    p = tmp_path / "Foo" / "README.md"
    p.parent.mkdir(parents=True)
    p.write_text(
        "Real link: [[Bar]].\n"
        "\n"
        "```yaml\n"
        "team: [[Ghost]], [[Another Ghost]]\n"
        "```\n",
        encoding="utf-8",
    )
    (tmp_path / "Foo" / "Bar.md").write_text("hi", encoding="utf-8")
    stale = find_stale_links(tmp_path)
    targets = {s.target for s in stale}
    assert "Ghost" not in targets, f"link inside ``` fence must be ignored, got {targets}"
    assert "Another Ghost" not in targets


def test_link_inside_tilde_fenced_block_ignored(tmp_path: Path) -> None:
    p = tmp_path / "x.md"
    p.write_text(
        "~~~markdown\n"
        "[[<Person>]] — example placeholder\n"
        "~~~\n",
        encoding="utf-8",
    )
    stale = find_stale_links(tmp_path)
    assert not any(s.target == "<Person>" for s in stale)


def test_link_in_inline_code_still_flagged(tmp_path: Path) -> None:
    # Inline `[[X]]` (single backticks) — too noisy to strip; only block fences are
    # stripped. Document this behavior with a test that pins the current scope.
    p = tmp_path / "y.md"
    p.write_text("See `[[Inline Ghost]]` in prose.\n", encoding="utf-8")
    stale = find_stale_links(tmp_path)
    assert any(s.target == "Inline Ghost" for s in stale)
