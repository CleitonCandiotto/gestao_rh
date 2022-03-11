from django.urls import path
from .views import DepartamentoListView


urlpatterns = [
    path('', DepartamentoListView.as_view(), name='list_departamentos'),
 
    
]