from django.contrib import admin
from .models import Periodo, Carrera, Profesor, Asignatura, Estudiante

# Register your models here.
admin.site.register(Periodo)
admin.site.register(Carrera)
admin.site.register(Profesor)
admin.site.register(Asignatura)
admin.site.register(Estudiante)