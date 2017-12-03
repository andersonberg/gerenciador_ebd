from datetime import date, datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


class Classe(models.Model):
    '''
    Definição da Classe da ebd
    '''

    ADULTO = 'adulto'
    JOVENS = 'jovens'
    ADOLESCENTES = 'adolescentes'
    JUVENIS = 'juvenis'
    JUNIORES = 'juniores'
    MATERNAL = 'maternal'

    FAIXA_TYPES = (
        (ADULTO, _('Adulto')),
        (JOVENS, _('Jovens')),
        (ADOLESCENTES, _('13 e 14 anos')),
        (JUVENIS, _('15 a 17 anos')),
        (JUNIORES, _('9 e 10 anos')),
        (MATERNAL, _('3 e 4 anos')),
    )

    numero = models.CharField(max_length=50, blank=False)
    departamento = models.ForeignKey(to='Departamento', blank=True, null=True)
    faixa = models.CharField(choices=FAIXA_TYPES, max_length=50, default=ADULTO)

    @property
    def professor(self):
        return self.componente_set.get(tipo=Componente.PROFESSOR)

    @property
    def adjuntos(self):
        return self.componente_set.filter(tipo=Componente.ADJUNTO)

    @property
    def qtd_alunos(self):
        return len(self.componente_set.filter(tipo=Componente.ALUNO))

    def __str__(self):
        return self.numero

    class Meta:
        ordering = ('numero', 'departamento', 'faixa')


class Departamento(models.Model):
    '''
    Representa um departamento da escola
    '''
    nome = models.CharField(max_length=100)
    coordenador = models.ForeignKey(to='Componente', blank=True, null=True)

    class Meta:
        ordering = ('nome',)

    def __unicode__(self):
        return '%s' % self.nome

    def __str__(self):
        return '%s' % self.nome


class Componente(models.Model):
    '''
    Representa um componente da escola dominical
    '''

    DIRIGENTE = 'dirigente'
    VICEDIRIGENTE = 'vice-dirigente'
    SECRETARIO = 'secretario'
    VICESECRETARIO = 'vice-secretario'
    TESOUREIRO = 'tesoureiro'
    VICETESOUREIRO = 'vice-tesoureiro'
    VICECOORDENADORA = 'vice-coordenadora'
    PROFESSOR = 'professor'
    ADJUNTO = 'adjunto'
    SECRETARIOLOCAL = 'secretario-local'
    ALUNO = 'aluno'
    COORDENADORA = 'coordenadora'

    COMPONENT_TYPES = (
        (DIRIGENTE, _('Dirigente')),
        (VICEDIRIGENTE, _('Vice-dirigente')),
        (SECRETARIO, _('Secretario')),
        (VICESECRETARIO, _('Vice-secretário')),
        (TESOUREIRO, _('Tesoureiro')),
        (VICETESOUREIRO, _('Vice-tesoureiro')),
        (VICECOORDENADORA, _('Vice-coordenadora')),
        (PROFESSOR, _('Professor')),
        (ADJUNTO, _('Adjunto')),
        (SECRETARIOLOCAL, _('Secretario Local')),
        (ALUNO, _('Aluno')),
        (COORDENADORA, _('Coordenadora')),
    )

    MASCULINO = 'masculino'
    FEMININO = 'feminino'
    SEXO_TYPES = (
        (MASCULINO, _('Masculino')),
        (FEMININO, _('Feminino')),
    )

    cartao_membro = models.IntegerField()
    classe = models.ForeignKey(to='Classe', blank=True, null=True)
    tipo = models.CharField(_('Função'), choices=COMPONENT_TYPES, default=ALUNO, max_length=50)
    nome = models.CharField(max_length=100)
    sexo = models.CharField(choices=SEXO_TYPES, max_length=15, blank=True, null=True)
    nascimento = models.DateField(blank=True, null=True)
    endereco = models.CharField(_('Endereço'), max_length=200, blank=True, null=True)
    complemento_end = models.CharField(_('Complemento'), max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField(_('UF'), max_length=50, blank=True, null=True)
    telefone = models.CharField(max_length=50, blank=True, null=True)
    celular = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    estado_civil = models.CharField(_('Estado Civil'), max_length=50, blank=True, null=True)

    class Meta:
        ordering = ('nome',)


class CadernetaGeral(models.Model):
    NORMAL = 'normal'
    MISSIONARIA = 'manha-missionaria'
    UNICA = 'classe-unica'
    ANIMADA = 'escola-animada'
    
    ESCOLA_TYPES = (
        (NORMAL, _('Normal')),
        (MISSIONARIA, _('Manhã Missionária')),
        (UNICA, _('Classe única')),
        (ANIMADA, _('Escola Animada'))
    )

    tipo = models.CharField(_('Tipo'), choices=ESCOLA_TYPES, default=NORMAL, max_length=50)
    data = models.DateField(default=date.today)

    def __str__(self):
        data_str = self.data.strftime("%d/%m/%Y")
        return data_str


class Caderneta(models.Model):

    classe = models.ForeignKey(to='Classe', related_name='classe', on_delete=models.CASCADE)
    domingo = models.ForeignKey(to='CadernetaGeral', related_name='caderneta_geral')
    presentes = models.IntegerField(blank=True, null=True, default=0)
    visitantes = models.IntegerField(blank=True, null=True, default=0)
    matriculados = models.IntegerField(blank=True, null=True, default=0)
    biblias = models.IntegerField(blank=True, null=True, default=0)
    professor = models.IntegerField(blank=True, null=True, default=0)
    adjuntos = models.IntegerField(blank=True, null=True, default=0)

    @property
    def frequencia(self):
        return (self.presentes / self.matriculados) * 100

    @property
    def atendimento(self):
        return self.presentes + self.visitantes + self.professor + self.adjuntos

    class Meta:
        ordering = ('classe',)
