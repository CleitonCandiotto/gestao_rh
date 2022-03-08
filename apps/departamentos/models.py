from statistics import mode
from django.db import models


class Departamento(models.Model):
    nome = models.CharField('Departamento', max_length=70, help_text='Nome do Departamento')

    def __str__(self):
        return self.nome
