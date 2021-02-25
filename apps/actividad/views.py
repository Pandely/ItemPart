"""from Tools.scripts.var_access_benchmark import C"""
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.actividad.forms import ActividadForm
from apps.actividad.models import Actividad
# Create your views here.

def index(request):

    return render(request, 'actividad/index_actividad.html')

def actividad_add(request):
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('actividadIndex:index')
    else:
        form = ActividadForm()
    return render(request, 'actividad/actividad_form.html', {'form': form})

def actividad_list(request):
    actividad = Actividad.objects.all()
    contexto = {'actividad':actividad}
    return render(request, 'actividad/actividad_list.html', contexto)

def actividad_edit(request, id_actividad):
    actividad = Actividad.objects.get(id=id_actividad)
    if request.method == 'GET':
        form = ActividadForm(instance=actividad)
    else:
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('actividad_listar')
    return render(request, 'actividad/actividad_form.html', {'form':form})

def actividad_delete(request, id_cliente):
    actividad = Actividad.objects.get(id=id_cliente)
    if request.method == 'POST':
        actividad.delete()
        return redirect('actividad_listar')
    return render(request, 'actividad/actividad_delete.html', {'actividad': actividad})


class actividadList(ListView):
    model = Actividad
    template_name = 'actividad/actividad_list.html'

class actividadCreate(CreateView):
    model = Actividad
    form_class = ActividadForm
    template_name = 'actividad/actividad_form.html'
    success_url = reverse_lazy('actividad_listar')

class actividadUpdate(UpdateView):
    model = Actividad
    form_class = ActividadForm
    template_name = 'actividad/actividad_form.html'
    success_url = reverse_lazy('actividad_listar')

class actividadDelete(DeleteView):
    model = Actividad
    form_class = ActividadForm
    template_name = 'actividad/actividad_delete.html'
    success_url = reverse_lazy('actividad_listar')



