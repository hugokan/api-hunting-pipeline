from pipeline.subfinder import run as subfinder
from pipeline.httpx import run as httpx
from pipeline.ffuf import run as ffuf
from pipeline.nuclei import run as nuclei

subfinder("input/domains.txt")
httpx()
ffuf()
nuclei()

