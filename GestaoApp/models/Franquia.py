from django.db import models

class Franquia(models.Model):
  descricao = models.CharField(max_length=255)
  fabricante = models.ForeignKey('Fabricante', models.DO_NOTHING)

  def __str__(self):
    return self.fabricante.descricao + ' - ' + self.descricao

  def __unicode__(self):
    return unicode(self.fabricante.descricao + ' - ' + self.descricao)

  class Meta:
    managed = False
    db_table = 'Franquia'
    unique_together = (('descricao', 'fabricante'),)