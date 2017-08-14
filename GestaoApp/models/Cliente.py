from django.db import models
from django.core.validators import EmailValidator
class Cliente(models.Model):
  nome = models.CharField(max_length=200, unique=True)
  telefone = models.CharField(max_length=20, null=True, blank=True)
  email = models.EmailField(null=True, blank=True, validators=[EmailValidator])

  def __str__(self):
    return self.nome + ' - ' + self.email + ' - ' + self.telefone

  def __unicode__(self):
    return unicode(self.nome + ' - ' + self.email + ' - ' + self.telefone)

  class Meta:
    managed = True
    db_table = 'Cliente'