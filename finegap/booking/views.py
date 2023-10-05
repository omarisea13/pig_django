from django.shortcuts import render, redirect
from .forms import FormularioContacto

def home(request):
    return render(request, 'booking/home.html')

def acerca_de(request):
    return render(request, 'booking/acerca_de.html')

def destinos(request, destino):
     return render(request, "booking/destinos.html", {
        "destino": destino
    })
     
def contacto(request):
    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            # Procesar el formulario si es válido
            Nombre = form.cleaned_data['Nombre']
            Email = form.cleaned_data['Email']
            Mensaje = form.cleaned_data['Mensaje']
            return redirect('home')
    else:
        form = FormularioContacto()

    return render(request, 'booking/contacto.html', {'form': form})