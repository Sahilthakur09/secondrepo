# API Documentation

Base URL: `http://localhost:8000/api/v1`

## Auth
- GET `/auth/linkedin/login`
  - Response: `{ authorization_url: string }`
- POST `/auth/linkedin/callback`
  - Body: `{ code: string, state: string }`
  - Response: `{ access_token: string, refresh_token?: string, expires_in?: number }`

## Profile
- POST `/profile/analyze`
  - Body: `{ headline, summary, experience[], skills[], interests[] }`
  - Response: `{ strengths[], brand_voice, content_pillars[] }`

## Content
- POST `/content/generate`
  - Body: `{ industry, role, interests[], brand_voice, format, topic_hint?, language }`
  - Response: `{ title?, body, hashtags[], call_to_action?, compliance_notices[] }`
- POST `/content/hashtags`
  - Body: `{ topic, industry, max_hashtags }`
  - Response: `{ hashtags[] }`

## Research
- POST `/research/trends`
  - Body: `{ industry, role?, language }`
  - Response: `[{ topic, summary, sources[] }]`

## Calendar
- GET `/calendar/`
  - Response: `CalendarItem[]`

## Analytics
- GET `/analytics/posts`
  - Response: `PostMetric[]`

## Schedule
- POST `/schedule/`
  - Body: `{ content_body, scheduled_time }`
  - Response: `{ id, content_body, scheduled_time, status }`
- GET `/schedule/`
  - Response: `[{ id, content_body, scheduled_time, status }]`