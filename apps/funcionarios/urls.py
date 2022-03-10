from django.urls import path
from .views import FuncionariosListView


urlpatterns = [
    path(' ', FuncionariosListView.as_view(), name='list_funcionarios')
]