from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from apps.actividad.views import actividadCreate, actividadList, actividadDelete, actividadUpdate

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nuevo$', login_required(actividadCreate.as_view()), name='actividad_crear'),
    url(r'^listar/$', login_required(actividadList.as_view()), name='actividad_listar'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(actividadUpdate.as_view()), name='actividad_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(actividadDelete.as_view()), name='actividad_eliminar')
]
