def detect_bfla(results):
    findings = []
    for r in results:
        if r["method"] in ["DELETE", "PUT", "PATCH"] and r["status"] < 300:
            findings.append({**r, "tag": "BFLA_SUSPECTED"})
    return findings

