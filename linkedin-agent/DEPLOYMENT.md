# Deployment Guide

## Prerequisites
- Docker and Docker Compose
- LinkedIn Developer app (Client ID/Secret, redirect URI)
- OpenAI API key
- Domain + HTTPS (recommended)

## Environment
Copy `.env.example` to `.env` and set values. For production, set strong `SECRET_KEY`, secure DB creds, and HTTPS URLs.

## Build & Run
```bash
docker compose -f docker-compose.yml up --build -d
```

## Migrations
If you later add Alembic migrations, run them here. Current schema autogenerates on startup.

## Observability
- Backend logs via container logs
- Health check: GET `/healthz`

## Cloud Providers
- AWS ECS/Fargate or EC2
- GCP Cloud Run (use separate managed Postgres/Redis)
- Azure Container Apps

## Frontend Hosting
- Vercel or containerized with the compose file

## Secrets Management
Use cloud secret managers and avoid committing secrets.