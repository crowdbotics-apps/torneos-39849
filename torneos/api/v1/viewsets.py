from rest_framework import authentication
from torneos.models import Disciplinas
from .serializers import DisciplinasSerializer
from rest_framework import viewsets

class DisciplinasViewSet(viewsets.ModelViewSet):
    serializer_class = DisciplinasSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Disciplinas.objects.all()