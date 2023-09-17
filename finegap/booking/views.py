   
    # finegap/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'booking/home.html')

def contacto(request):
    return render(request, 'booking/contacto.html')

def acerca_de(request):
    return render(request, 'booking/acerca_de.html')

def destinos(request, destino):
     return render(request, "booking/destinos.html", {
        "destino": destino
    })