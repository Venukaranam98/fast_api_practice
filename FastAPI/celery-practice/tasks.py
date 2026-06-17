from celery_app import celery_app
import random
import time


@celery_app.task(
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 3},
)
def send_email(email: str):
    print(f"Sending email to {email}...")

    time.sleep(2)

    if random.choice([True, False]):
        raise Exception("Email service unavailable")

    print("Email sent!")

    return f"Email sent to {email}"