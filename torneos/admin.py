from django.contrib import admin
from .models import Disciplinas,Formatos,Jugadores,Torneos,TorneosJugadores
admin.site.register(Jugadores)
admin.site.register(Disciplinas)
admin.site.register(Torneos)
admin.site.register(TorneosJugadores)
admin.site.register(Formatos)

# Register your models here.
