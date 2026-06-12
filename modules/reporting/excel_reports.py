import pandas as pd
from pathlib import Path


REPORT_DIR = Path("reports") / "excel"


def generate_excel_report(
    dataframe,
    filename
):
    REPORT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    target = REPORT_DIR / filename

    dataframe.to_excel(
        target,
        index=False
    )

    return str(target)
