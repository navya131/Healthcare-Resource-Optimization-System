import pandas as pd

try:
    import plotly.express as px
except ModuleNotFoundError:
    px = None


def _has_columns(df, columns):
    return isinstance(df, pd.DataFrame) and not df.empty and all(
        column in df.columns for column in columns
    )


def appointment_chart(df):
    if px is None or not _has_columns(df, ["status"]):
        return None

    summary = (
        df["status"]
        .fillna("Unknown")
        .value_counts()
        .reset_index()
    )
    summary.columns = ["Status", "Count"]

    return px.bar(
        summary,
        x="Status",
        y="Count",
        title="Appointments by Status",
        text="Count",
    )


def bed_chart(df):
    if px is None or not _has_columns(df, ["status"]):
        return None

    summary = (
        df["status"]
        .fillna("Unknown")
        .value_counts()
        .reset_index()
    )
    summary.columns = ["Status", "Count"]

    return px.pie(
        summary,
        names="Status",
        values="Count",
        title="Bed Availability",
        hole=0.35,
    )


def resource_chart(df):
    if px is None or not _has_columns(df, ["resource_type", "available_quantity"]):
        return None

    summary = (
        df.groupby("resource_type", dropna=False)["available_quantity"]
        .sum()
        .reset_index()
    )
    summary["resource_type"] = summary["resource_type"].fillna("Unknown")

    return px.bar(
        summary,
        x="resource_type",
        y="available_quantity",
        title="Available Resources by Type",
        labels={
            "resource_type": "Resource Type",
            "available_quantity": "Available Quantity",
        },
        text="available_quantity",
    )
