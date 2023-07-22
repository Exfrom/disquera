from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'), #cada path es una ruta
    path('pagina2', views.pagina2, name='pagina2'),
    path('artista', views.artista, name='artista'),
    path('artista/add', views.artista, name='artista-add'),
    path('artista/editar', views.editartista, name='edit')
]