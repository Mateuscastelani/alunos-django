from rest_framework import serializers
from .models import AlunoUnivesp

class AlunoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AlunoUnivesp
        fields = ['nome', 'sobrenome', 'matricula']