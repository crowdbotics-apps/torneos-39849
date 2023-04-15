from rest_framework import authentication
from torneos.models import Disciplinas,Formatos,Jugadores,Torneos,TorneosJugadores
from .serializers import DisciplinasSerializer,FormatosSerializer,JugadoresSerializer,TorneosSerializer,TorneosJugadoresSerializer
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

class FormatosViewSet(viewsets.ModelViewSet):
    serializer_class = FormatosSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Formatos.objects.all()