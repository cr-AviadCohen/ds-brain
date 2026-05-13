from pathlib import Path

from lint.check_orphans import find_orphans


def test_page_with_no_inbound_links_is_orphan(tmp_path: Path) -> None:
    a = tmp_path / "Entities" / "People" / "Alice.md"
    a.parent.mkdir(parents=True)
    a.write_text("---\ntags: [wiki]\n---\nbody\n", encoding="utf-8")
    idx = tmp_path / "Log" / "INDEX.md"
    idx.parent.mkdir()
    idx.write_text("# Index\n\n(no links)\n", encoding="utf-8")
    orphans = find_orphans(tmp_path)
    assert any(o.name == "Alice.md" for o in orphans)


def test_linked_page_not_orphan(tmp_path: Path) -> None:
    a = tmp_path / "Entities" / "People" / "Alice.md"
    a.parent.mkdir(parents=True)
    a.write_text("---\ntags: [wiki]\n---\nbody\n", encoding="utf-8")
    idx = tmp_path / "Log" / "INDEX.md"
    idx.parent.mkdir()
    idx.write_text("# Index\n\n[[Alice]]\n", encoding="utf-8")
    orphans = find_orphans(tmp_path)
    assert all(o.name != "Alice.md" for o in orphans)
