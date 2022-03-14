from unicodedata import name
from django.urls import path
from .views import HoraExtraListView


urlpatterns = [
    path('', HoraExtraListView.as_view(), name='list_hora_extra'),
    #path('edit/<int:pk>/', FuncionarioUpdateView.as_view(), name='edit_funcionario'),
    #path('delete/<int:pk>/', FuncionarioDeleteView.as_view(), name='delete_funcionario'),
    #path('create/', FuncionarioCreateView.as_view(), name='create_funcionario')
    
]