from apps.funcionarios.models import Funcionario 
from rest_framework import serializers
from apps.registro_hora_extra.api.serializers import RegistroHoraExtraSerializer


class FuncinarioSerializer(serializers.ModelSerializer):
    registrohoraextra_set = RegistroHoraExtraSerializer(many=True)

    class Meta:
        model = Funcionario
        fields = ['nome', 'user', 'departamentos', 'empresa', 'registrohoraextra_set']