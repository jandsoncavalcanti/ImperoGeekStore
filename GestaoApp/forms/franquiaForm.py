# -*- coding: utf-8 -*-
from dal import autocomplete
from django import forms
from GestaoApp.models import Franquia, Fabricante

class FranquiaForm(forms.ModelForm):
  class Meta:
    model = Franquia
    fields = ('__all__')
    widgets = {
      'descricao': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Descrição - Ex.: Halo, Game of Thrones, Star Wars', 'autofocus' : 'autofocus'}),
      'fabricante' : autocomplete.ModelSelect2(url='fabricante_autocomplete',attrs={'data-minimum-input-length': 3, 'data-placeholder' : 'Fabricante - Ex.: Microsoft, Sony, Blizzard'},),
    }

class FranquiaSearchForm(forms.ModelForm):
  class Meta:
    model = Franquia
    fields = ('__all__')
    widgets = {
      'descricao': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Descrição - Ex.: Halo, Game of Thrones, Star Wars', 'autofocus' : 'autofocus'}),
      'fabricante' : autocomplete.ModelSelect2(url='fabricante_autocomplete',attrs={'data-minimum-input-length': 3, 'data-placeholder' : 'Fabricante - Ex.: Microsoft, Sony, Blizzard'},),
    }

  def __init__(self, *args, **kwargs):
    super(FranquiaSearchForm, self).__init__(*args, **kwargs)
    self.fields['descricao'].required = False
    self.fields['fabricante'].required = False
    