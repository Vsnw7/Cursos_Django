from django.contrib import admin
from .models import Cursos
from .models import Actividad


class AdministrarModelo(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=('titulo', 'categoria', 'descripcion', 'profesor')
    search_fields=('titulo', 'categoria', 'descripcion', 'profesor')
    date_hierarchy='created'
    list_filter=('categoria', 'profesor')

    class Media:
        css = {
            'all': ('css/custom_admin.css',)  # Ruta dentro de /static
        }

admin.site.register(Cursos, AdministrarModelo)


class AdministrarActividad(admin.ModelAdmin):
    list_display=('id', 'curso', 'descripcionActividad')
    search_fields=('id', 'curso__titulo')
    date_hierarchy='created'
    readonly_fields=('id',)

    class Media:
        css = {
            'all': ('css/custom_admin.css',)  # Ruta dentro de /static
        }

admin.site.register(Actividad, AdministrarActividad)

