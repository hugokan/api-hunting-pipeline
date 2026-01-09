import subprocess

def run():
    subprocess.run([
        "ffuf",
        "-u", "https://api.target.com/FUZZ",
        "-w", "wordlists/api-paths.txt",
        "-mc", "200,401,403",
        "-of", "json",
        "-o", "data/ffuf.json"
    ], check=True)

