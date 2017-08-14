from django.db import models

class EstoqueVenda(models.Model):
  estoque = models.ForeignKey('Estoque', models.DO_NOTHING)
  venda = models.ForeignKey('Venda', models.DO_NOTHING)
  quantidade = models.IntegerField()
  valorvendaunitario = models.FloatField()  # Field name made lowercase.

  class Meta:
  	managed = True
  	db_table = 'EstoqueVenda'