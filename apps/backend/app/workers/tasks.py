from .celery_app import celery_app
from ..services.linkedin_client import LinkedInClient


@celery_app.task(name="post_to_linkedin")
def post_to_linkedin(body: str) -> dict:
    client = LinkedInClient(mock=True)
    return client.post_text_update(body)


@celery_app.task(name="compute_metrics")
def compute_metrics(post_id: str) -> dict:
    client = LinkedInClient(mock=True)
    return client.fetch_post_metrics(post_id)