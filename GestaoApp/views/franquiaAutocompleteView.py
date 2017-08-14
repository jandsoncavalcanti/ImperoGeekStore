from dal import autocomplete
from django.http import HttpResponse
from GestaoApp.models import Franquia
from django.http import JsonResponse

class FranquiaAutocompleteView(autocomplete.Select2QuerySetView):
  def get_queryset(self):
 
    if self.q:
      qs = Franquia.objects.filter(descricao__icontains=self.q)[:7]
    else:
      qs = Franquia.objects.none()

    return qs