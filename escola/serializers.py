from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

from rest_framework import serializers
from escola.models import Classe, Componente, Departamento


class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = ('id', 'numero', 'departamento', 'faixa')


class ComponenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Componente
        fields = ('id',
                  'nome',
                  'classe',
                  'cartao_membro',
                  'tipo',
                  'sexo',
                  'nascimento',
                  'logradouro',
                  'numero_end',
                  'complemento_end',
                  'bairro',
                  'cep',
                  'cidade',
                  'uf',
                  'telefone',
                  'celular',
                  'email',
                  'estado_civil')


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('id', 'nome', 'coordenador')
