from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')

# Create your views here.
