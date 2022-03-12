from django.shortcuts import render

# Create your views here.

# creo dentro de miproyecto un file que se llame views.py

from django.http import HttpResponse
import random

from django.template import loader

# creo una vista/view mediante una fucnión y le paso como parametro request

def inicio(request):
    return HttpResponse('Hola soy la nueva pagina')

def otro_vista(request):
    return HttpResponse('''
    <h1> este es un Titulo en h1 </h1>
    ''')

def numero_random(request):
    numero= random.randrange(15,180)
    texto= f'<h1> Este es tu número random: {numero}</h1>'
    return HttpResponse(texto)

def numero_del_usuario(request, numero):
    texto= f'<h1> Este es tu número: {numero}</h1>'
    return HttpResponse(texto)

def mi_plantilla(request):
    
    nombre= 'Lara'
    apellido= 'Gonzalez'

    diccionario_de_datos = {
        'nombre': nombre,
        'apellido': apellido
} 

#version nueva con loader 
    template = loader.get_template("mi_plantilla.html")
   
    plantilla_preparada= template.render(diccionario_de_datos) #así se genera el tempalte con RENDER
    
    return HttpResponse(plantilla_preparada)


# versión vieja con open
# plantilla = open(r'C:\Users\laruu\OneDrive\Escritorio\miproyecto\miproyecto\plantillas\mi_plantilla.html')
# template= Template(plantilla.read())
#plantilla.close()
# context = Context(diccionario_de_datos) 
#plantilla_preparada =template.render(diccionario_de_datos)

# comentamos esto porque ya no hay un context 
# sino solo el template, en lugar de pasarle
# el context a la plantilla le agregmaos 
# directamente el diccionario de datos 
#aca tengo que agregarle el nombre de la plantilla que ovy a usar 

    #para simplificar todo se usa un LOADER,
    #  un cargador. esto nos va a permitir 
    # no tener que escribir el mismo codigo
    #  muchas veces. se pone arriba del 
    # todo donde se trajo el template se 
    # agrega laoder 

    #para evitar poner todo lo que dice en
    #  open, vamos a settings y
    #  en la parte de TEMPLATES agregamos 
    # lo que estabamos 
    # poniendo en open 
    # "C:\Users\laruu\OneDrive\Escritorio\miproyecto\miproyecto\plantillas\