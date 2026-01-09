import json
import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="API Bug Hunting Dashboard",
    layout="wide"
)

st.title("🛡️ API Bug Hunting Dashboard")
st.caption("ffuf + nuclei | Recon & Verification")

DATA_DIR = Path("../data")

# -------------------------
# Load FFUF data
# -------------------------
def load_ffuf():
    with open(DATA_DIR / "ffuf_endpoints.json") as f:
        data = json.load(f)

    rows = []
    for r in data.get("results", []):
        rows.append({
            "URL": r["url"],
            "Status": r["status"],
            "Length": r["length"],
            "Words": r["words"],
            "Lines": r["lines"],
        })

    return pd.DataFrame(rows)

# -------------------------
# Load Nuclei data
# -------------------------
def load_nuclei():
    rows = []

    with open(DATA_DIR / "nuclei_findings.json") as f:
        for line in f:
            r = json.loads(line)
            rows.append({
                "Template": r.get("template-id"),
                "Name": r.get("info", {}).get("name"),
                "Severity": r.get("severity"),
                "Type": r.get("type"),
                "URL": r.get("matched-at"),
            })

    return pd.DataFrame(rows)

# -------------------------
# Sidebar
# -------------------------
st.sidebar.header("⚙️ Filtros")

severity_filter = st.sidebar.multiselect(
    "Severidad",
    ["low", "medium", "high", "critical"],
    default=["medium", "high", "critical"]
)

status_filter = st.sidebar.multiselect(
    "Status Code",
    [200, 401, 403, 404],
    default=[200, 401, 403]
)

# -------------------------
# Main Layout
# -------------------------
col1, col2 = st.columns(2)

# -------- FFUF --------
with col1:
    st.subheader("🔎 Endpoints descubiertos (ffuf)")

    ffuf_df = load_ffuf()
    ffuf_df = ffuf_df[ffuf_df["Status"].isin(status_filter)]

    st.metric("Total endpoints", len(ffuf_df))

    st.dataframe(
        ffuf_df,
        use_container_width=True
    )

# -------- NUCLEI --------
with col2:
    st.subheader("🚨 Vulnerabilidades detectadas (nuclei)")

    nuclei_df = load_nuclei()
    nuclei_df = nuclei_df[nuclei_df["Severity"].isin(severity_filter)]

    st.metric("Findings", len(nuclei_df))

    st.dataframe(
        nuclei_df,
        use_container_width=True
    )

# -------------------------
# Severity Stats
# -------------------------
st.subheader("📊 Severidad")

if not nuclei_df.empty:
    sev_count = nuclei_df["Severity"].value_counts()
    st.bar_chart(sev_count)
else:
    st.info("No hay findings con los filtros actuales")
