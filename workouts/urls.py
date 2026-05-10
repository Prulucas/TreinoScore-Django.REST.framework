from django.urls import path
from . import views

app_name = 'workouts'

urlpatterns = [
    # path('workouts', listar_treinos, name='workout'),
    path('', views.listar_treinos, name='workout_index'),
    path('create_workout/', views.treino_create, name='treino_form'),
    path('treino/<int:pk>/detalhes/',
         views.treino_detalhes, name='treino_detalhes'),
    path('treino/exercicio/remover/<int:pk>/',
         views.remover_exercicio_do_treino, name='remover_exercicio'),
    path('treino/<int:pk>/', views.treino_view, name='treino_view'),
    path('treino/gerar_pdf_treino/<int:pk>',
         views.gerar_pdf_treino, name='gerar_pdf_treino'),
    path('treino/deletar/<int:pk>/', views.treino_delete, name='treino_delete'),
    path('create_exercise/', views.exercicio_create, name='exercicio_form'),
    path('exercicio/deletar/<int:pk>/',
         views.exercicio_delete, name='exercicio_delete'),
]
