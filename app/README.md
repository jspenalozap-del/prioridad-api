# 🎯 Motor de Reglas de Priorización

Este proyecto es una solución a la prueba técnica para el Centro de Ingeniería de Software. Consiste en un sistema que registra solicitudes y las ordena dinámicamente basándose en un motor de reglas de negocio.

## 🚀 Decisiones de Arquitectura (Trade-offs)
Para este proyecto utilicé **Arquitectura Limpia (Clean Architecture)** simplificada:
- **Dominio:** Contiene las reglas de negocio puras (Motor de Priorización) independientes de la tecnología.
- **Infraestructura:** Implementé un repositorio para **Supabase** (persistencia real) y dejé preparada la estructura para persistencia en memoria.
- **API:** FastAPI para una comunicación rápida y documentación automática con Swagger.

**Decisión clave:** Separé el cálculo de la prioridad en un `priority_engine.py`. Esto permite que las reglas cambien en el futuro sin tocar los controladores o la base de datos, cumpliendo con el requisito de "API evolutiva".

## 🧠 El Motor de Reglas
La prioridad calculada no es un simple campo de la base de datos, se calcula bajo estas reglas:
1. **Peso por Tipo:** Los `INCIDENTE` suman +1.5 puntos de peso base.
2. **Antigüedad:** Por cada 24 horas que pasa una solicitud sin atender, su prioridad aumenta +0.5 puntos (evita el estancamiento).
3. **Manual:** La prioridad manual del usuario influye en el score inicial.
4. **Límites:** El resultado siempre se mantiene en el rango de 1 a 5.

## 🛠️ Tecnologías utilizadas
- **Backend:** Python 3.13, FastAPI, Pydantic, Supabase SDK.
- **Frontend:** React JS, Axios, CSS3.
- **Base de Datos:** PostgreSQL (vía Supabase).

## ⚙️ Instalación y Ejecución

### Backend
1. Crear entorno virtual: `python -m venv .venv`
2. Activar: `.venv\Scripts\activate`
3. Instalar: `pip install -r requirements.txt`
4. Configurar `.env` con `SUPABASE_URL` y `SUPABASE_KEY`.
5. Correr: `uvicorn app.main:app --reload`

### Frontend
1. Instalar: `npm install`
2. Correr: `npm start`