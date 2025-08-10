from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Cursos



def principal(request):
    cursos = Cursos.objects.all()
    return render(request, "inicio/principal.html", {'cursos': cursos})

def cursos (request):
    cursos=Cursos.objects.all() #all recupera todos los objetos del modelo(registros de la tabla alumnos)
    return render(request, "cursos/cursos.html",{'cursos':cursos})


def contacto(request):
    return render(request, "inicio/contacto.html") 


def editar_curso(request, id):
    curso=get_object_or_404(Cursos, pk=id)
    if request.method =='POST':
        curso.titulo = request.POST['titulo']
        curso.categoria = request.POST['categoria']
        curso.descripcion = request.POST['descripcion']
        curso.profesor = request.POST['profesor']
        if 'imagen' in request.FILES:
            curso.imagen = request.FILES['imagen']
        curso.save()
        return redirect('Cursos')
    return render(request, 'cursos/editarCurso.html', {'curso':curso})



def eliminar_curso (request, id):
    curso=get_object_or_404(Cursos, pk=id)
    if request.method =='POST':
        curso.delete()
        return redirect('Cursos')
    return render (request, 'cursos/confirmarEliminacion.html', {'curso': curso})


def crear_curso(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        categoria = request.POST.get('categoria')
        descripcion = request.POST.get('descripcion')
        profesor = request.POST.get('profesor')
        imagen = request.FILES.get('imagen')

        nuevo_curso = Cursos(
            titulo=titulo,
            categoria=categoria,
            descripcion=descripcion,
            profesor=profesor,
            imagen=imagen
        )
        nuevo_curso.save()
        return redirect('Cursos')

    return render(request, 'cursos/crearCurso.html')

