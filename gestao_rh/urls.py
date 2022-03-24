
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from core import views
from apps.funcionarios.api.views import FuncionarioViewSet
from apps.registro_hora_extra.api.views import RegistroHoraExtraViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'api/funcionarios', FuncionarioViewSet)
router.register(r'api/horas-extras', RegistroHoraExtraViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('funcionarios/', include('apps.funcionarios.urls'), name='funcionarios'),
    path('empresas/', include('apps.empresas.urls'), name='empresas'),
    path('departamentos/', include('apps.departamentos.urls'), name='departamentos'),
    path('documentos/', include('apps.documentos.urls'), name='documentos'),
    path('horas-extras/', include('apps.registro_hora_extra.urls'), name='hora_extras'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
