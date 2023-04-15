from rest_framework import authentication
from torneos.models import Disciplinas,Torneos,TorneosJugadores
from .serializers import DisciplinasSerializer,TorneosSerializer,TorneosJugadoresSerializer
from rest_framework import viewsets

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