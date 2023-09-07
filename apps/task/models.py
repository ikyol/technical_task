from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator_tasks")
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_tasks")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> models.CharField:
        return self.title

    class Meta:
        app_label = "task"


class Role(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField()

    def __str__(self) -> models.CharField:
        return self.name

    class Meta:
        app_label = "task"
