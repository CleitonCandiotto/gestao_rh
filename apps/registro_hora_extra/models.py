from django.db import models
from apps.funcionarios.models import Funcionario
from django.urls import reverse


class RegistroHoraExtra(models.Model):
    motivo = models.CharField('Motivo', max_length=100, help_text='Motivo da Hora Extra')
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    horas = models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        return self.motivo


    def get_absolute_url(self):
        return reverse('list_hora_extra')



