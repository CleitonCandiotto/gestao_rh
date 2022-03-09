from statistics import mode
from django.db import models
from apps.funcionarios.models import Funcionario


class Documento(models.Model):
    descricao = models.CharField('Descrição', max_length=70, help_text='Descrição do Documento')
    # um documento pode pertencer para um empregado
    pertence = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING) 


    def __str__(self):
        return self.descricao
