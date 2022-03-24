from apps.funcionarios.models import Funcionario 
from rest_framework import serializers


class FuncinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['nome', 'user', 'departamentos', 'empresa']