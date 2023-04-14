from django.contrib import admin
from .models import Clubes,Disciplinas,Jugadores,JugadoresDisciplinas,Torneos,TorneosJugadores
admin.site.register(Jugadores)
admin.site.register(Disciplinas)
admin.site.register(Clubes)
admin.site.register(JugadoresDisciplinas)
admin.site.register(Torneos)
admin.site.register(TorneosJugadores)

# Register your models here.
