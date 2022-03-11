from statistics import mode
from django.db import models
from apps.empresas.models import Empresa


class Departamento(models.Model):
    nome = models.CharField('Departamento', max_length=70, help_text='Nome do Departamento')
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
