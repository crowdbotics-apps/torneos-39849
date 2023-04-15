
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import DisciplinasViewSet,TorneosViewSet
router = DefaultRouter()
router.register('disciplinas', DisciplinasViewSet )
router.register('torneos', TorneosViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
