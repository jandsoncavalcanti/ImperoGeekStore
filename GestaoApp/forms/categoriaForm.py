# -*- coding: utf-8 -*-
from django import forms
from GestaoApp.models import Categoria

class CategoriaForm(forms.ModelForm):
  class Meta:
    model = Categoria
    fields = ('__all__')
    widgets = {
      'descricao': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Descrição - Ex.: Camisa, Livro, Filme', 'autofocus' : 'autofocus'}),
    }

class CategoriaSearchForm(forms.ModelForm):
  class Meta:
    model = Categoria
    fields = ('__all__')
    widgets = {
      'descricao': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Descrição - Ex.: Camisa, Livro, Filme', 'autofocus' : 'autofocus'}),
    }

  def __init__(self, *args, **kwargs):
    super(CategoriaSearchForm, self).__init__(*args, **kwargs)
    self.fields['descricao'].required = False