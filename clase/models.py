import email
from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()


class Profesor(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)


class Entregable(models.Model):
    nombre= models.CharField(max_length=20)
    FechaDeEntrega= models.DateTimeField()
    entregado= models.BooleanField() #asi le decis si es true o false


class Curso(models.Model):
    nombre= models.CharField(max_length=20)
    camada= models.IntegerField() #el integerfield indica que son numericos
 
 #ENTRE CLASES DEBE HABER DOS ESPACIOS DE SPEARACIÓN Y CUANDO HACES U IMPORT TAMBIEN TIENENQ UE HABER DOS EPSACIOS ENTRE EL IMPORT Y LAS CLASES