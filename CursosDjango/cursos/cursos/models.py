from django.db import models
from ckeditor.fields import RichTextField
 
# Create your models here.

class Cursos(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Id de Curso")
    titulo = models.TextField(verbose_name="Título del Curso")
    categoria = models.CharField(max_length=20, verbose_name="Categoría del Curso")
    descripcion = models.TextField(verbose_name="Descripción del Curso")
    profesor = models.TextField(verbose_name="Profesor que lo imparte")
    imagen = models.ImageField(null = True, upload_to="foto", verbose_name="Fotografía")
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de actualización")

    class Meta:  
        verbose_name="Curso"
        verbose_name_plural="Cursos"
        ordering=["created"]   

    def __str__(self):
        return self.titulo
    

class Actividad(models.Model):
    id=models.AutoField(primary_key=True, verbose_name="Clave de la Actividad")
    curso=models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name="Curso")
    descripcionActividad=RichTextField(verbose_name="Descripción de la Actividad")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Creado")

    class Meta:  #cambia el titulo del modelo y da un ordenamiento a los registros
        verbose_name="Actividad"
        verbose_name_plural="Actividades"
        ordering=["-created"]

    def __str__(self):
        return self.curso
