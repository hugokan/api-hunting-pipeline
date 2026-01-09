import subprocess

def run():
    subprocess.run([
        "httpx",
        "-l", "data/subs.txt",
        "-mc", "200,401,403",
        "-o", "data/alive.txt"
    ], check=True)
