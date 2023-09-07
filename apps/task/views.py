from django.db.models import Q
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Role, Task
from .serializers import RoleSerializer, TaskSerializer
from . import tasks


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAdminUser]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self) -> Task:
        user = self.request.user
        return Task.objects.filter(Q(created_by=user) | Q(assigned_to=user))

    def perform_create(self, serializer: TaskSerializer) -> None:
        serializer.save(created_by=self.request.user)
        assigned_to = serializer.validated_data.get("assigned_to")
        from loguru import logger
        logger.info(f"Assignee {assigned_to}")
        if assigned_to:
            tasks.send_task_assignment_email.delay(serializer.instance.id, assigned_to.email)
