from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

#RENDERIZADO
def inicio(request):
    return render(request, 'app_biblioteca/inicio.html')

def encargados(request):
    return render(request, 'app_biblioteca/encargados.html')

def socios(request):
    return render(request, 'app_biblioteca/socios.html')

def libros(request):
    return render(request, 'app_biblioteca/libros.html')

#INGRESO
def ingreso_encargados(request):
    if (request.method == 'POST'):
        form = Encargado_Form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info['nombre']
            apellido = info['apellido']
            codigo = info['codigo']
            email = info['email']
            encargado = Encargado(nombre=nombre, apellido=apellido,codigo=codigo,email=email)
            encargado.save()
            return render(request, 'app_biblioteca/inicio.html')
    else:
        form = Encargado_Form()
    return render(request,'app_biblioteca/ingreso_encargados.html',{'formulario':form})

def ingreso_socios(request):
    if (request.method == 'POST'):
        form = Socio_Form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info['nombre']
            apellido = info['apellido']
            num_socio = info['num_socio']
            email = info['email']
            fecha_alta = info['fecha_alta']
            socio = Socio(nombre=nombre, apellido=apellido, num_socio=num_socio, email=email, fecha_alta=fecha_alta)
            socio.save()
            return render(request,'app_biblioteca/inicio.html')
    else:
        form = Socio_Form()
    return render(request,'app_biblioteca/ingreso_socios.html', {'formulario':form})

def ingreso_libros(request):
    if (request.method == 'POST'):
        form = Libro_Form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            titulo = info['titulo']
            autor = info['autor']
            genero = info['genero']
            codigo = info['codigo']
            libro = Libro(titulo=titulo, autor=autor, genero=genero, codigo=codigo)
            libro.save()
            return render(request,'app_biblioteca/inicio.html')
    else:
        form = Libro_Form()
    return render(request,'app_biblioteca/ingreso_libros.html', {'formulario':form})

#BUSQUEDA
def busqueda_libro(request):
    return render(request, 'app_biblioteca/resultado_libro.html')

def buscar_libro(request):
    if request.GET['codigo']:
        cod= request.GET['codigo']
        codigo = Libro.objects.filter(codigo=cod) 
        return render(request,'app_biblioteca/buscar_libro.html', {'codigo':codigo})
    else:
        return render(request,'app_biblioteca/resultado_libro.html', {'error':'No se ingreso ningun libro'})

def busqueda_socio(request):
    return render(request, 'app_biblioteca/resultado_socio.html')

def buscar_socio(request):
    if request.GET['num_socio']:
        num_soc= request.GET['num_socio']
        num_socio = Socio.objects.filter(num_socio=num_soc) 
        return render(request,'app_biblioteca/buscar_socio.html', {'num_socio':num_socio})
    else:
        return render(request,'app_biblioteca/resultado_socio.html', {'error':'No se ingreso ningun socio'})

def busqueda_encargado(request):
    return render(request, 'app_biblioteca/resultado_encargado.html')

def buscar_encargado(request):
    if request.GET['codigo']:
        cod= request.GET['codigo']
        codigo = Encargado.objects.filter(codigo=cod) 
        return render(request,'app_biblioteca/buscar_encargado.html', {'codigo':codigo})
    else:
        return render(request,'app_biblioteca/resultado_encargado.html', {'error':'No se ingreso ningun socio'})

#LECTURA
def leer_encargados(request):
    encargados = Encargado.objects.all()
    return render(request, 'app_biblioteca/leer_encargados.html',{'encargados':encargados})

def leer_libros(request):
    libros = Libro.objects.all()
    return render(request, 'app_biblioteca/leer_libros.html',{'libros':libros})

def leer_socios(request):
    socios = Socio.objects.all()
    return render(request, 'app_biblioteca/leer_socios.html',{'socios':socios})

#DELETE
def eliminar_encargado(request, codigo_encargado):
    encargado = Encargado.objects.get(codigo=codigo_encargado) #trae por cod.
    encargado.delete()
    encargados = Encargado.objects.all()
    return render(request, 'app_biblioteca/leer_encargados.html',{'encargados':encargados})

def eliminar_libro(request, codigo_libro):
    libro = Libro.objects.get(codigo=codigo_libro)
    libro.delete()
    libros = Libro.objects.all()
    return render(request, 'app_biblioteca/leer_libros.html',{'libros':libros})

def eliminar_socio(request, num_soc):
    socio = Socio.objects.get(num_socio=num_soc)
    socio.delete()
    socios = Socio.objects.all()
    return render(request, 'app_biblioteca/leer_socios.html',{'socios':socios})

def editar_encargado(request, codigo_encargado):
    encargado = Encargado.objects.get(codigo=codigo_encargado)
    if request.method == 'POST':
        form = Encargado_Form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            encargado.nombre= info['nombre']
            encargado.apellido= info['apellido']
            encargado.codigo= info['codigo']
            encargado.email= info['email']
            encargado.save()
            return render(request, 'app_biblioteca/inicio.html')
    else:
        form = Encargado_Form(initial={'nombre':encargado.nombre, 'apellido':encargado.apellido, 'codigo':encargado.codigo, 'email':encargado.email})
    return render(request, 'app_biblioteca/editar_encargado.html',{'formulario':form,'codigo_encargado':codigo_encargado})

def editar_socio(request, num_soc):
    socio = Socio.objects.get(num_socio=num_soc)
    if request.method == 'POST':
        form = Socio_Form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            socio.nombre = info['nombre']
            socio.apellido = info['apellido']
            socio.num_socio= info['num_socio']
            socio.email= info['email']
            socio.fecha_alta= info['fecha_alta']
            socio.save()
            return render (request, 'app_biblioteca/inicio.html')
    else:
        form = Socio_Form(initial={'nombre':socio.nombre, 'apellido':socio.apellido, 'num_socio':socio.num_socio, 'email':socio.email, 'fecha_alta':socio.fecha_alta})
    return render(request, 'app_biblioteca/editar_socio.html',{'formulario':form,'num_soc':num_soc})

def editar_libro(request, codigo_libro):
    libro = Libro.objects.get(codigo=codigo_libro)
    if request.method == 'POST':
        form = Libro_Form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            libro.titulo = info['titulo']
            libro.autor = info['autor']
            libro.genero = info['genero']
            libro.codigo = info['codigo']
            libro.save()
            return render (request, 'app_biblioteca/inicio.html')
    else:
        form = Libro_Form(initial={'titulo':libro.titulo, 'autor':libro.autor, 'genero':libro.genero, 'codigo':libro.codigo})
    return render(request, 'app_biblioteca/editar_libro.html',{'formulario':form,'codigo_libro':codigo_libro})