from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from escola.models import Classe, Componente, Departamento, Caderneta, CadernetaGeral
from escola.serializers import ClasseSerializer, ComponenteSerializer, DepartamentoSerializer, CadernetaSerializer, CadernetaGeralSerializer


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


class ProfessorViewHTML(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pages/componentes.html'

    def get(self, request):
        queryset = Componente.objects.filter(tipo__in=[Componente.PROFESSOR, Componente.ADJUNTO])
        return Response({'title': 'Professores', 'componentes': queryset})


class AlunoViewHTML(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pages/componentes.html'

    def get(self, request):
        queryset = Componente.objects.filter(tipo__in=[Componente.ALUNO, Componente.SECRETARIOLOCAL])
        return Response({'title': 'Alunos', 'componentes': queryset})


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


class DepartamentoViewHTML(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pages/departamentos.html'

    def get(self, request):
        queryset = Departamento.objects.all()
        return Response({'departamentos': queryset})


class ClasseDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name='pages/classe-details.html'

    def get(self, request, pk):
        classe = get_object_or_404(Classe, pk=pk)
        serializer = ClasseSerializer(classe)
        return Response({'serializer': serializer, 'classe': classe})

    def post(self, request, pk):
        classe = get_object_or_404(Classe, pk=pk)
        serializer = ClasseSerializer(classe, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'classe': classe})
        serializer.save()
        return redirect('classes')


class ComponenteDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name='pages/componente-details.html'

    def get(self, request, pk):
        componente = get_object_or_404(Componente, pk=pk)
        serializer = ComponenteSerializer(componente)

        url_redirect = 'classes'
        if componente.tipo in ['professor', 'adjunto']:
            url_redirect = 'professores'
        elif componente.tipo == 'aluno':
            url_redirect = 'alunos'
        return Response({'serializer': serializer, 'componente': componente, 'url_redirect': url_redirect})

    def post(self, request, pk):
        componente = get_object_or_404(Componente, pk=pk)
        serializer = ComponenteSerializer(componente, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'componente': componente})
        serializer.save()
        if componente.tipo in ['professor', 'adjunto']:
            return redirect('professores')
        elif componente.tipo == 'aluno':
            return redirect('alunos')
        else:
            return redirect('classes')


class ComponenteNew(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name='pages/componente-new.html'

    def get(self, request, *args, **kwargs):
        serializer = ComponenteSerializer()
        return Response({'serializer': serializer, 'url': reverse('componente_new'), 'url_redirect': 'home'})

    def post(self, request, *args, **kwargs):
        componente = Componente()
        serializer = ComponenteSerializer(componente, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'componente': componente})
        serializer.save()
        return redirect('home')


class ClasseNew(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name='pages/classe-new.html'

    def get(self, request, *args, **kwargs):
        serializer = ClasseSerializer()
        return Response({'serializer': serializer, 'url': reverse('classe_new'), 'url_redirect': 'classes'})

    def post(self, request, *args, **kwargs):
        classe = Classe()
        serializer = ClasseSerializer(classe, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'classe': classe})
        serializer.save()
        return redirect('home')


class CadernetaList(generics.ListAPIView):
    """
    List all Cadernetas in EBD.
    """

    queryset = Caderneta.objects.all()
    serializer_class = CadernetaSerializer
    paginate_by = 10


class CadernetaView(generics.RetrieveUpdateDestroyAPIView):
    """
    Caderneta view for read-write-delete endpoints.
    """

    queryset = Caderneta.objects.all()
    serializer_class = CadernetaSerializer


class CadernetaCreate(generics.CreateAPIView):
    """
    Caderneta view for create endpoint.
    """

    queryset = Caderneta.objects.all()
    serializer_class = Caderneta


class CadernetaViewHTML(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pages/caderneta.html'

    def get(self, request):
        queryset = Caderneta.objects.all()
        return Response({'cadernetas': queryset})


class CadernetaGeralList(generics.ListAPIView):
    """
    List all Cadernetas in EBD.
    """

    queryset = CadernetaGeral.objects.all()
    serializer_class = CadernetaGeralSerializer
    paginate_by = 10


class CadernetaGeralView(generics.RetrieveUpdateDestroyAPIView):
    """
    Caderneta view for read-write-delete endpoints.
    """

    queryset = CadernetaGeral.objects.all()
    serializer_class = CadernetaGeralSerializer


class CadernetaGeralCreate(generics.CreateAPIView):
    """
    Caderneta view for create endpoint.
    """

    queryset = CadernetaGeral.objects.all()
    serializer_class = CadernetaGeralSerializer
