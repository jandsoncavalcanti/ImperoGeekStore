from django.db import models
from django.utils import timezone

class Estoque(models.Model):
  quantidadetotal = models.IntegerField(db_column='quantidadeTotal')  # Field name made lowercase.
  quantidadevendida = models.IntegerField(db_column='quantidadeVendida', blank=True, null=True, default=0)  # Field name made lowercase.
  produto = models.ForeignKey('Produto', models.DO_NOTHING)

  def clean(self):
    # Don't allow draft entries to have a pub_date.
    if self.quantidadevendida:
    	if self.quantidadevendida > self.quantidadetotal:
    		raise ValidationError(_('A quantidade em estoque do produto nao pode ser menor que sua quantidade vendida'))

  class Meta:
    managed = True
    db_table = 'Estoque'