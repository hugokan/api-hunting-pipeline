def detect_bola(results):
    findings = []
    for r in results:
        if "{id}" in r["endpoint"] or r["endpoint"].rstrip("/").split("/")[-1].isdigit():
            if r["status"] == 200:
                findings.append({**r, "tag": "BOLA_SUSPECTED"})
    return findings
