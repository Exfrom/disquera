from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'), #cada path es una ruta
    path('pagina2', views.pagina2, name='pagina2')
]