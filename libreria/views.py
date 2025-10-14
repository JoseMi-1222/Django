from django.shortcuts import render
from django.db.models import Q
from .models import *
# Create your views here.

def index(request):
    return render(request, 'libro/index.html')

def listar_libros(request):
    libros = Libro.objects.select_related('biblioteca').prefetch_related('autores')
    libros = libros.all()
    return render(request, 'libro/lista.html', {'libros_mostrar': libros})

def dame_libro(request, id_libro):
    libro = Libro.objects.select_related('biblioteca').prefetch_related('autores').get(id=id_libro)
    return render(request, 'libro/libro.html', {'libro_mostrar': libro})

def dame_libros_fecha(request, anyo_libro, mes_libro):
    libros = Libro.objects.select_related('biblioteca').prefetch_related('autores')
    libros = libros.filter(fecha_publicacion__year=anyo_libro, fecha_publicacion__month=mes_libro)
    libros = libros.all()
    return render(request, 'libro/lista.html', {'libros_mostrar': libros})

def dame_libros_idioma(request, idioma):
    libros = Libro.objects.select_related('biblioteca').prefetch_related('autores')
    libros = libros.filter(Q(tipo=idioma) | Q(tipo='ES')).order_by('fecha_publicacion')
    libros = libros.all()
    return render(request, 'libro/lista.html', {'libros_mostrar': libros})

def dame_libros_biblioteca(request, id_biblioteca, texto_libro):
    libros = Libro.objects.select_related('biblioteca').prefetch_related('autores')
    libros = libros.filter(biblioteca__id=id_biblioteca, descripcion__contains=texto_libro).order_by('-nombre')
    libros = libros.all()
    return render(request, 'libro/lista.html', {'libros_mostrar': libros})