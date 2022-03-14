from statistics import mode
from django.db import models
from apps.funcionarios.models import Funcionario
from django.urls import reverse


class Documento(models.Model):
    descricao = models.CharField('Descrição', max_length=70, help_text='Descrição do Documento')
    # um documento pode pertencer para um empregado
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT) 
    documento = models.FileField('Documento', upload_to='documentos')


    def __str__(self):
        return self.descricao

    
    def get_absolute_url(self):
        return reverse('edit_funcionario', args=[self.pertence.id])
        
