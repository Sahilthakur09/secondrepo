from typing import Dict, Any


class LinkedInClient:
    def __init__(self, access_token: str | None = None, mock: bool = True) -> None:
        self.access_token = access_token
        self.mock = mock or not bool(access_token)

    def post_text_update(self, body: str) -> Dict[str, Any]:
        if self.mock:
            return {"status": "ok", "post_id": "mock-123", "body": body[:140]}
        # TODO: Implement LinkedIn API call
        raise NotImplementedError

    def fetch_post_metrics(self, post_id: str) -> Dict[str, Any]:
        if self.mock:
            return {"post_id": post_id, "likes": 42, "comments": 5, "shares": 3, "impressions": 1200}
        raise NotImplementedError