from celery import Celery

celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)
celery_app.conf.timezone = "Asia/Kolkata"
celery_app.conf.beat_schedule = {
    "send-email-every-minute": {
        "task": "tasks.send_email",
        "schedule": 60.0,
        "args": ("venu@example.com",),
    },
}