from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

from rest_framework import serializers
from escola.models import Classe, Componente, Departamento, Caderneta


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
        fields = ('__all__')
