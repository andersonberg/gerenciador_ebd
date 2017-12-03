from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

from rest_framework import serializers
from escola.models import Classe, Componente, Departamento, Caderneta, CadernetaGeral


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('__all__')


class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = ('__all__')


class ComponenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Componente
        fields = ('__all__')


class CadernetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caderneta
        fields = ('classe', 'domingo', 'presentes', 'visitantes', 'matriculados', 'biblias', 'professor', 'adjuntos')


class CadernetaGeralSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadernetaGeral
        fields = ('__all__')
