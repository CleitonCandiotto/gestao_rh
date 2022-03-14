from unicodedata import name
from django.urls import path
from .views import (
    DepartamentoListView, 
    DepartamentoCreateView, 
    DepartamentoEditView,
    DepartamenteDeleteView
    )


urlpatterns = [
    path('', DepartamentoListView.as_view(), name='list_departamentos'),
    path('create/', DepartamentoCreateView.as_view(), name='create_departamento'),
    path('edit/<int:pk>/', DepartamentoEditView.as_view(), name='edit_departamento'),
    path('delete/<int:pk>/', DepartamenteDeleteView.as_view(), name='delete_departamento')
]