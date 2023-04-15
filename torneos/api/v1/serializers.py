from rest_framework import serializers
from torneos.models import Disciplinas,Formatos,Jugadores,Torneos,TorneosJugadores

class JugadoresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jugadores
        fields = "__all__"

class DisciplinasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Disciplinas
        fields = "__all__"

class TorneosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Torneos
        fields = "__all__"

class TorneosJugadoresSerializer(serializers.ModelSerializer):

    class Meta:
        model = TorneosJugadores
        fields = "__all__"

class FormatosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Formatos
        fields = "__all__"