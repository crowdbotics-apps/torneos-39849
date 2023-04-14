
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ClubesViewSet,DisciplinasViewSet,JugadoresViewSet,JugadoresDisciplinasViewSet
router = DefaultRouter()
router.register('jugadores', JugadoresViewSet )
router.register('disciplinas', DisciplinasViewSet )
router.register('clubes', ClubesViewSet )
router.register('jugadoresdisciplinas', JugadoresDisciplinasViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
