# LinkedIn Personal Branding AI Agent

A full-stack application that autonomously manages a user's LinkedIn presence: analyzes profile, researches trends, generates content, schedules posts, and tracks engagement.

## Quickstart (Docker)

1. Copy env template and edit values:

```bash
cp .env.example .env
```

2. Start services:

```bash
docker compose up --build
```

- Backend: http://localhost:8000 (docs at /docs)
- Frontend: http://localhost:3000

## Tech Stack
- Backend: FastAPI (Python), SQLAlchemy, APScheduler, Redis
- Orchestration: LangChain
- LLMs: OpenAI (configurable)
- Frontend: Next.js (React, TypeScript)
- DB: PostgreSQL (SQLite fallback for local dev)
- Auth: LinkedIn OAuth 2.0
- Containerization: Docker

## Monorepo Structure
```
linkedin-agent/
  backend/
  frontend/
  docker-compose.yml
  README.md
  API.md
  USER_GUIDE.md
  TECH_REPORT.md
  DEPLOYMENT.md
```

## Licensing
MIT