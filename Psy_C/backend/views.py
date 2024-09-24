from django.shortcuts import render,redirect
from backend.models import Indentificador

# Create your views here.
def dasbord(request):
    return render(request,'dasbord.html')

def ingresoUser(request):
    if request.method == 'POST':
        ingresarUser = request.POST['email']
        ingresarUser2 = request.POST['password']
        

        datosUser = Indentificador(
            email = ingresarUser ,
             password = ingresarUser2
        )

        datosUser.save()
        print(datosUser)
        return redirect('los_problemas')
        