from rest_framework import serializers
from torneos.models import Disciplinas,Torneos

class DisciplinasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Disciplinas
        fields = "__all__"

class TorneosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Torneos
        fields = "__all__"