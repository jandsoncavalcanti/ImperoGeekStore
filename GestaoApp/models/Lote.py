from django.db import models
from django.utils import timezone

class Lote(models.Model):
  datainsercao = models.DateTimeField(db_column='dataInsercao', blank=True, null=True, default=timezone.now)  # Field name made lowercase.
  valorcompraunitario = models.FloatField(db_column='valorCompraUnitario')  # Field name made lowercase.
  valorvendaunitario = models.FloatField(db_column='valorVendaUnitario')  # Field name made lowercase.
  quantidadetotal = models.IntegerField(db_column='quantidadeTotal')  # Field name made lowercase.
  quantidadevendida = models.IntegerField(db_column='quantidadeVendida', blank=True, null=True, default=0)  # Field name made lowercase.
  produto = models.ForeignKey('Produto', models.DO_NOTHING)

  class Meta:
    managed = False
    db_table = 'Lote'