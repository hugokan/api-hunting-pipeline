import streamlit as st

def render_sidebar(mode):
    st.sidebar.title("Execution Phase")

    st.sidebar.write(f"Current phase: **{mode.upper()}**")

    if mode == "stealth":
        st.sidebar.info("Low noise reconnaissance")
    elif mode == "normal":
        st.sidebar.warning("Access control testing")

    approve = st.sidebar.checkbox("Allow phase promotion")
    return approve
