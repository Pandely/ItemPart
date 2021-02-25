from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from apps.cliente.views import ClienteList, ClienteCreate, ClienteUpdate, ClienteDelete

urlpatterns = [
    url(r'^crearCliente/$', login_required(ClienteCreate.as_view()), name='crearCliente'),
    url(r'^listarCliente/$', login_required(ClienteList.as_view()), name='listarCliente'),
    url(r'^editarCliente/(?P<pk>\d+)/$', login_required(ClienteUpdate.as_view()), name='editarCliente'),
    url(r'^eliminarCliente/(?P<pk>\d+)/$', login_required(ClienteDelete.as_view()), name='eliminarCliente')
]

