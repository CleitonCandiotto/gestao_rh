from statistics import mode
from django.db import models

class TesteNovo(models.Model):
    teste_novo = models.CharField(max_length=200)
