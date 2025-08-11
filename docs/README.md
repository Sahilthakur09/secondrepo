# Influence OS - LinkedIn Personal Branding AI

A full-stack application that autonomously manages a user's LinkedIn presence: profile analysis, trend research, content strategy and generation, engagement optimization, analytics, and automated posting.

## Stack
- Backend: FastAPI, Celery, Redis, PostgreSQL
- AI: OpenAI/Anthropic via modular orchestrator, LangChain-ready
- Frontend: Next.js (scaffold)
- Infra: Docker Compose

## Quickstart
1. Copy environment file:
```
cp .env.example .env
```
2. Start services:
```
docker compose up --build
```
3. Open API docs: http://localhost:8000/api/docs
4. Frontend dev server: http://localhost:3000

## Monorepo Structure
- `apps/backend`: FastAPI app and Celery workers
- `apps/frontend`: Next.js app (scaffold)
- `docs`: documentation
- `infra`: infrastructure helpers

## Key Endpoints
- `GET /api/v1/auth/linkedin/login` - OAuth URL
- `POST /api/v1/auth/linkedin/callback` - Token exchange (mock)
- `POST /api/v1/profile/analyze` - Profile insights
- `POST /api/v1/content/generate` - Content generation
- `POST /api/v1/content/hashtags` - Hashtag suggestions
- `GET /api/v1/calendar` - Content calendar
- `GET /api/v1/analytics/posts` - Post metrics
- `POST /api/v1/schedule` - Schedule a post

## Notes
- LinkedIn API calls are mocked by default. Add credentials and implement client methods to go live.
- Replace the orchestrator with your preferred model and prompt chains.