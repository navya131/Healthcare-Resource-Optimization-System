from io import BytesIO
from pathlib import Path

import pandas as pd

try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import (
        Paragraph,
        SimpleDocTemplate,
        Spacer,
        Table,
        TableStyle,
    )
except ModuleNotFoundError:
    colors = None
    A4 = None
    landscape = None
    getSampleStyleSheet = None
    Paragraph = None
    SimpleDocTemplate = None
    Spacer = None
    Table = None
    TableStyle = None


REPORT_DIR = Path("reports") / "pdf"


def _escape_pdf_text(value):
    return (
        str(value)
        .replace("\\", "\\\\")
        .replace("(", "\\(")
        .replace(")", "\\)")
    )


def _wrap_lines(text, width=90):
    lines = []
    for raw_line in str(text).splitlines() or [""]:
        if not raw_line:
            lines.append("")
            continue
        while len(raw_line) > width:
            lines.append(raw_line[:width])
            raw_line = raw_line[width:]
        lines.append(raw_line)
    return lines


def _simple_pdf_bytes(title, dataframe):
    if isinstance(dataframe, pd.DataFrame):
        body = dataframe.to_string(index=False)
    else:
        body = str(dataframe)

    lines = [str(title), "", body]
    text_lines = []
    for line in lines:
        text_lines.extend(_wrap_lines(line))

    content_lines = [
        "BT",
        "/F1 12 Tf",
        "1 0 0 1 50 780 Tm",
        "14 TL",
    ]
    for line in text_lines:
        content_lines.append(f"({_escape_pdf_text(line)}) Tj")
        content_lines.append("T*")
    content_lines.append("ET")
    content = "\n".join(content_lines).encode("latin-1", "replace")

    objects = []
    objects.append(b"1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj\n")
    objects.append(b"2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >> endobj\n")
    objects.append(
        b"3 0 obj << /Type /Page /Parent 2 0 R /MediaBox [0 0 842 595] "
        b"/Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >> endobj\n"
    )
    objects.append(
        b"4 0 obj << /Length "
        + str(len(content)).encode("ascii")
        + b" >> stream\n"
        + content
        + b"\nendstream endobj\n"
    )
    objects.append(
        b"5 0 obj << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> endobj\n"
    )

    output = [b"%PDF-1.4\n"]
    offsets = [0]
    cursor = len(output[0])
    for obj in objects:
        offsets.append(cursor)
        output.append(obj)
        cursor += len(obj)

    xref_offset = cursor
    xref_lines = [
        b"xref\n",
        f"0 {len(objects) + 1}\n".encode("ascii"),
        b"0000000000 65535 f \n",
    ]
    for offset in offsets[1:]:
        xref_lines.append(f"{offset:010d} 00000 n \n".encode("ascii"))
    trailer = (
        b"trailer << /Size "
        + str(len(objects) + 1).encode("ascii")
        + b" /Root 1 0 R >>\nstartxref\n"
        + str(xref_offset).encode("ascii")
        + b"\n%%EOF"
    )
    output.extend(xref_lines)
    output.append(trailer)
    return b"".join(output)


def _dataframe_to_table_data(dataframe, max_rows=40):
    if dataframe is None or dataframe.empty:
        return [["Message"], ["No records found for this report."]]

    preview = dataframe.head(max_rows).copy()
    table_data = [list(preview.columns)]

    for _, row in preview.iterrows():
        table_data.append([str(value) for value in row.tolist()])

    return table_data


def _build_pdf(target, title, dataframe):
    if SimpleDocTemplate is None:
        pdf_bytes = _simple_pdf_bytes(title, dataframe)
        if hasattr(target, "write"):
            target.write(pdf_bytes)
            return
        Path(target).write_bytes(pdf_bytes)
        return

    doc = SimpleDocTemplate(
        target,
        pagesize=landscape(A4),
        rightMargin=24,
        leftMargin=24,
        topMargin=24,
        bottomMargin=24,
    )
    styles = getSampleStyleSheet()

    elements = [
        Paragraph(str(title), styles["Title"]),
        Spacer(1, 12),
    ]

    if isinstance(dataframe, pd.DataFrame):
        table_data = _dataframe_to_table_data(dataframe)
    else:
        table_data = [["Report Content"], [str(dataframe)]]

    table = Table(table_data, repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1565C0")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 8),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F4F8FB")]),
            ]
        )
    )
    elements.append(table)

    doc.build(elements)


def generate_pdf_report(filename, title, content):
    REPORT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    target = REPORT_DIR / filename
    _build_pdf(str(target), title, content)
    return str(target)


def generate_pdf_report_bytes(title, dataframe):
    buffer = BytesIO()
    _build_pdf(buffer, title, dataframe)
    buffer.seek(0)
    return buffer.getvalue()
