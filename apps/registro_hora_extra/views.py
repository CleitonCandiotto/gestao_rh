from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm
from django.views.generic.edit import UpdateView, DeleteView, CreateView



class HoraExtraListView(ListView):
    model = RegistroHoraExtra
    template_name = 'hora_extra_list.html'


    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraEditView(UpdateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'funcionario', 'horas']
    template_name = 'hora_extra_edit.html'


class HoraExtraDeleteView(DeleteView):
    model = RegistroHoraExtra
    template_name = 'hora_extra_delete.html'
    success_url = reverse_lazy('list_hora_extra')


class HoraExtraCreateView(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    template_name = 'hora_extra_create.html'


    def get_form_kwargs(self):
        '''
        Func para pegar o user e passar para o formulario para filtrar pela empresa
        '''
        kwargs = super(HoraExtraCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs