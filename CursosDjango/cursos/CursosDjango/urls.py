from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from contenido import views
from cursos import views as views_cursos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_cursos.principal, name="Principal"),
    path('contacto/', views_cursos.contacto, name="Contacto"),
    path('cursos/', views_cursos.cursos, name="Cursos"),
    path('cursos/crearCursos/', views_cursos.crear_curso, name="crear_curso"),
    path('cursos/editar/<int:id>/', views_cursos.editar_curso, name='editar_curso'),
    path('cursos/eliminar/<int:id>/', views_cursos.eliminar_curso, name='eliminar_curso'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / "contenido" / "static")
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
