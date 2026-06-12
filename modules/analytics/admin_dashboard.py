import pandas as pd
import streamlit as st

from modules.analytics.analytics_service import (
    get_patients,
    get_doctors,
    get_appointments,
    get_resources,
    get_beds
)
from modules.analytics.visualizations import (
    appointment_chart,
    bed_chart,
    resource_chart
)


def admin_analytics_page():
    st.header("Healthcare Analytics Dashboard")

    patients = get_patients()
    doctors = get_doctors()
    appointments = get_appointments()
    resources = get_resources()
    beds = get_beds()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Patients", len(patients))
    c2.metric("Doctors", len(doctors))
    c3.metric("Appointments", len(appointments))
    c4.metric("Beds", len(beds))

    tab1, tab2, tab3 = st.tabs(["Charts", "Module Snapshot", "Raw Data"])

    with tab1:
        fig1 = appointment_chart(appointments)
        if fig1:
            st.plotly_chart(fig1, use_container_width=True)

        fig2 = bed_chart(beds)
        if fig2:
            st.plotly_chart(fig2, use_container_width=True)

        fig3 = resource_chart(resources)
        if fig3:
            st.plotly_chart(fig3, use_container_width=True)

    with tab2:
        snapshot = pd.DataFrame(
            {
                "Module": ["Patients", "Doctors", "Appointments", "Resources", "Beds"],
                "Records": [len(patients), len(doctors), len(appointments), len(resources), len(beds)]
            }
        )
        st.dataframe(snapshot, use_container_width=True, hide_index=True)

    with tab3:
        st.write("Patients")
        st.dataframe(patients, use_container_width=True)
        st.write("Doctors")
        st.dataframe(doctors, use_container_width=True)
