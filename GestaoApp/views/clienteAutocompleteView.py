from dal import autocomplete
from django.http import HttpResponse
from GestaoApp.models import Cliente
from django.http import JsonResponse

class ClienteAutocompleteView(autocomplete.Select2QuerySetView):
  def get_queryset(self):
 
    if self.q:
      qs = Cliente.objects.filter(nome__icontains=self.q)[:7]
    else:
      qs = Cliente.objects.none()

    return qs