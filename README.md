# DevOps Project

Proyecto de infraestructura moderna con Docker, CI/CD y AWS.

## Requisitos
- Docker Desktop

## Cómo ejecutar localmente

```bash
docker-compose up --build
```

Abrir en el navegador: http://localhost:5000

## Endpoints
- `/` — Página principal
- `/health` — Estado de la app
- `/api/tareas` — Lista de tareas
- `/api/info` — Info del sistema

## Tecnologías
- Python + Flask
- PostgreSQL
- Docker + Docker Compose
- GitHub Actions (CI/CD)
- AWS EC2
