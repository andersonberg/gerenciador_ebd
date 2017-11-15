from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

from rest_framework import serializers
from escola.models import Classe, Componente, Departamento, Evento


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


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ('__all__')
