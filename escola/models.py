from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


class Classe(models.Model):
    '''
    Definição da Classe da ebd
    '''
    numero = models.CharField(max_length=50, blank=False)
    tipo = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ('numero', 'tipo',)


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    def __str__(self):
        return self.username
