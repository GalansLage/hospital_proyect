from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cita(models.Model):
    idCita = models.AutoField(primary_key=True)
    Medico_idMedico = models.PositiveIntegerField()
    Paciente_idPaciente = models.PositiveIntegerField()
    Fecha = models.DateField(null=True)
    Hora = models.TimeField(null=True)
    Descripcion = models.TextField(null=True)
    
    def __str__(self):
        return self.idCita

class Medico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idMedico = models.AutoField(primary_key=True)
    Nombre = models.TextField(null=True)
    Apellido = models.TextField(null=True)
    Especialidad = models.TextField(null=True)
    Email = models.EmailField(null=True)
    
    def __str__(self):
        return self.Nombre

class Paciente(models.Model):
    TYPE_GENERS= (
        (0, 'Otros'),
        (1, 'M'),
        (2, 'H'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idPaciente = models.AutoField(primary_key=True)
    nombre = models.CharField( max_length=255, null=True)
    apellido = models.CharField(null=True, blank=True, max_length=255)
    fecha_Nacimiento = models.DateField(null=True, blank=True)
    genero = models.IntegerField(choices=TYPE_GENERS, default=0)
    email = models.EmailField(null=True)


    def __str__(self):
        return self.nombre


class PruebaMedica(models.Model):
    idPrueba_Medica = models.AutoField(primary_key=True)
    Medico_idMedico = models.PositiveIntegerField()
    Paciente_idPaciente = models.PositiveIntegerField()
    Tipo = models.TextField()
    Fecha = models.DateField(null=True)
    Resultado = models.TextField()

    def __str__(self):
        return self.Tipo

class Tratamiento(models.Model):
    idTratamiento = models.AutoField(primary_key=True)
    Medico_idMedico = models.PositiveIntegerField()
    Paciente_idPaciente = models.PositiveIntegerField()
    Descripcion = models.TextField()
    Fecha_Inicio = models.DateField(null=True)
    Duracion = models.TextField()

    def __str__(self):
        return self.idTratamiento
