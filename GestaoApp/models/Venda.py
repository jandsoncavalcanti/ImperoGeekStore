from django.db import models
from django.utils import timezone

class Venda(models.Model):
  cliente = models.ForeignKey('Cliente', models.DO_NOTHING, null=True)
  dataCriacao = models.DateTimeField(default=timezone.now)
  valorTotal = models.DecimalField(max_digits=10, decimal_places=2)
  valorCredito = models.DecimalField( max_digits=10, decimal_places=2, null=True, blank=True)
  parcelas = models.IntegerField(null=True, blank=True)
  valorDebito = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
  valorMoeda = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
  descontoPorcentagem = models.IntegerField(null=True, blank=True)
  descontoValor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

  class Meta:
    managed = True
    db_table = 'Venda'