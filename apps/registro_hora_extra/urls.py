from django.urls import path
from .views import (
    HoraExtraListView, 
    HoraExtraEditView, 
    HoraExtraDeleteView, 
    HoraExtraCreateView, 
    HoraExtraBaseEditView,
    UtilizouHoraExtra,
    DesmarcouHoraExtra,
    ExportarCsv,
    ExportarExcel  
)


urlpatterns = [
    path('', HoraExtraListView.as_view(), name='list_hora_extra'),
    path('edit-funcionario/<int:pk>/', HoraExtraEditView.as_view(), name='edit_hora_extra'),
    path('edit/<int:pk>/', HoraExtraBaseEditView.as_view(), name='edit_hora_extra_base'),
    path('utilizou-hora-extra/<int:pk>/', UtilizouHoraExtra.as_view(), name='utilizou_hora_extra'),
    path('desmarcou-hora-extra/<int:pk>/', DesmarcouHoraExtra.as_view(), name='desmarcou_hora_extra'),
    path('delete/<int:pk>/', HoraExtraDeleteView.as_view(), name='delete_hora_extra'),
    path('create/', HoraExtraCreateView.as_view(), name='create_hora_extra'),
    path('exportar-csv/', ExportarCsv.as_view(), name='exportar_csv'),
    path('exportar-excel/', ExportarExcel.as_view(), name='exportar_excel')  
  
]