from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from uuid import UUID

class TipoSolicitud(str, Enum):
    INCIDENTE = "INCIDENTE"
    REQUERIMIENTO = "REQUERIMIENTO"
    CONSULTA = "CONSULTA"

@dataclass(frozen=True)
class Solicitud:
    id: UUID
    tipo: TipoSolicitud
    prioridad_manual: int
    fecha_creacion: datetime
    usuario: str
    descripcion: str | None = None