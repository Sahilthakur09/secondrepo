from __future__ import annotations
import os
from typing import List, Tuple
from openai import OpenAI
from ..config import get_settings

_settings = get_settings()
_client = OpenAI(api_key=_settings.openai_api_key) if _settings.openai_api_key else None
_MODEL = "gpt-4o-mini"


def _ensure_client():
    if _client is None:
        raise RuntimeError("OPENAI_API_KEY not configured")


def analyze_profile_text(profile_text: str) -> Tuple[List[str], List[str], str]:
    if _client is None:
        # Fallback deterministic output for demo
        return (["Clear domain expertise", "Strong communication"], ["More case studies"], "Helpful, pragmatic, concise")
    prompt = (
        "Analyze the following LinkedIn profile summary. Return strengths (bullet list), gaps (bullet list), and a 1-sentence brand voice.\n\n"
        f"PROFILE:\n{profile_text}"
    )
    response = _client.chat.completions.create(
        model=_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    text = response.choices[0].message.content or ""
    strengths = [line[2:].strip() for line in text.splitlines() if line.strip().startswith("-")][:3]
    gaps = ["Add quantified outcomes", "Publish long-form content"]
    voice = "Credible, friendly, outcome-focused"
    return strengths or ["Credibility"], gaps, voice


def suggest_hashtags(industry: str | None, topics: List[str]) -> List[str]:
    base = ["#LinkedIn", "#PersonalBranding", "#Career"]
    topical = [f"#{t.title().replace(' ', '')}" for t in topics[:3]]
    return list(dict.fromkeys(base + topical))[:8]


def generate_content(post_type: str, prompt: str, language: str = "en") -> Tuple[str, List[str]]:
    if _client is None:
        content = f"[{post_type.upper()}] {prompt}\n\nHook: A provocative opening...\n\nBody: Three key insights...\n\nCTA: What do you think?"
        return content, suggest_hashtags(None, ["growth", "leadership", "ai"])
    system = (
        "You are a LinkedIn content strategist. Create engaging, platform-native posts with strong hooks, clear structure, and a CTA. Keep within LinkedIn norms."
    )
    response = _client.chat.completions.create(
        model=_MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": f"Type: {post_type}\nLanguage: {language}\nPrompt: {prompt}"},
        ],
        temperature=0.7,
        max_tokens=600,
    )
    content = response.choices[0].message.content or ""
    return content, suggest_hashtags(None, ["growth", "leadership", "ai"])


def optimize_content(content: str) -> Tuple[str, List[str], List[str]]:
    if _client is None:
        return content + "\n\nImproved hook and clear CTA added.", suggest_hashtags(None, ["optimization"]), ["Shorten sentences", "Front-load value"]
    response = _client.chat.completions.create(
        model=_MODEL,
        messages=[
            {"role": "system", "content": "Improve the post for LinkedIn engagement while keeping voice consistent."},
            {"role": "user", "content": content},
        ],
        temperature=0.4,
        max_tokens=400,
    )
    improved = response.choices[0].message.content or content
    return improved, suggest_hashtags(None, ["engagement"]), ["Clarify hook", "Stronger CTA"]


def generate_strategy(industry: str | None, role: str | None, interests: List[str], frequency_per_week: int):
    pillars = interests[:5] or ["Leadership", "AI", "Career Growth"]
    from datetime import datetime, timedelta

    days = max(1, frequency_per_week)
    calendar = []
    now = datetime.utcnow()
    for i in range(14):
        calendar.append({
            "date": (now + timedelta(days=i)).isoformat(),
            "post_type": ["text", "carousel", "article"][i % 3],
            "topic": (pillars[i % len(pillars)]),
        })
    return pillars, calendar


def generate_trends(industry: str | None) -> List[dict]:
    topics = [
        {"topic": "AI tooling impact", "summary": "How small teams ship faster with AI."},
        {"topic": "Personal branding", "summary": "Leaders building trust through transparency."},
        {"topic": "Hiring trends", "summary": "Skills-based hiring gains traction."},
    ]
    return topics