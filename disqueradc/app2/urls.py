from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('',views.inicio,name='inicio'), #cada path es una ruta
    path('pagina2', views.pagina2, name='pagina2'),
    #artista
    path('artista',views.artista,name='artista'),
    path('artista/add',views.addartista,name='artista-add'),
    path('artista/edit',views.editartista, name='edit-artista'),
    
    #disquera
    path('disquera',views.disquera,name='disquera'),
    path('disquera/add',views.adddisquera,name='disquera-add'),
    path('disquera/edit',views.editdisquera, name='edit-disquera'),
    path('disquera/elim',views.elimdisquera, name='elim-disquera'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)