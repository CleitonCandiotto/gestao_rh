from django.views.generic.list import ListView
from django.http import HttpResponse
from .models import Funcionario


class FuncionariosListView(ListView):
    model = Funcionario

    
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)
    
