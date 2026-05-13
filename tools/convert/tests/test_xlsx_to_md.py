from pathlib import Path

from openpyxl import Workbook

from convert.xlsx_to_md import xlsx_to_markdown


def test_sheet_becomes_table(tmp_path: Path) -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "people"
    ws.append(["Name", "Role"])
    ws.append(["Alice", "PM"])
    ws.append(["Bob", "Eng"])
    src = tmp_path / "x.xlsx"
    wb.save(src)

    md = xlsx_to_markdown(src)
    assert "## people" in md
    assert "| Name | Role |" in md
    assert "| Alice | PM |" in md
