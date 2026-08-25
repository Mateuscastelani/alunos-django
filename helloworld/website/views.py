from django.views.generic import ListView
from .models import AlunoUnivesp # Importando o seu modelo
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AlunoSerializer

class ListaAlunosUnivesp(ListView):
    template_name = "alunosUnivesp.html"
    model = AlunoUnivesp
    context_object_name = "alunos"


def index(request):
    return HttpResponse("Bem-vindo à página inicial do Website!")

# código da API
class ListaAlunosAPI(APIView):
    def get(self, request):
        # Busca todos os alunos
        alunos = AlunoUnivesp.objetos.all()
        
        # Verifica se alguém passou o parâmetro 'mat' na URL (ex: ?mat=123)
        mat = request.query_params.get('mat', None)
        
        if mat:
            # Se passou a matrícula, filtra para mostrar só aquele aluno
            alunos = AlunoUnivesp.objetos.filter(matricula=mat)
            
        # Passa os dados para o Serializer traduzir para JSON
        serializer = AlunoSerializer(alunos, many=True)
        
        # Devolve a resposta com o código HTTP 200 (Sucesso)
        return Response(serializer.data, status=status.HTTP_200_OK)