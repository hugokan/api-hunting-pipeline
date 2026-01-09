import subprocess

def run(domains_file):
    subprocess.run([
        "subfinder",
        "-dL", domains_file,
        "-o", "data/subs.txt"
    ], check=True)
