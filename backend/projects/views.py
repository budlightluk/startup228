from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# from django_filters.rest_framework import DjangoFilterBackend  # закомментируйте эту строку
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.prefetch_related('tasks', 'members').select_related('creator')
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    # filter_backends = [DjangoFilterBackend]  # закомментируйте эту строку
    # filterset_fields = ['status', 'project', 'assigned_to']  # закомментируйте эту строку
