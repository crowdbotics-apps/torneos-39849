from rest_framework import authentication
from torneos.models import Clubes,Disciplinas,Jugadores,JugadoresDisciplinas,Torneos,TorneosJugadores
from .serializers import ClubesSerializer,DisciplinasSerializer,JugadoresSerializer,JugadoresDisciplinasSerializer,TorneosSerializer,TorneosJugadoresSerializer
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

class TorneosViewSet(viewsets.ModelViewSet):
    serializer_class = TorneosSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Torneos.objects.all()

class TorneosJugadoresViewSet(viewsets.ModelViewSet):
    serializer_class = TorneosJugadoresSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = TorneosJugadores.objects.all()