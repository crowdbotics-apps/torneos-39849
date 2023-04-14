from django.conf import settings
from django.db import models
class Jugadores(models.Model):
    'Generated Model'
    nombre = models.CharField(max_length=256,)
    email = models.EmailField(max_length=254,)
    edad = models.SmallIntegerField()
    club = models.ForeignKey("torneos.Clubes",null=True,blank=True,on_delete=models.CASCADE,related_name="jugadores_club",)
    disciplinas = models.ManyToManyField("torneos.Disciplinas",blank=True,related_name="jugadores_disciplinas",)
class Disciplinas(models.Model):
    'Generated Model'
    nombre = models.CharField(max_length=256,)
class Clubes(models.Model):
    'Generated Model'
    nombre = models.CharField(max_length=256,)
    logo = models.BinaryField()
    color1 = models.SmallIntegerField()
    color2 = models.SmallIntegerField()
    color3 = models.SmallIntegerField()
    disciplinas = models.ManyToManyField("torneos.Disciplinas",blank=True,related_name="clubes_disciplinas",)
class JugadoresDisciplinas(models.Model):
    'Generated Model'
    id_jugador = models.ForeignKey("torneos.Jugadores",on_delete=models.CASCADE,related_name="jugadoresdisciplinas_id_jugador",)
    id_disciplina = models.ForeignKey("torneos.Disciplinas",on_delete=models.CASCADE,related_name="jugadoresdisciplinas_id_disciplina",)
    categoria = models.SmallIntegerField()
    rankeo = models.SmallIntegerField()
    puntaje = models.DecimalField(max_digits=5,decimal_places=2,)
class Torneos(models.Model):
    'Generated Model'
    nombre = models.CharField(max_length=256,)
    modalidad = models.BooleanField()
    clubes = models.ManyToManyField("torneos.Clubes",blank=True,related_name="torneos_clubes",)
    disciplina = models.ForeignKey("torneos.Disciplinas",on_delete=models.CASCADE,null=True,blank=True,related_name="torneos_disciplina",)
class TorneosJugadores(models.Model):
    'Generated Model'
    torneo = models.ForeignKey("torneos.Torneos",on_delete=models.CASCADE,related_name="torneosjugadores_torneo",)
    jugador = models.ForeignKey("torneos.Jugadores",on_delete=models.CASCADE,related_name="torneosjugadores_jugador",)

# Create your models here.
