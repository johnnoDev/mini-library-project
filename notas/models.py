from django.db import models

# Create your models here.

# Modelos de Configuración (Solo Django Admin)
class Periodo(models.Model):
    descripcion = models.CharField(max_length=100)

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)

class Profesor(models.Model):
    nombres = models.CharField(max_length=100)

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)

class Estudiante(models.Model):
    cedula = models.CharField(max_length=10)
    nombres = models.CharField(max_length=150)

# -----------------------------------------------------------------
# Modelo Matrícula (Maestro)
class Matricula(models.Model):
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    total_estudiantes = models.PositiveIntegerField(default=0)

# Modelo MatrículaDetalle
class MatriculaDetalle(models.Model):
    matricula = models.ForeignKey(
        Matricula,
        related_name="detalles",
        on_delete=models.CASCADE
    )

    estudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura,on_delete=models.CASCADE)

# Modelo Notas (Maestro)
class Notas(models.Model):
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor,on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura,on_delete=models.CASCADE)

    total_estudiantes=models.PositiveIntegerField(default=0)

# Modelo NotaDetalle
class NotaDetalle(models.Model):

    notas=models.ForeignKey(
        Notas,
        related_name="detalles",
        on_delete=models.CASCADE
    )

    estudiante=models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE
    )

    nota1=models.DecimalField(max_digits=5,decimal_places=2)
    nota2=models.DecimalField(max_digits=5,decimal_places=2)

    nota_final=models.DecimalField(
        max_digits=5,
        decimal_places=2,
        editable=False
    )

    observacion=models.CharField(
        max_length=20,
        editable=False
    )
