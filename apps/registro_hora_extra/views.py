import json
import csv
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
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
    form_class = RegistroHoraExtraForm
    template_name = 'hora_extra_edit.html'


    def get_form_kwargs(self):
        '''
        Func para pegar o user e passar para o formulario para filtrar pela empresa
        '''
        kwargs = super(HoraExtraEditView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraBaseEditView(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    template_name = 'hora_extra_edit.html'


    def get_success_url(self):
        return reverse_lazy('edit_hora_extra_base', args=[self.object.id] )


    def get_form_kwargs(self):
        '''
        Func para pegar o user e passar para o formulario para filtrar pela empresa
        '''
        kwargs = super(HoraExtraBaseEditView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


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
        

class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):
        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = True
        registro_hora_extra.save()

        funcionario = self.request.user.funcionario


        response = json.dumps(
            {'mensagem': 'Hora extra Marcada como Usada',
             'horas': float(funcionario.total_hora_extra)
             }
            )

        return HttpResponse(response, content_type='application/json')


class DesmarcouHoraExtra(View):
    def post(self, *args, **kwargs):
        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = False
        registro_hora_extra.save()

        funcionario = self.request.user.funcionario

        response = json.dumps(
            {'mensagem': 'Hora Extra Desmarcada como Usada',
             'horas': float(funcionario.total_hora_extra)
             }
            )

        return HttpResponse(response, content_type='application/json')


class ExportarCsv(View):
    def get(self, request):
        response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
        )

        registro_he = RegistroHoraExtra.objects.filter(utilizada=False)

        writer = csv.writer(response)
        writer.writerow(['id', 'funcionario', 'Motivo', 'Horas', 'Total horas'])

        for registro in registro_he:
            writer.writerow([
                registro.id, 
                registro.funcionario, 
                registro.motivo, 
                registro.horas, 
                registro.funcionario.total_hora_extra
                ])

        return response