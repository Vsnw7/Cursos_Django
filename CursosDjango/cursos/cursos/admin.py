from django.contrib import admin
from .models import Cursos

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=('titulo', 'categoria', 'descripcion', 'profesor')
    search_fields=('titulo', 'categoria', 'descripcion', 'profesor')
    date_hierarchy='created'
    list_filter=('categoria', 'profesor')

admin.site.register(Cursos, AdministrarModelo)
