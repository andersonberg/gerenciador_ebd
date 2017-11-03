from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from escola.models import Classe, Componente, Departamento
from escola.serializers import ClasseSerializer, ComponenteSerializer, DepartamentoSerializer


class ClasseList(generics.ListAPIView):
    """
    List all classes in EBD.
    """

    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer
    paginate_by = 10


class ClasseViewHTML(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pages/classes.html'

    def get(self, request):
        queryset = Classe.objects.all()
        return Response({'classes': queryset})


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


class DepartamentoList(generics.ListAPIView):
    """
    List all departamentos in EBD.
    """

    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    paginate_by = 10


class DepartamentoView(generics.RetrieveUpdateDestroyAPIView):
    """
    Departamento view.
    """

    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer


class DepartamentoCreate(generics.CreateAPIView):
    """
    Departamento view for create endpoint.
    """

    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
