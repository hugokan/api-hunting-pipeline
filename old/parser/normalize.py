import json

def extract_urls():
    with open("ffuf_endpoints.json") as f:
        data = json.load(f)

    urls = set()
    for r in data["results"]:
        if r["status"] in [200, 401, 403]:
            urls.add(r["url"])

    with open("clean_endpoints.txt", "w") as f:
        f.write("\n".join(urls))

if __name__ == "__main__":
    extract_urls()
