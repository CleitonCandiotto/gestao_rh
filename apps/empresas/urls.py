from django.urls import path
from .views import EmpresaCreateView, EmpresaEditView


urlpatterns  = [
    path('add/', EmpresaCreateView.as_view(), name='add_empresa'),
    path('edit/<int:pk>/', EmpresaEditView.as_view(), name='edit_empresa' )
]