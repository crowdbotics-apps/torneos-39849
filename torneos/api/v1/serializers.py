from rest_framework import serializers
from torneos.models import Clubes,Disciplinas,Jugadores,JugadoresDisciplinas

class JugadoresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jugadores
        fields = "__all__"

class DisciplinasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Disciplinas
        fields = "__all__"

class ClubesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clubes
        fields = "__all__"

class JugadoresDisciplinasSerializer(serializers.ModelSerializer):

    class Meta:
        model = JugadoresDisciplinas
        fields = "__all__"