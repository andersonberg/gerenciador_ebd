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
    tipo = models.CharField(_('Type'), choices=COMPONENT_TYPES, default=ALUNO, max_length=50)
    nome = models.CharField(max_length=100)
    sexo = models.CharField(choices=SEXO_TYPES, max_length=15, blank=True, null=True)
    nascimento = models.DateField(blank=True, null=True)
    logradouro = models.CharField(max_length=100, blank=True, null=True)
    numero_end = models.IntegerField(blank=True, null=True)
    complemento_end = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField(max_length=50, blank=True, null=True)
    telefone = models.CharField(max_length=50, blank=True, null=True)
    celular = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    estado_civil = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ('nome',)
