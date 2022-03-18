from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa
from django.urls import reverse
from django.db.models import Sum



class Funcionario(models.Model):
    nome = models.CharField('Funcionario', max_length=100, help_text='Nome Funcionario')
    user = models.OneToOneField(User, models.PROTECT)
    departamentos = models.ManyToManyField(Departamento) # um funcionario pode estar em vários departamentos
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)
    

    def __str__(self) :
        return self.nome


    def get_absolute_url(self):
        return reverse('list_funcionarios')


    @property
    def total_hora_extra(self):
        total = self.registrohoraextra_set.all().aggregate(Sum('horas'))['horas__sum']
        return total
        