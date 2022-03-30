from django.contrib import admin
from .models import Teste


@admin.register(Teste)
class TesteAdmin(admin.ModelAdmin):
    list_display = ['descricao',]

