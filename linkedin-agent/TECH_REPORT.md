# Technical Report

## Architecture Overview
- Monorepo with FastAPI backend, Next.js frontend, PostgreSQL, Redis
- Background scheduler for automated posting and analytics sync
- LinkedIn OAuth for account connection
- LLM-powered services for analysis, research, and content creation

## AI Model Choices
- OpenAI GPT-4o-mini for generation and optimization
- Optional moderation endpoint for safety filtering
- LangChain for prompt templates and chains

## Key Implementation Decisions
- SQLAlchemy ORM with PostgreSQL (SQLite fallback for local dev)
- APScheduler for reliable timed jobs without heavy worker overhead
- Typed Pydantic schemas for input/output contracts

## Data Schema (high level)
- User: id, linkedin_id, tokens, preferences
- Post: id, user_id, content, type, status, scheduled_at, platform_id
- Analytics: id, post_id, impressions, likes, comments, shares, created_at

## Security & Compliance
- Store OAuth tokens encrypted at rest
- Rate limiting and request validation
- Safety filters on generated content

## Limitations & Future Work
- Deeper competitor analysis
- Multi-language support and cross-platform syndication
- Rich carousel/article editors