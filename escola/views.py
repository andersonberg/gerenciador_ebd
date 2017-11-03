from django.shortcuts import render
from rest_framework import generics
from escola.models import Classe, Componente
from escola.serializers import ClasseSerializer, ComponenteSerializer


class ClasseList(generics.ListAPIView):
    """
    List all classes in EBD.
    """

    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer
    paginate_by = 10


class ClasseView(generics.RetrieveUpdateDestroyAPIView):
    """
    Classe view for read-write-delete endpoints.
    """

    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer


class ClasseCreate(generics.CreateAPIView):
    """
    Classe view for create endpoint.
    """

    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer


class ComponenteList(generics.ListAPIView):
    """
    List all components in EBD.
    """

    queryset = Componente.objects.all()
    serializer_class = ComponenteSerializer
    paginate_by = 10


class ComponenteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Componente view.
    """

    queryset = Componente.objects.all()
    serializer_class = ComponenteSerializer


class ComponenteCreate(generics.CreateAPIView):
    """
    Componente view for create endpoint.
    """

    queryset = Componente.objects.all()
    serializer_class = ComponenteSerializer
