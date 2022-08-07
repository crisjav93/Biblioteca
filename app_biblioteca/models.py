from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Encargado(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    codigo=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.nombre+' '+self.apellido+' '+str(self.codigo)+' '+self.email

class Socio(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    num_socio=models.IntegerField()
    email=models.EmailField()
    fecha_alta=models.DateField()

    def __str__(self):
        return self.nombre+' '+self.apellido+' '+str(self.num_socio)+' '+self.email+' '+str(self.fecha_alta)

class Libro(models.Model):
    titulo=models.CharField(max_length=50)
    autor=models.CharField(max_length=50)
    genero=models.CharField(max_length=50)
    codigo=models.IntegerField()

    def __str__(self):
        return self.titulo+' '+self.autor+' '+self.genero+' '+str(self.codigo)

class avatar(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank= True)