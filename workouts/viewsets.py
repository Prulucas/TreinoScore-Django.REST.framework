from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from .models import Treino, TreinoExercicio, Exercicio
from .serializers import TreinoSerializer, ExercicioSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from users.permissions import IsTeacherOrAdminOrReadOnly


class TreinoViewSet(viewsets.ModelViewSet):
    serializer_class = TreinoSerializer
    permission_classes = [IsTeacherOrAdminOrReadOnly]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return Treino.objects.all().order_by('-created')

        if hasattr(user, 'role') and user.role == 'teacher':
            return Treino.objects.filter(teacher=user).order_by('-created')

        return Treino.objects.filter(student=user).order_by('day')

    # Para vincular automaticamente professor ao criar via POST
    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

    @action(detail=True, methods=['get'], url_path='gerar_pdf')
    def gerar_pdf(self, request, pk=None):
        treino = self.get_object()
        exercicios = TreinoExercicio.objects.filter(
            treino=treino).order_by('order')

        template_path = 'workouts/pdf_treino.html'
        context = {'treino': treino, 'exercicios': exercicios}

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="Treino_{treino.title}.pdf"'

        template = get_template(template_path)
        html = template.render(context)

        pisa_status = pisa.CreatePDF(html, dest=response)

        if pisa_status.err:
            return Response({'error': 'Erro ao gerar PDF'}, status=status.HTTP_400_BAD_REQUEST)

        return response


class ExercicioViewSet(viewsets.ModelViewSet):
    queryset = Exercicio.objects.all().order_by('title')
    serializer_class = ExercicioSerializer
    permission_classes = [IsTeacherOrAdminOrReadOnly]


class CustomTokenLoginView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key,
                             'user_id': user.pk,
                             'role': getattr(user, 'role', 'student')
                             }, status=status.HTTP_200_OK)

        return Response(
            {"detail": "Usuário ou senha incorretos."},
            status=status.HTTP_400_BAD_REQUEST
        )
