from typing import Tuple

SENSITIVE_TOPICS = {
    "confidential": "Avoid sharing confidential or proprietary information.",
    "nda": "Do not disclose information protected by NDAs.",
    "politics": "Avoid partisan political endorsements on professional channels.",
}


def check_and_adjust_content(text: str) -> Tuple[str, list[str]]:
    notices: list[str] = []
    lowered = text.lower()
    for keyword, message in SENSITIVE_TOPICS.items():
        if keyword in lowered:
            notices.append(message)
    adjusted = text.strip()
    if notices and not adjusted.endswith("\n"):
        adjusted += "\n"
    if notices:
        adjusted += "\n\nNote: Content adjusted for professional compliance."
    return adjusted, notices