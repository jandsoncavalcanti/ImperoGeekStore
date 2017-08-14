from dal import autocomplete
from django.http import HttpResponse
from GestaoApp.models import Produto
from django.http import JsonResponse
import json
from django.core import serializers

class ProdutoAutocompleteView(autocomplete.Select2QuerySetView):
  def get_queryset(self):
    categoria = self.forwarded.get('categoria', None)

    franquia = self.forwarded.get('franquia', None)

    qs = Produto.objects.none()

    if self.q:
      qs = Produto.objects.filter(descricao__icontains=self.q)
      if categoria:
        qs = qs.filter(categoria=categoria)
      if franquia:
        qs = qs.filter(franquia=franquia)

    return qs