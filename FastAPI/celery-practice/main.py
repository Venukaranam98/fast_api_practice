from fastapi import FastAPI
from celery_app import celery_app

from tasks import send_email

app = FastAPI()


@app.get("/send-email")
def trigger_email():
    task = send_email.delay("venu@example.com")

    return {
        "message": "Email task added to queue",
        "task_id": task.id
    }


@app.get("/task-status/{task_id}")
def get_task_status(task_id: str):
    task = celery_app.AsyncResult(task_id)

    return {
        "task_id": task.id,
        "status": task.status,
        "result": task.result
    }

@app.get("/send-email-later")
def send_email_later():
    task = send_email.apply_async(
        args=["venu@example.com"],
        countdown=10
    )

    return {
        "message": "Email scheduled",
        "task_id": task.id
    }