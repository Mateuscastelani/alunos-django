from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    # Devolve a página HTML visual
    path('alunos/', views.ListaAlunosUnivesp.as_view(), name='lista_alunos'),
    
    # rota da sua API Devolve apenas os dados puros em JSON
    path('api/alunos/', views.ListaAlunosAPI.as_view(), name='api_alunos'),
]