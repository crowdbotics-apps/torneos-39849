from django.contrib import admin
from .models import Disciplinas,Jugadores,Torneos,TorneosJugadores
admin.site.register(Jugadores)
admin.site.register(Disciplinas)
admin.site.register(Torneos)
admin.site.register(TorneosJugadores)

# Register your models here.
