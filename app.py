import streamlit as st

from core.config import load_config
from core.scheduler import PhaseScheduler

from scanners.httpx import run_httpx
from scanners.ffuf import run_ffuf
from scanners.nuclei import run_nuclei

from analyzer.bola import detect_bola
from analyzer.bfla import detect_bfla

from ui.sidebar import render_sidebar

# --------------------------------------------------
# INIT
# --------------------------------------------------

st.set_page_config(page_title="API Hunting Dashboard", layout="wide")

config = load_config()

if "scheduler" not in st.session_state:
    st.session_state.scheduler = PhaseScheduler(config)

if "results" not in st.session_state:
    st.session_state.results = []

if "findings" not in st.session_state:
    st.session_state.findings = []

scheduler = st.session_state.scheduler

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

approve_promotion = render_sidebar(scheduler)

# --------------------------------------------------
# MAIN
# --------------------------------------------------

st.title("🛡️ API Hunting Dashboard")

targets = ["https://api.target.com"]
wordlist = ["users", "admin", "orders", "profile"]

if st.button("▶ Run pipeline"):
    ctx = scheduler.get_context()

    results = []
    results += run_httpx(ctx, targets)
    results += run_ffuf(ctx, targets[0], wordlist)

    if ctx.allow("nuclei"):
        results += run_nuclei(ctx, targets[0])

    st.session_state.results = results

    bola = detect_bola(results)
    bfla = detect_bfla(results)

    st.session_state.findings = bola + bfla

# --------------------------------------------------
# DISPLAY
# --------------------------------------------------

st.subheader("Scan Results")
if st.session_state.results:
    st.json(st.session_state.results)
else:
    st.info("No scan results yet")

st.subheader("Findings")
if st.session_state.findings:
    st.json(st.session_state.findings)
else:
    st.info("No findings detected")

# --------------------------------------------------
# PHASE PROMOTION
# --------------------------------------------------

stats = {"403_rate": 0.05, "429_rate": 0.0}

if scheduler.can_promote(stats, st.session_state.findings) and approve_promotion:
    scheduler.promote()
    st.success("Phase promoted to NORMAL")

