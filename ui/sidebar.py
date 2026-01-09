import streamlit as st

def render_sidebar(scheduler):
    st.sidebar.title("Execution Phase")
    st.sidebar.write(f"Current phase: **{scheduler.current_phase.upper()}**")

    approve = False
    if scheduler.current_phase == "stealth":
        approve = st.sidebar.checkbox("Allow promotion to NORMAL")

    return approve

