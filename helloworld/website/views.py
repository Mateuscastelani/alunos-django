from django.views.generic import ListView
from .models import AlunoUnivesp # Importando o seu modelo
from django.http import HttpResponse

class ListaAlunosUnivesp(ListView):
    template_name = "alunosUnivesp.html"
    model = AlunoUnivesp
    context_object_name = "alunos"


def index(request):
    return HttpResponse("Bem-vindo à página inicial do Website!")