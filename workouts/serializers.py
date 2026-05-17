from rest_framework import serializers
from .models import Treino, TreinoExercicio, Exercicio

# 1. Serializer do Exercício Base (ex: Supino Reto)


class ExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicio
        fields = ['id', 'title', 'description', 'category', 'difficulty']

# 2. Serializer da tabela intermediária (Une o exercício às séries/repetições do treino)


class TreinoExercicioSerializer(serializers.ModelSerializer):
    exercicio = ExercicioSerializer(read_only=True)

    class Meta:
        model = TreinoExercicio
        fields = ['id', 'exercicio', 'order',
                  'series', 'repetitions', 'weight', 'rest_seconds']

# 3. Serializer Principal do Treino


class TreinoSerializer(serializers.ModelSerializer):
    exercicios = TreinoExercicioSerializer(
        many=True, read_only=True, source='treinoexercicio_set')

    class Meta:
        model = Treino
        fields = ['id', 'title', 'student',
                  'teacher', 'day', 'created', 'exercicios']
