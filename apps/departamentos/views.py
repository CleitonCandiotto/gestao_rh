from pyexpat import model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Departamento


class DepartamentoListView(ListView):
    model = Departamento
    template_name = 'departamento_list.html'


    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)


class DepartamentoCreateView(CreateView):
    model = Departamento
    template_name = 'departamento_create.html'
    fields = ['nome']


    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoCreateView, self).form_valid(form)


class DepartamentoEditView(UpdateView):
    model = Departamento
    fields = ['nome']
    template_name = 'departamento_edit.html'


class DepartamenteDeleteView(DeleteView):
    model = Departamento
    fields = ['nome']
    template_name = 'departamento_delete.html'
    success_url = reverse_lazy('list_departamentos')
