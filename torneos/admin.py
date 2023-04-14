from django.contrib import admin
from .models import Clubes,Disciplinas,Formatos,Jugadores,JugadoresDisciplinas,Torneos,TorneosJugadores
admin.site.register(Jugadores)
admin.site.register(Disciplinas)
admin.site.register(Clubes)
admin.site.register(JugadoresDisciplinas)
admin.site.register(Torneos)
admin.site.register(TorneosJugadores)
admin.site.register(Formatos)

# Register your models here.
