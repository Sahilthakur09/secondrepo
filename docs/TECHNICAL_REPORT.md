# Technical Report

## Architecture Overview
- FastAPI backend with versioned API
- Celery workers for async tasks and scheduling
- PostgreSQL for persistence (roadmap)
- Redis for queue/broker and caching
- Next.js frontend for dashboard

## AI Model Choices
- Default: OpenAI GPT-4 class models (configurable)
- Alternative: Anthropic Claude models
- Orchestration via modular interface, compatible with LangChain

## Implementation Decisions
- Mock LinkedIn client to enable local development
- API-first with OpenAPI docs
- Dockerized services for reproducibility

## Future Work
- Implement full LinkedIn API integration and OAuth flows
- Add database models for users, posts, schedules, analytics
- Add A/B testing framework and reporting
- Add multi-language support and image generation