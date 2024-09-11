from django.shortcuts import render

# Create your views here.
def dasbord(request):
    return render(request,'dasbord.html')