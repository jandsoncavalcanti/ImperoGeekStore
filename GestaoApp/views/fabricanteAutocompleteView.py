from dal import autocomplete
from django.http import HttpResponse
from GestaoApp.models import Fabricante
from django.http import JsonResponse

class FabricanteAutocompleteView(autocomplete.Select2QuerySetView):
  def get_queryset(self):
 
    if self.q:
      qs = Fabricante.objects.filter(descricao__icontains=self.q)[:7]
    else:
      qs = Fabricante.objects.none()

    return qs