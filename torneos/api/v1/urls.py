
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ClubesViewSet,DisciplinasViewSet,JugadoresViewSet,JugadoresDisciplinasViewSet,TorneosViewSet,TorneosJugadoresViewSet
router = DefaultRouter()
router.register('jugadores', JugadoresViewSet )
router.register('disciplinas', DisciplinasViewSet )
router.register('clubes', ClubesViewSet )
router.register('jugadoresdisciplinas', JugadoresDisciplinasViewSet )
router.register('torneos', TorneosViewSet )
router.register('torneosjugadores', TorneosJugadoresViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
