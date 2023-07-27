from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# Create your views here.
def inicio(request):#vista 1
    return HttpResponse("<h1>inicio disquera</h1>")

def pagina2(request):
    return render(request, 'views/pagina2.html')

#artista
def artista(request): #vista inicio artistas
     return render(request,'artistas/index.html')

def addartista(request):
    return render(request,'artistas/crear.html')

def editartista(request):
    return render(request, 'artistas/editar.html')

#disquera
def disquera(request):
    return render(request, 'disquera/index.html')

def adddisquera(request):
    return render(request,'disquera/crear.html')

def editdisquera(request):
    return render(request, 'disquera/editar.html')

def elimdisquera(request):
    return render(request, 'disquera/eliminar.html')