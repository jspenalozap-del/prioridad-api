from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.requests import router as solicitudes_router

app = FastAPI(title="Motor de Reglas de Priorización")

# ESTO DA PERMISO AL FRONTEND PARA CONECTARSE
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(solicitudes_router)

@app.get("/health")
def health():
    return {"status": "ok"}