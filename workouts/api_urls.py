from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TreinoViewSet, ExercicioViewSet

router = DefaultRouter()
router.register(r'treinos', TreinoViewSet, basename='treino')
router.register(r'exercicios', ExercicioViewSet, basename='exercicio')

urlpatterns = [
    path('', include(router.urls)),
]
