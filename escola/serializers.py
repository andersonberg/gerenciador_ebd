from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

from rest_framework import serializers
from escola.models import Classe


class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = ('id', 'numero', 'tipo')
