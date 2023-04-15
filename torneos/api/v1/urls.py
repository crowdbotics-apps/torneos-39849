
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import DisciplinasViewSet
router = DefaultRouter()
router.register('disciplinas', DisciplinasViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
