from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'usuario {username} creado')

    else:
        form = UserRegisterForm()
    return render(request, 'usuario/registro_usuario.html', {'form' : form})