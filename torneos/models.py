from django.conf import settings
from django.db import models
class Disciplinas(models.Model):
    'Generated Model'
    nombre = models.CharField(max_length=256,)
class Torneos(models.Model):
    'Generated Model'
    nombre = models.CharField(max_length=256,)
    modalidad = models.BooleanField()
    disciplina = models.ForeignKey("torneos.Disciplinas",null=True,blank=True,on_delete=models.CASCADE,related_name="torneos_disciplina",)
    inter = models.BooleanField(null=True,blank=True,)
class TorneosJugadores(models.Model):
    'Generated Model'
    torneo = models.ForeignKey("torneos.Torneos",on_delete=models.CASCADE,related_name="torneosjugadores_torneo",)
    horario_jugador = models.CharField(null=True,blank=True,max_length=256,)

# Create your models here.
