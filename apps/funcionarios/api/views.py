from .serializers import FuncinarioSerializer
from apps.funcionarios.models import Funcionario
from rest_framework import viewsets
from rest_framework import permissions


class FuncionarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Funcionario.objects.all()
    serializer_class = FuncinarioSerializer
    permission_classes = [permissions.IsAuthenticated]

