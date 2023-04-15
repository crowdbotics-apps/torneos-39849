
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import DisciplinasViewSet,JugadoresViewSet,TorneosViewSet,TorneosJugadoresViewSet
router = DefaultRouter()
router.register('jugadores', JugadoresViewSet )
router.register('disciplinas', DisciplinasViewSet )
router.register('torneos', TorneosViewSet )
router.register('torneosjugadores', TorneosJugadoresViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
