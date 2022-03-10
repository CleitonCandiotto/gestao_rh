from django.views.generic.list import ListView
from django.http import HttpResponse
from .models import Funcionario


class FuncionariosListView(ListView):
    model = Funcionario
    
