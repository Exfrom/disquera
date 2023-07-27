from django.db import models
# Create your models here.
class Disquera(models.Model):
    id=models.AutoField(primary_key=True)
    nitdisquera=models.CharField(max_length=25)
    nombredisquera=models.CharField(max_length=100)
    telefonodisquera=models.CharField(max_length=15)
    direcciondisquera=models.CharField(max_length=100)
    estadodisquera=models.BooleanField()
    
class Artista(models.Model):
    id=models.AutoField(primary_key=True)
    noDocumento=models.CharField(max_length=25)
    tipoDocumento=models.CharField(max_length=25)
    nombreArtista=models.CharField(max_length=50)
    apellidosArtista=models.CharField(max_length=50)
    fNacimiento=models.DateField
    emailArtista=models.CharField(max_length=100)
    fotoArtista=models.CharField(max_length=255)
    iddisquerafk=models.ForeignKey(Disquera,on_delete=models.CASCADE)
    estadoArtista=models.BooleanField()
    
class Cancion(models.Model):
    id=models.AutoField(primary_key=True)
    nombreCancion=models.CharField(max_length=100)
    duracionCancion=
    idAlbumFK=
    estadoCancion=models.BooleanField()
    
class Album(models.Model):
    id=models.AutoField(primary_key=True)
    nombreAlbum=models.CharField(max_length=100)
    anioPublicacion=models.CharField(max_length=10)
    idArtistaFK=
    idGeneroFK=
    fotoAlbum=models.CharField(max_length=255)
    estadoAlbum=models.BooleanField()
    
class Genero(models.Model):
    id=models.AutoField(primary_key=True)
    nombreGenero=models.CharField(max_length=100)
    estadoGenero=models.BooleanField()
    
    