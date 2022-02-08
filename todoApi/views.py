from rest_framework.permissions import IsAuthenticated

from .models import Task
from rest_framework import viewsets


# with Django rest_framework viewsets
from .serializers import TaskSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
