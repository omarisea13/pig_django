   
    # finegap/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'finegap/home.html')

def contacto(request):
    return render(request, 'finegap/contacto.html')

def acerca_de(request):
    return render(request, 'finegap/acerca_de.html')
