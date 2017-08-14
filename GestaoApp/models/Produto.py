from django.db import models

class Produto(models.Model):
  descricao = models.CharField(max_length=255)
  precoatual = models.FloatField(db_column='precoAtual', blank=True, null=True)  # Field name made lowercase.
  franquia = models.ForeignKey('Franquia', models.DO_NOTHING)
  categoria = models.ForeignKey('Categoria', models.DO_NOTHING)

  def __str__(self):
    return self.categoria.descricao + ' - ' + self.franquia.fabricante.descricao + ' - ' + self.descricao

  def __unicode__(self):
    return unicode(self.categoria.descricao + ' - ' + self.franquia.fabricante.descricao + ' - ' + self.descricao)

  class Meta:
    managed = False
    db_table = 'Produto'
    unique_together = (('descricao', 'franquia'),)