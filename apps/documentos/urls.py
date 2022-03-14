from django.urls import path
from .views import DocumentoCreateView


urlpatterns  = [
    path('create/<int:funcionario_id>/', DocumentoCreateView.as_view(), name='create_documento'),

]