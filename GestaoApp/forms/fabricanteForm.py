# -*- coding: utf-8 -*-
from django import forms
from GestaoApp.models import Fabricante

class FabricanteForm(forms.ModelForm):
  class Meta:
    model = Fabricante
    fields = ('__all__')
    widgets = {
      'descricao': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Descrição - Ex.: Microsoft, Sony, Blizzard', 'autofocus' : 'autofocus'}),
    }

class FabricanteSearchForm(forms.ModelForm):
  class Meta:
    model = Fabricante
    fields = ('__all__')
    widgets = {
      'descricao': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Descrição - Ex.: Microsoft, Sony, Blizzard', 'autofocus' : 'autofocus'}),
    }

  def __init__(self, *args, **kwargs):
    super(FabricanteSearchForm, self).__init__(*args, **kwargs)
    self.fields['descricao'].required = False