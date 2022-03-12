from django.http import HttpResponse
from django.shortcuts import render
from clase.models import Curso
import random


# Create your views here.

def nuevo_curso(request):
    camada= random.randrange(10, 30)
    nuevo_curso= Curso(nombre= 'Curso Python', camada=camada)
    nuevo_curso.save()
    return HttpResponse(f"Se creo el curso {nuevo_curso.nombre} camada {nuevo_curso.camada}")

def nuevo_curso1(request):
    camada= random.randrange(10, 60)
    nuevo_curso1= Curso(nombre= 'Curso Python1', camada=camada)
    nuevo_curso1.save()
    return HttpResponse(f"Se creo el curso {nuevo_curso1.nombre} camada {nuevo_curso1.camada}")