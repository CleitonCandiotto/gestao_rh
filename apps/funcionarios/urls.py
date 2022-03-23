from unicodedata import name
from django.urls import path
from .views import (
    FuncionarioUpdateView, 
    FuncionariosListView, 
    FuncionarioDeleteView, 
    FuncionarioCreateView,
    render_pdf_view
    )


urlpatterns = [
    path('', FuncionariosListView.as_view(), name='list_funcionarios'),
    path('edit/<int:pk>/', FuncionarioUpdateView.as_view(), name='edit_funcionario'),
    path('delete/<int:pk>/', FuncionarioDeleteView.as_view(), name='delete_funcionario'),
    path('create/', FuncionarioCreateView.as_view(), name='create_funcionario'),
    path('pdf-relatorio/<int:pk>/', render_pdf_view, name='pdf_relatorio'),
    
]