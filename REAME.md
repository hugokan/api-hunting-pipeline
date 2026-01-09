# Instrucciones

## Para ejuctar el pipeline
1. desde la raiz
2. Ejeuctar el .py
3. 
## Para levantar el dashboard
1. Ir a la carpeta dashboard
2. Ejecutar el siguiente comando: streamlit run app.py

## Estructura

api-hunting-dashboard/
├── app.py
├── config.yaml
│
├── core/
│   ├── config.py
│   ├── context.py
│   └── scheduler.py
│
├── scanners/
│   ├── ffuf.py
│   ├── httpx.py
│   └── nuclei.py
│
├── analyzer/
│   ├── bola.py
│   └── bfla.py
│
├── ui/
│   └── sidebar.py
│
└── utils/
    └── monitor.py


## use a virtual environment:
    
    python3 -m venv path/to/venv
    source path/to/venv/bin/activate
    python3 -m pip install xyz