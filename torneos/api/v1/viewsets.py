from rest_framework import authentication
from torneos.models import Disciplinas,Jugadores,Torneos,TorneosJugadores
from .serializers import DisciplinasSerializer,JugadoresSerializer,TorneosSerializer,TorneosJugadoresSerializer
from rest_framework import viewsets

class JugadoresViewSet(viewsets.ModelViewSet):
    serializer_class = JugadoresSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Jugadores.objects.all()

class DisciplinasViewSet(viewsets.ModelViewSet):
    serializer_class = DisciplinasSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Disciplinas.objects.all()

class TorneosViewSet(viewsets.ModelViewSet):
    serializer_class = TorneosSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Torneos.objects.all()

class TorneosJugadoresViewSet(viewsets.ModelViewSet):
    serializer_class = TorneosJugadoresSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = TorneosJugadores.objects.all()