from django.contrib import admin
from .models import Teste, RegistroUsuario


@admin.register(Teste)
class TesteAdmin(admin.ModelAdmin):
    list_display = ['descricao',]


@admin.register(RegistroUsuario)
class RegistroUsuarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'idade', 'salario']
