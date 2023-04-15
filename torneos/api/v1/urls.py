
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import DisciplinasViewSet,TorneosViewSet,TorneosJugadoresViewSet
router = DefaultRouter()
router.register('disciplinas', DisciplinasViewSet )
router.register('torneos', TorneosViewSet )
router.register('torneosjugadores', TorneosJugadoresViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
