# Sistema de Scraping con Lector de Patrones

> Proyecto académico — Diseño de Sistemas de Información
> Instituto Tecnológico Metropolitano (ITM) · 2026

Sistema automatizado que monitorea mesas de casino en vivo, detecta rachas repetidas en los resultados de cada ronda y envía alertas inmediatas al operador vía Telegram.

---

## Integrantes

| Nombre | Rol principal |
|--------|---------------|
| Andrés Mauricio Coneo Pretelt | Implementación Facade + Observers |
| Juan David Hincapié Puerta | Arquitectura del repositorio, motor principal |
| Shara García Betancur | Reglas de detección, documentación técnica |

---

## Tecnologías utilizadas

| Capa | Tecnología |
|------|-----------|
| Motor de scraping | Python 3.11 + Playwright (Chromium headless) |
| Lógica de patrones | Python 3.11 (clases abstractas, ABCs) |
| Notificaciones | Telegram Bot API (HTTP REST) |
| Persistencia | PostgreSQL 15 |
| API REST (proyectado) | FastAPI |
| Frontend (proyectado) | React + TypeScript |
| Control de versiones | Git + GitHub |

---

## Arquitectura general

El sistema sigue una arquitectura en capas con patrones GoF:

```
main.py
  - CasinoScraperFacade   (Facade - encapsula Playwright)
  - PatronEngine           (Interpreter + Observer)
       - CorteRachaRule    (IPatronRule)
       - TelegramObserver  (IObserver -> Telegram Bot API)
       - DatabaseObserver  (IObserver -> PostgreSQL)
```

Consultar el modelo C4 completo (4 niveles) en el documento Entregable No. 2.

---

## Funcionalidades implementadas (MVP)

- [x] Conexión a mesa de casino en vivo vía Playwright
- [x] Extracción de resultado por ronda (scraping DOM dinámico)
- [x] Protocolo anti-inactividad (keep-alive automático)
- [x] Motor de reglas: `CorteRachaRule` detecta N resultados consecutivos iguales
- [x] Alerta inmediata a Telegram cuando se detecta el patrón al 100%
- [x] Persistencia de señales en PostgreSQL (mock en desarrollo)
- [x] Flujo alternativo: timeout de conexión con reintento automático
- [ ] API REST (FastAPI) — proyectado para siguiente iteración
- [ ] Dashboard web (React) — proyectado para siguiente iteración

---

## Requisitos de instalación

**Python 3.11+**

```bash
pip install playwright
playwright install chromium
pip install psycopg2-binary python-telegram-bot
```

**Variables de entorno** — crear archivo `.env` en la raíz:

```
TELEGRAM_TOKEN=tu_token_de_bot
CHAT_ID=tu_chat_id
DB_URL=postgresql://usuario:password@localhost:5432/scraping_db
```

---

## Instrucciones para ejecutar

```bash
# 1. Clonar el repositorio
git clone https://github.com/juandapuerta1/NEXUS_ProyectoLunes.git
cd NEXUS_ProyectoLunes

# 2. Instalar dependencias
pip install -r requirements.txt
playwright install chromium

# 3. Configurar variables de entorno (ver sección anterior)

# 4. Ejecutar
python main.py
```

---

## Estructura del proyecto

```
NEXUS_ProyectoLunes/
├── config/            Variables de entorno y configuración
├── db/                Mock de conexión a PostgreSQL
├── main.py            Punto de entrada y orquestador del flujo
├── requirements.txt   Dependencias del proyecto
└── README.md          Este archivo
```

---

## Patrones de diseño aplicados

| Patrón | Clase | Propósito |
|--------|-------|-----------|
| Facade | `CasinoScraperFacade` | Encapsula la complejidad de Playwright |
| Observer | `TelegramObserver`, `DatabaseObserver` | Notificación desacoplada al detectar patrón |
| Interpreter | `CorteRachaRule` + `IPatronRule` | Reglas de detección extensibles sin modificar el motor |

---

## Principios SOLID aplicados

- **SRP**: cada clase tiene una única responsabilidad
- **OCP**: agregar una nueva regla solo requiere implementar `IPatronRule`
- **LSP**: cualquier `IPatronRule` puede inyectarse en `PatronEngine`
- **ISP**: `IAlertaRepository` e `IFuenteRepository` son interfaces separadas
- **DIP**: `PatronEngine` depende de `IObserver`, no de `TelegramObserver` directamente

---

## Enlaces

- **Prototipo Figma**: https://www.figma.com/design/O2EGtqc4trFfd0F9rte7hP/Sistema-de-Scraping---Prototipo-AF
- **Tablero Trello**: https://trello.com/b/agFFc50y/sistema-de-scraping-backlog-hus
- **Diagramas UML editables**: [agregar enlace Miro/Lucidchart]

---

## Docente

Alexandra Guerrero Bocanegra — Diseño de Sistemas de Información — ITM — 2026
