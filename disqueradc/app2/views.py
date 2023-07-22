from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# Create your views here.
def inicio(request):#vista 1
    return HttpResponse("<h1>inicio disquera</h1>")

def pagina2(request):
    return render(request, 'views/pagina2.html')

def artista(request): #vista inicio artistas
     return render(request,'artistas/index.html')

def addartista(request):
    return render(request,'artistas/crear.html')

def editartista(request):
    return render(request, 'artistas/editar.html')