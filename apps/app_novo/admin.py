from django.contrib import admin
from .models import TesteNovo


@admin.register(TesteNovo)
class TesteNovoAdmin(admin.ModelAdmin):
    list_display = ['teste_novo',]
