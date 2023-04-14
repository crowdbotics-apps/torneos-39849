from rest_framework import authentication
from torneos.models import Clubes,Disciplinas,Jugadores,JugadoresDisciplinas
from .serializers import ClubesSerializer,DisciplinasSerializer,JugadoresSerializer,JugadoresDisciplinasSerializer
from rest_framework import viewsets

class JugadoresViewSet(viewsets.ModelViewSet):
    serializer_class = JugadoresSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Jugadores.objects.all()

class DisciplinasViewSet(viewsets.ModelViewSet):
    serializer_class = DisciplinasSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Disciplinas.objects.all()

class ClubesViewSet(viewsets.ModelViewSet):
    serializer_class = ClubesSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Clubes.objects.all()

class JugadoresDisciplinasViewSet(viewsets.ModelViewSet):
    serializer_class = JugadoresDisciplinasSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = JugadoresDisciplinas.objects.all()