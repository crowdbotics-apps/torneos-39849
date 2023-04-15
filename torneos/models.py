from django.conf import settings
from django.db import models
class Jugadores(models.Model):
    'Generated Model'
    nombre = models.CharField(max_length=256,)
    email = models.EmailField(max_length=254,)
    edad = models.SmallIntegerField()
    disciplinas = models.ManyToManyField("torneos.Disciplinas",blank=True,related_name="jugadores_disciplinas",)
class Disciplinas(models.Model):
    'Generated Model'
    nombre = models.CharField(max_length=256,)
class Torneos(models.Model):
    'Generated Model'
    nombre = models.CharField(max_length=256,)
    modalidad = models.BooleanField()
    disciplina = models.ForeignKey("torneos.Disciplinas",null=True,blank=True,on_delete=models.CASCADE,related_name="torneos_disciplina",)
    formato = models.ForeignKey("torneos.Formatos",null=True,blank=True,on_delete=models.CASCADE,related_name="torneos_formato",)
    inter = models.BooleanField(null=True,blank=True,)
class TorneosJugadores(models.Model):
    'Generated Model'
    torneo = models.ForeignKey("torneos.Torneos",on_delete=models.CASCADE,related_name="torneosjugadores_torneo",)
    jugador = models.ForeignKey("torneos.Jugadores",on_delete=models.CASCADE,related_name="torneosjugadores_jugador",)
    horario_jugador = models.CharField(null=True,blank=True,max_length=256,)
class Formatos(models.Model):
    'Generated Model'
    nombre = models.CharField(max_length=256,)
    estructura = models.CharField(max_length=256,)

# Create your models here.
