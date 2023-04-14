from django.contrib import admin
from .models import Clubes,Disciplinas,Jugadores,JugadoresDisciplinas
admin.site.register(Jugadores)
admin.site.register(Disciplinas)
admin.site.register(Clubes)
admin.site.register(JugadoresDisciplinas)

# Register your models here.
