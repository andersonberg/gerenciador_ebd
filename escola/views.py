from django.shortcuts import render
from rest_framework import generics
from escola.models import Classe
from escola.serializers import ClasseSerializer


class ClasseList(generics.ListAPIView):
    """
    List all classes in EBD.
    """

    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer
    paginate_by = 10


class ClasseRetrieve(generics.RetrieveAPIView):
    """
    Recovering a classe of EBD.
    """

    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer


class ClasseCreate(generics.CreateAPIView):
    """
    Create a new classe.
    """

    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer


class ClasseUpdate(generics.UpdateAPIView):
    """
    Update a classe.
    """

    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer


class ClasseDelete(generics.DestroyAPIView):
    """
    Delete a classe.
    """

    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer
