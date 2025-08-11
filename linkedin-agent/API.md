# API Overview

Base URL: `${APP_BASE_URL}` (default http://localhost:8000)

OpenAPI docs: `/docs` and `/redoc`

## Auth
- GET `/api/auth/linkedin/login` → Redirect URL for LinkedIn OAuth
- GET `/api/auth/linkedin/callback` → OAuth callback; stores tokens

## User & Profile
- GET `/api/user/me` → Current user
- POST `/api/profile/analyze` → Analyze LinkedIn profile and return strengths, gaps, brand voice

## Industry & Trends
- GET `/api/trends` → Latest industry trends for user profile

## Content
- POST `/api/content/strategy` → Generate content pillars and calendar
- POST `/api/content/generate` → Generate post(s) by type (text, carousel, article, poll)
- POST `/api/content/optimize` → Optimize post for engagement; suggest hashtags
- POST `/api/content/schedule` → Schedule a post
- GET `/api/content/calendar` → List scheduled posts

## Analytics
- GET `/api/analytics/summary` → Engagement summary
- GET `/api/analytics/posts` → Per-post metrics
- POST `/api/analytics/abtest` → Start A/B test between variants

## Admin/Jobs
- POST `/api/jobs/sync_analytics` → Fetch latest analytics from LinkedIn

Authentication method TBD (cookie/session). Some endpoints require OAuth completed.