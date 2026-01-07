import os
from dotenv import load_dotenv
load_dotenv()
from fastapi import APIRouter, Query
from uuid import uuid4
from datetime import datetime, timezone
from app.api.schemas.request import SolicitudCreate, SolicitudOut
from app.domain.models import Solicitud, TipoSolicitud
from app.domain.priority_engine import prioridad_calculada
from app.repositories.supabase_repo import SupabaseSolicitudRepository

router = APIRouter(prefix="/solicitudes", tags=["Solicitudes"])

# Conexión a Supabase usando el archivo .env
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
repo = SupabaseSolicitudRepository(url, key)

@router.post("", response_model=SolicitudOut, status_code=201)
def crear_solicitud(payload: SolicitudCreate):
    s = Solicitud(
        id=uuid4(),
        tipo=TipoSolicitud(payload.tipo),
        prioridad_manual=payload.prioridad_manual,
        fecha_creacion=datetime.now(timezone.utc),
        usuario=payload.usuario,
        descripcion=payload.descripcion,
    )
    repo.add(s) # Guarda en Supabase
    return SolicitudOut(**s.__dict__, prioridad_calculada=prioridad_calculada(s))

@router.get("", response_model=list[SolicitudOut])
def listar_solicitudes(priority: int | None = Query(default=None, ge=1, le=5)):
    items = repo.list_all() # Trae de Supabase
    
    resultado = []
    for s in items:
        pc = prioridad_calculada(s)
        if priority is None or pc == priority:
            resultado.append(SolicitudOut(**s.__dict__, prioridad_calculada=pc))
    
    # Ordenar por prioridad calculada
    resultado.sort(key=lambda x: -x.prioridad_calculada)
    return resultado