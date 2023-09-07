from celery import shared_task
from django.core.mail import send_mail

from .models import Task


@shared_task
def send_task_assignment_email(task_id: int, assigned_to_email: str) -> None:
    task = Task.objects.get(id=task_id)
    subject = "Вы назначены на новую задачу"
    message = f"Вам назначена новая задача: {task.title}"
    from_email = "your_email@example.com"
    recipient_list = [assigned_to_email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
