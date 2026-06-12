from config.database import get_connection
import pandas as pd


def get_patients():

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM patients",
        conn
    )

    conn.close()

    return df


def get_doctors():

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM doctors",
        conn
    )

    conn.close()

    return df


def get_appointments():

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM appointments",
        conn
    )

    conn.close()

    return df


def get_resources():

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM resources",
        conn
    )

    conn.close()

    return df


def get_beds():

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM beds",
        conn
    )

    conn.close()

    return df