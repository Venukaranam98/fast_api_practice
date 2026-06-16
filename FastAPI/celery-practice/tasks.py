from celery_app import celery_app
import time


@celery_app.task
def send_email(email: str):
    print(f"Sending email to {email}...")

    time.sleep(5)

    print("Email sent!")

    return f"Email sent to {email}"