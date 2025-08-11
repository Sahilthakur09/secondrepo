# Deployment Guide

## Prerequisites
- Docker and Docker Compose
- Domain and HTTPS (recommend a reverse proxy like Traefik or Nginx)

## Environment
- Copy `.env.example` to `.env` and fill credentials

## Run
```
docker compose up -d --build
```

## Production Notes
- Switch Uvicorn workers to Gunicorn + Uvicorn workers for scaling
- Configure CORS and allowed origins
- Use managed Postgres and Redis
- Set up Celery Beat for periodic jobs (e.g., analytics refresh)