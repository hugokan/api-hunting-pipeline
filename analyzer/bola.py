def detect_bola(results):
    findings = []
    for r in results:
        parts = r["endpoint"].rstrip("/").split("/")
        if parts[-1].isdigit() and r["status"] == 200:
            findings.append({**r, "tag": "BOLA_SUSPECTED"})
    return findings

