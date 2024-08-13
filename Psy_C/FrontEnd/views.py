from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
# aqui creo el codigo para crear las vista y llamarlos en el main proyecto urls.py
def IndexViews(request):
    return render(request,'index.html')

def infoPagina(request):
    return render(request,'infoPagina.html')

def losProblemas(request):
    return render(request,'losProblemas.html')

def inicioSesion(request):
    return render(request,'inicioSesion.html')

def prueba(request):
    return render(request,'prueba.html')


