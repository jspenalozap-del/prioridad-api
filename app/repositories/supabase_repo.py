from datetime import datetime
from uuid import UUID
from supabase import create_client, Client
from app.domain.models import Solicitud, TipoSolicitud

class SupabaseSolicitudRepository:
    def __init__(self, url: str, key: str):
        self.client: Client = create_client(url, key)

    def add(self, s: Solicitud) -> None:
        # Esto guarda en la base de datos
        self.client.table("solicitudes").insert({
            "id": str(s.id),
            "tipo": s.tipo.value,
            "prioridad_manual": s.prioridad_manual,
            "fecha_creacion": s.fecha_creacion.isoformat(),
            "usuario": s.usuario,
            "descripcion": s.descripcion,
        }).execute()

    def list_all(self) -> list[Solicitud]:
        # Esto trae los datos de la base de datos
        res = self.client.table("solicitudes").select("*").execute()
        data = res.data or []
        
        resultado = []
        for row in data:
            resultado.append(Solicitud(
                id=UUID(row["id"]),
                tipo=TipoSolicitud(row["tipo"]),
                prioridad_manual=int(row["prioridad_manual"]),
                fecha_creacion=datetime.fromisoformat(row["fecha_creacion"].replace("Z", "+00:00")),
                usuario=row["usuario"],
                descripcion=row.get("descripcion")
            ))
        return resultado