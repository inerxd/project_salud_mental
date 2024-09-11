from django.shortcuts import render
from backend.models import Indentificador,TypeUser
from backend.views import dasbord

#from django.http import HttpResponse

# Create your views here.
# aqui creo el codigo para crear las vista y llamarlos en el main proyecto urls.py
def IndexViews(request):
    return render(request,'index.html')

def Nosostros(request):
    return render(request,'nosotros.html')

def losProblemas(request):
    return render(request,'losProblemas.html')

def inicioSesion(request):
    if request.method == 'GET':
        return render(request,'inicioSesion.html')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Buscar el usuario por email
        identificadores = Indentificador.objects.filter(email=email)
        
        if identificadores.exists():
            identificador = identificadores.first()
            
            # Verificar la contraseña directamente (deberías usar hashing en producción)
            if password == identificador.password:
                
                
                # Verificar el tipo de usuario
                if identificador.TypeUserId.id == 1:
                    # Redirigir a la vista de administrador
                   return render(request, dasbord(request))
                else:
                    # Usuario no es administrador
                    return render(request,'inicioSesion.html')
            else:
                # Contraseña incorrecta
                return render(request,'inicioSesion.html')
        else:
            # El email no existe
            return render(request,'inicioSesion.html')

def signUp(request):
    return render(request,'signUp.html')


            
       




