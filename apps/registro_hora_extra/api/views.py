from .serializers import RegistroHoraExtraSerializer
from apps.registro_hora_extra.models import RegistroHoraExtra
from rest_framework import viewsets
from rest_framework import permissions


class RegistroHoraExtraViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RegistroHoraExtra.objects.all()
    serializer_class = RegistroHoraExtraSerializer
    permission_classes = [permissions.IsAuthenticated]

