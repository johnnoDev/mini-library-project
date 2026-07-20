from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from .models import *
from .forms import *

# Create your views here.
class MatriculaDetalleCreateView(CreateView):
    model = MatriculaDetalle
    form_class = MatriculaDetalleForm
    template_name = 'notas/detalle_form.html'
    
    def form_valid(self, form):
        matricula = get_object_or_404(Matricula, pk=self.kwargs['matricula_pk'])
        """ 
        form.instance es el objeto MatriculaDetalle que el formulario está construyendo a partir de lo que el usuario llenó (estudiante, carrera, asignatura), pero todavía no guardado en la base de datos.
        """
        form.instance.matricula = matricula

        ya_existe = MatriculaDetalle.objects.filter(
            matricula=matricula,
            estudiante=form.instance.estudiante,
            asignatura=form.instance.asignatura,
        ).exists()

        if ya_existe:
            form.add_error(None, 'Este estudiante ya está matriculado en esa asignatura.')
            return self.form_invalid(form)

        return super().form_valid(form)