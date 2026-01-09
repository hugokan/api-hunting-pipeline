def run_nuclei(ctx, target):
    if not ctx.allow("nuclei"):
        return []

    return [{
        "endpoint": target,
        "method": "GET",
        "status": 200,
        "severity": "high",
        "scanner": "nuclei"
    }]

