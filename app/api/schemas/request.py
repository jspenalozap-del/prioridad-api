from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field

class SolicitudCreate(BaseModel):
    tipo: str
    prioridad_manual: int = Field(ge=1, le=5)
    usuario: str
    descripcion: str | None = None

class SolicitudOut(BaseModel):
    id: UUID
    tipo: str
    prioridad_manual: int
    fecha_creacion: datetime
    usuario: str
    descripcion: str | None = None
    prioridad_calculada: int