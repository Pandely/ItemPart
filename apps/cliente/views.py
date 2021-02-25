from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ClienteForm
from .models import Cliente


class ClienteList(ListView):
    model = Cliente
    template_name = 'cliente/listarCliente.html'


class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/crearCliente.html'
    success_url = reverse_lazy('listarCliente')


class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/crearCliente.html'
    success_url = reverse_lazy('listarCliente')


class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'cliente/eliminarCliente.html'
    success_url = reverse_lazy('listarCliente')
