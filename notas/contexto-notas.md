EXAMEN PRÁCTICO DE POO CON DJANGO
Modelo propuesto
Modelos de Configuración (Solo Django Admin)
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
________________________________________
Modelo Matrícula (Maestro)
class Matricula(models.Model):
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    total_estudiantes = models.PositiveIntegerField(default=0)
________________________________________
Modelo MatrículaDetalle
class MatriculaDetalle(models.Model):
    matricula = models.ForeignKey(
        Matricula,
        related_name="detalles",
        on_delete=models.CASCADE
    )

    estudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura,on_delete=models.CASCADE)
________________________________________
Modelo Notas (Maestro)
class Notas(models.Model):
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor,on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura,on_delete=models.CASCADE)

    total_estudiantes=models.PositiveIntegerField(default=0)
________________________________________
Modelo NotaDetalle
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
Así se evita repetir profesor, período, carrera y asignatura por cada estudiante.
________________________________________
Indicaciones Generales
Desarrolle el caso de estudio asignado (Fila 1 o Fila 2) dentro del proyecto Django existente tal como se ha realizado los cruds del proyecto
El desarrollo deberá cumplir obligatoriamente con las siguientes condiciones:
•	Crear una nueva aplicación dentro del proyecto existente. 
•	Reutilizar toda la arquitectura del proyecto. 
•	Reutilizar Bootstrap, layouts, JavaScript, CSS, autenticación, plantillas, componentes y librerías existentes. 
•	Implementar correctamente el patrón Maestro–Detalle. 
•	Utilizar Class Based Views (CBV) para el CRUD. 
•	Aplicar Programación Orientada a Objetos. 
•	Implementar validaciones. 
•	Realizar todos los cálculos mediante lógica propia. 
•	No utilizar Inteligencia Artificial ni asistentes de código durante el examen. 
•	Todos los modelos deberán ser creados por ambos grupos. 
•	Los modelos de configuración deberán administrarse únicamente desde Django Admin. 
•	Solamente el módulo asignado a su fila deberá contar con CRUD transaccional. 
________________________________________
MODELOS QUE DEBEN CREAR TODOS LOS ESTUDIANTES
Todos los grupos deberán crear los siguientes modelos:
•	Periodo 
•	Carrera 
•	Profesor 
•	Asignatura 
•	Estudiante 
•	Matricula 
•	MatriculaDetalle 
•	Notas 
•	NotaDetalle 
Los modelos:
•	Periodo 
•	Carrera 
•	Profesor 
•	Asignatura 
•	Estudiante 
serán registrados únicamente mediante Django Admin.
No requieren CRUD.
________________________________________



PREGUNTA 1 — FILA 1
Sistema de Matriculación Académica
Descripción
La institución educativa necesita incorporar un nuevo módulo para registrar las matrículas de los estudiantes.
Cada matrícula corresponde a un período académico y podrá contener varios estudiantes matriculados en distintas carreras y asignaturas.
El estudiante deberá desarrollar únicamente el CRUD del proceso de matrícula utilizando el patrón Maestro–Detalle.
________________________________________
Modelo Maestro
Matricula

Periodo
Fecha
Total Estudiantes
________________________________________
Modelo Detalle
MatriculaDetalle

Matricula
Estudiante
Carrera
Asignatura
________________________________________
Requerimientos Funcionales
El sistema deberá:
•	Registrar una matrícula. 
•	Seleccionar el período académico. 
•	Agregar múltiples estudiantes. 
•	Seleccionar carrera. 
•	Seleccionar asignatura. 
•	Un estudiante podrá aparecer varias veces únicamente si pertenece a otra asignatura. 
•	Calcular automáticamente: 
Total Estudiantes
contando los registros del detalle.
Cuando se agregue o elimine un detalle, el total deberá actualizarse automáticamente.
________________________________________
Pantalla esperada
--------------------------------------------------------
            REGISTRO DE MATRÍCULA
--------------------------------------------------------

Periodo : [ 2026-I                     ]

Fecha   : [17/07/2026]

Total Estudiantes : [ 25 ]

--------------------------------------------------------
DETALLE
--------------------------------------------------------

+------------------------------------------------------+
| Estudiante | Carrera | Asignatura |      Acción      |
+------------------------------------------------------+
| Juan       | Sistemas| POO         | Edit Eliminar    |
| Pedro      | Sistemas| BD          | Edit Eliminar    |
| Ana        | Software| IA          | Edit Eliminar    |
+------------------------------------------------------+

        [Agregar Detalle]

--------------------------------------------------------

Guardar
Cancelar
________________________________________
