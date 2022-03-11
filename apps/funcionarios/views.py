from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Funcionario


class FuncionariosListView(ListView):
    model = Funcionario
    template_name = 'funcionario_list.html'

    
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)
    

class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']
    template_name = 'funcionario_edit.html'


class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    fields = ['nome', 'departamentos']
    template_name = 'funcionario_delete.html'
    success_url = reverse_lazy('list_funcionarios')
