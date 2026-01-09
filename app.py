import streamlit as st

from core.config import load_config
from core.scheduler import PhaseScheduler
from scanners.httpx import run_httpx
from scanners.ffuf import run_ffuf
from scanners.nuclei import run_nuclei
from analyzer.bola import detect_bola
from analyzer.bfla import detect_bfla
from ui.sidebar import render_sidebar

config = load_config()
scheduler = PhaseScheduler(config)

ctx = scheduler.get_context()

approve_promotion = render_sidebar(ctx.mode)

st.title("API Hunting Dashboard")

targets = ["http://localhost:8888"]
wordlist = ["users", "admin", "orders"]

results = []
results += run_httpx(ctx, targets)
results += run_ffuf(ctx, targets[0], wordlist)

if ctx.allow("nuclei"):
    results += run_nuclei(ctx, targets[0])

bola = detect_bola(results)
bfla = detect_bfla(results)

findings = bola + bfla

st.subheader("Findings")
st.json(findings)

stats = {"403_rate": 0.05, "429_rate": 0.0}

if scheduler.can_promote(stats, findings) and approve_promotion:
    scheduler.promote()
    st.success("Phase promoted to NORMAL")
