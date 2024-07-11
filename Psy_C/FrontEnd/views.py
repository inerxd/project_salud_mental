from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def IndexViews(request):
    return render(request,'index.html')

def infoPagina(request):
    return render(request,'infoPagina.html')

def losProblemas(request):
    return render(request,'losProblemas.html')

def inicioSesion(request):
    return render(request,'inicioSesion.html')


