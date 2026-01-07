from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Importar esto
from app.api.routes import requests
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Motor de Reglas de Priorización")

# --- AGREGAR ESTE BLOQUE ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # En producción podrías poner la URL de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ---------------------------

app.include_router(requests.router)

@app.get("/health")
def health():
    return {"status": "ok"}