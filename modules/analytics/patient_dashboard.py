import pandas as pd
import streamlit as st

from config.database import get_connection


def _cancel_appointment(appointment_id, cancellation_reason):
    conn = get_connection()
    conn.execute(
        """
        UPDATE appointments
        SET status = 'Cancelled',
            cancellation_reason = ?
        WHERE appointment_id = ?
        """,
        (cancellation_reason, appointment_id)
    )
    conn.commit()
    conn.close()


def patient_dashboard_page():
    st.header("Patient Dashboard")

    conn = get_connection()

    appointments = pd.read_sql_query(
        """
        SELECT
            a.appointment_id,
            a.appointment_date,
            a.appointment_time,
            a.status,
            a.reason,
            COALESCE(a.cancellation_reason, '') AS cancellation_reason,
            COALESCE(u.full_name, 'Unassigned') AS doctor_name,
            COALESCE(d.specialization, 'General') AS specialization
        FROM appointments a
        LEFT JOIN doctors d ON a.doctor_id = d.doctor_id
        LEFT JOIN users u ON d.user_id = u.id
        WHERE a.patient_user_id = ?
        ORDER BY a.appointment_id DESC
        """,
        conn,
        params=(st.session_state.user_id,)
    )

    records = pd.read_sql_query(
        """
        SELECT
            record_id,
            diagnosis,
            visit_date,
            treatment,
            doctor_notes
        FROM medical_records
        WHERE patient_user_id = ?
        ORDER BY record_id DESC
        """,
        conn,
        params=(st.session_state.user_id,)
    )

    prescriptions = pd.read_sql_query(
        """
        SELECT
            prescription_id,
            medication,
            dosage,
            duration,
            instructions,
            prescribed_date
        FROM prescriptions
        WHERE patient_user_id = ?
        ORDER BY prescription_id DESC
        """,
        conn,
        params=(st.session_state.user_id,)
    )

    diagnostics = pd.read_sql_query(
        """
        SELECT
            diagnostic_id,
            report_name,
            report_type,
            report_file,
            upload_date
        FROM diagnostics
        WHERE patient_user_id = ?
        ORDER BY diagnostic_id DESC
        """,
        conn,
        params=(st.session_state.user_id,)
    )

    conn.close()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Appointments", len(appointments))
    c2.metric("Medical Records", len(records))
    c3.metric("Prescriptions", len(prescriptions))
    c4.metric("Reports", len(diagnostics))

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Appointments", "Medical Records", "Prescriptions", "Diagnostics"]
    )

    with tab1:
        st.dataframe(appointments, use_container_width=True)

        cancellable = appointments[
            appointments["status"].isin(["Pending", "Approved"])
        ]

        if not cancellable.empty:
            st.subheader("Cancel Appointment")

            option_map = {
                f"#{row.appointment_id} - {row.doctor_name} on {row.appointment_date} at {row.appointment_time}": row.appointment_id
                for row in cancellable.itertuples(index=False)
            }

            selected = st.selectbox(
                "Select appointment to cancel",
                list(option_map.keys())
            )
            cancellation_reason = st.text_area(
                "Cancellation Reason",
                key="patient_cancel_reason"
            )

            if st.button("Cancel Appointment"):
                if not cancellation_reason.strip():
                    st.error("Please enter a cancellation reason.")
                else:
                    _cancel_appointment(
                        option_map[selected],
                        cancellation_reason.strip()
                    )
                    st.success("Appointment cancelled.")
                    st.rerun()

    with tab2:
        st.dataframe(records, use_container_width=True)

    with tab3:
        st.dataframe(prescriptions, use_container_width=True)

    with tab4:
        st.dataframe(diagnostics, use_container_width=True)
