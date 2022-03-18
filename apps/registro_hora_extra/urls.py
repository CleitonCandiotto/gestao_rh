from unicodedata import name
from django.urls import path
from .views import HoraExtraListView, HoraExtraEditView, HoraExtraDeleteView, HoraExtraCreateView, HoraExtraBaseEditView


urlpatterns = [
    path('', HoraExtraListView.as_view(), name='list_hora_extra'),
    path('edit-funcionario/<int:pk>/', HoraExtraEditView.as_view(), name='edit_hora_extra'),
    path('edit/<int:pk>/', HoraExtraBaseEditView.as_view(), name='edit_hora_extra_base'),
    path('delete/<int:pk>/', HoraExtraDeleteView.as_view(), name='delete_hora_extra'),
    path('create/', HoraExtraCreateView.as_view(), name='create_hora_extra')  
]