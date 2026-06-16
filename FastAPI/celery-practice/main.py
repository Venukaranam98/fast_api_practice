from fastapi import FastAPI
from tasks import send_email

app = FastAPI()


@app.get("/send-email")
def trigger_email():
    task = send_email.delay("venu@example.com")

    return {
        "message": "Email task added to queue",
        "task_id": task.id
    }