from django import forms
from .models import Matricula, MatriculaDetalle

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['periodo']

class MatriculaDetalleForm(forms.ModelForm):
    class Meta:
        model = MatriculaDetalle
        fields = ['estudiante', 'carrera', 'asignatura']

