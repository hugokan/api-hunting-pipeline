def run_httpx(ctx, targets):
    if not ctx.allow("httpx"):
        return []

    results = []
    for t in targets:
        results.append({
            "endpoint": t,
            "method": "GET",
            "status": 200,
            "scanner": "httpx"
        })
    return results
