from django.db import models

# Create your models here.

class Cursos(models.Model):
    ID = models.AutoField(primary_key=True, verbose_name="Id de Curso")
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
