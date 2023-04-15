from rest_framework import serializers
from torneos.models import Disciplinas,Torneos,TorneosJugadores

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