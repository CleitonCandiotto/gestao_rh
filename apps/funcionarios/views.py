from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Funcionario
from django.contrib.auth.models import User

#lib pdf
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa



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


class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos', 'foto']
    template_name = 'funcionario_create.html'


    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioCreateView, self).form_valid(form)


def render_pdf_view(request, *args, **kwargs):
    template_path = 'pdf_funcionario.html'
    funcionario = Funcionario.objects.get(id=kwargs['pk'])
    context = {'funcionario': funcionario}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="funcionario.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
    html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response