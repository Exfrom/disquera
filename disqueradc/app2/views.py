import array
from django.shortcuts import render
from django.http import HttpResponse
from .models import Disquera
from .models import Artista
# Create your views here.


# Create your views here.
def inicio(request):#vista 1
    return HttpResponse("<h1>inicio disquera</h1>")

def pagina2(request):
    return render(request, 'views/pagina2.html')

#artista
def artista(request): #vista inicio artistas
    artistas=Artista.objects.all()
    return render(request,'artistas/index.html',{'artistas':artistas})

def addartista(request):
    return render(request,'artistas/crear.html')

def editartista(request):
    return render(request, 'artistas/editar.html')

#disquera
def disquera(request):
    disqueras=Disquera.objects.all()
    #print(Disqueras)
    return render(request, 'disquera/index.html',{'disqueras':disqueras})

def adddisquera(request):
    return render(request,'disquera/crear.html')

def editdisquera(request):
    return render(request, 'disquera/editar.html')

def elimdisquera(request):
    return render(request, 'disquera/eliminar.html')