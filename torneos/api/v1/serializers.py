from rest_framework import serializers
from torneos.models import Disciplinas

class DisciplinasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Disciplinas
        fields = "__all__"