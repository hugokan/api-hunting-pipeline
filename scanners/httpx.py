def run_ffuf(ctx, base_url, wordlist):
    if not ctx.allow("ffuf"):
        return []

    max_words = ctx.rules["ffuf"]["max_words"]
    words = wordlist[:max_words]

    results = []
    for w in words:
        results.append({
            "endpoint": f"{base_url}/{w}",
            "method": "GET",
            "status": 403,
            "scanner": "ffuf"
        })
    return results


