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
    iddisquerafk=models.ForeignKey(Disquera,on_delete=models.CASCADE)