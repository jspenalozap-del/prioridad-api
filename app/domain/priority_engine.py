from datetime import datetime, timezone
from app.domain.models import Solicitud, TipoSolicitud

def prioridad_calculada(s: Solicitud) -> int:
    # 1. Empezamos con la prioridad manual (1 a 5)
    score = float(s.prioridad_manual)

    # 2. Regla de Negocio: Los INCIDENTES tienen más peso (+1.5 puntos)
    if s.tipo == TipoSolicitud.INCIDENTE:
        score += 1.5
    elif s.tipo == TipoSolicitud.REQUERIMIENTO:
        score += 0.5

    # 3. Regla de Negocio: Antigüedad aumenta prioridad
    # Calculamos cuántas horas han pasado desde que se creó
    ahora = datetime.now(timezone.utc)
    diferencia = ahora - s.fecha_creacion
    horas_transcurridas = diferencia.total_seconds() / 3600
    
    # Por cada 24 horas, sumamos 0.5 puntos de prioridad (para que no se queden olvidadas)
    score += (horas_transcurridas / 24) * 0.5

    # 4. Ajuste final: El resultado debe estar entre 1 y 5
    # Usamos round para que sea un número entero
    resultado = round(score)
    
    if resultado > 5:
        return 5
    if resultado < 1:
        return 1
        
    return resultado