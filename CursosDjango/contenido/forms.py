from django import forms
from .models import Cursos

class CursoForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ['titulo', 'categoria', 'descripcion', 'profesor', 'imagen']

