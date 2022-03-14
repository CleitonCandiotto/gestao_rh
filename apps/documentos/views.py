from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Documento



class DocumentoCreateView(CreateView):
    model = Documento
    fields = ['descricao', 'documento']
    template_name = 'documento_create.html'


    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['funcionario_id']    


        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

