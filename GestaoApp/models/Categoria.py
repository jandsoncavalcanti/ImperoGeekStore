from django.db import models

class Categoria(models.Model):
  descricao = models.CharField(unique=True, max_length=255)

  def __str__(self):
    return self.descricao

  def __unicode__(self):
    return unicode(self.descricao)

  class Meta:
    managed = False
    db_table = 'Categoria'