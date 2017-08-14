from dal import autocomplete
from django.http import HttpResponse
from GestaoApp.models import Categoria
from django.http import JsonResponse

class CategoriaAutocompleteView(autocomplete.Select2QuerySetView):
  def get_queryset(self):
 
    if self.q:
      qs = Categoria.objects.filter(descricao__icontains=self.q)[:7]
    else:
      qs = Categoria.objects.none()

    return qs