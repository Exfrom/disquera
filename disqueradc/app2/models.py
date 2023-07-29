from django.db import models
# Create your models here.
class Disquera(models.Model):
    id = models.AutoField(primary_key=True)
    nitdisquera = models.CharField(max_length=25)
    nombredisquera = models.CharField(max_length=100)
    telefonodisquera = models.CharField(max_length=15)
    direcciondisquera = models.CharField(max_length=100)
    estadodisquera = models.BooleanField()
    acciones=models.CharField(max_length=100)
    
    
    def __str__(self):
        row="Disquera: =" +self.nombredisquera
        return row

class Artista(models.Model):
    id = models.AutoField(primary_key=True)
    noDocumento = models.CharField(max_length=25, verbose_name='No Documento')
    tipoDocumento = models.CharField(max_length=25, verbose_name='Tipo Documento')
    nombreArtista = models.CharField(max_length=50, verbose_name='Nombre')
    apellidosArtista = models.CharField(max_length=50, verbose_name='Apellido')
    fNacimiento = models.DateField(null=True)
    emailArtista = models.CharField(max_length=100)
    fotoArtista = models.ImageField(upload_to='imagenes/',null=True,blank=True)
    iddisquerafk = models.ForeignKey(Disquera, on_delete=models.CASCADE)
    estadoArtista = models.BooleanField()
    acciones=models.CharField(max_length=100)
    def __str__(self):
        row="Artista: =" +self.nombreArtista
        return row

class Genero(models.Model):
    id = models.AutoField(primary_key=True)
    nombreGenero = models.CharField(max_length=100)
    estadoGenero = models.BooleanField()
    acciones=models.CharField(max_length=100)
    
class Album(models.Model):
    id = models.AutoField(primary_key=True)
    nombreAlbum = models.CharField(max_length=100)
    anioPublicacion = models.CharField(max_length=10)
    idArtistaFK = models.ForeignKey(Artista, on_delete=models.CASCADE)
    idGeneroFK = models.ForeignKey(Genero, on_delete=models.CASCADE)
    fotoAlbum = models.ImageField(upload_to='imagenes/',null=True,blank=True) 
    estadoAlbum = models.BooleanField()
    acciones=models.CharField(max_length=100)

class Cancion(models.Model):
    id = models.AutoField(primary_key=True)
    nombreCancion = models.CharField(max_length=100)
    duracionCancion = models.CharField(max_length=10)  
    idAlbumFK = models.ForeignKey(Album, on_delete=models.CASCADE)
    estadoCancion = models.BooleanField()
    acciones=models.CharField(max_length=100)