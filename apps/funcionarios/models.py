from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento



class Funcionario(models.Model):
    nome = models.CharField('Funcionario', max_length=100, help_text='Nome Funcionario')
    user = models.ForeignKey(User, models.PROTECT)
    departamentos = models.ManyToManyField(Departamento) # um funcionario pode estar em vários departamentos

    
    def __str__(self) :
        return self.nome
