from django.shortcuts import render
from django.http import HttpResponse 

def principal(request):
    return render(request, "inicio/principal.html") 

def cursos(request):
    cursos_lista = [
        { 'titulo': 'Programación',                'imagen': 'inicio/images/image.png' },
        { 'titulo': 'Base de datos',               'imagen': 'inicio/images/base de datos.webp' },
        { 'titulo': 'Inglés',                      'imagen': 'inicio/images/ingles.webp' },
        { 'titulo': 'Desarrollo Web',              'imagen': 'inicio/images/desarrollo-web.png' },
        { 'titulo': 'Administración de Proyectos', 'imagen': 'inicio/images/adp.jpg' },
    ]
    contexto = {
        'cursos': cursos_lista
    }
    return render(request, "inicio/cursos.html", contexto)

def contacto(request):
    return render(request, "inicio/contacto.html") 

