import subprocess

def run():
    subprocess.run([
        "nuclei",
        "-l", "data/alive.txt",
        "-t", "api/",
        "-severity", "medium,high,critical",
        "-json",
        "-o", "data/nuclei.json"
    ], check=True)

