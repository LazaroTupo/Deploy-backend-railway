from django.db import models

# Create your models here.
class Terapista(models.Model):
    dni = models.CharField(primary_key=True, unique=True,max_length=8)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    fecha_de_nacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9, null = True, blank = True)
    genero = models.CharField(max_length=1)
    estado_civil = models.CharField(max_length=1)
    salario = models.FloatField()
    activo = models.BooleanField()

    def __str__(self):
        return self.apellido+", "+self.nombre

class Paciente(models.Model):
    dni = models.CharField(primary_key=True, unique=True, max_length=8)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    fecha_de_nacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9, null = True, blank = True)
    genero = models.CharField(max_length=1)
    estado_civil = models.CharField(max_length=1)
    ocupacion = models.CharField(max_length=50)

    def __str__(self):
        return self.apellido+", "+self.nombre

class Cita(models.Model):    
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    terapista = models.ForeignKey(Terapista, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=True, null=True)  
    evaluacion = models.ForeignKey('historial_medico.Evaluacion', on_delete=models.CASCADE, null=True, blank=True)
    reporte = models.CharField(max_length=500, blank=True, null=True)
    precio = models.FloatField()  
    asistido = models.BooleanField()