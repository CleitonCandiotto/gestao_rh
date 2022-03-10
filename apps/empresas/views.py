from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa


class EmpresaCreateView(CreateView):
    model = Empresa
    template_name = 'add_empresa.html'
    fields = ['nome']


    def form_valid(self, form):
        """
        Vai linkar o a empresa cadastrada com o funcionario que está logado
        """
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()

        return redirect('home')
        

class EmpresaEditView(UpdateView):
    model = Empresa
    fields = ['nome']
    template_name = 'edit_empresa.html'
