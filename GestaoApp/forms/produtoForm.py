# -*- coding: utf-8 -*-
from dal import autocomplete
from django import forms
from GestaoApp.models import Produto, Categoria, Franquia

class ProdutoForm(forms.ModelForm):
  class Meta:
    model = Produto
    fields = ('descricao','categoria','franquia',)
    widgets = {
      'descricao' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Descrição - Ex.: Obi-Wan tam G', 'autofocus' : 'autofocus'}),
      'categoria' : autocomplete.ModelSelect2(url='categoria_autocomplete',attrs={'data-minimum-input-length': 3, 'data-placeholder' : 'Categoria - Ex.: Camisa, Livro, Filme'},),
      'franquia' : autocomplete.ModelSelect2(url='franquia_autocomplete',attrs={'data-minimum-input-length': 3, 'data-placeholder' : 'Franquia - Ex.: Halo, Game of Thrones, Star Wars'},),
    }

class ProdutoSearchForm(forms.ModelForm):
  class Meta:
    model = Produto
    fields = ('descricao','categoria','franquia',)
    widgets = {
      'descricao' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Descrição - Ex.: Obi-Wan tam G', 'autofocus' : 'autofocus'}),
      'categoria' : autocomplete.ModelSelect2(url='categoria_autocomplete',attrs={'data-minimum-input-length': 3, 'data-placeholder' : 'Categoria - Ex.: Camisa, Livro, Filme'},),
      'franquia' : autocomplete.ModelSelect2(url='franquia_autocomplete',attrs={'data-minimum-input-length': 3, 'data-placeholder' : 'Franquia - Ex.: Halo, Game of Thrones, Star Wars'},),
    }

  def __init__(self, *args, **kwargs):
    super(ProdutoSearchForm, self).__init__(*args, **kwargs)
    self.fields['descricao'].required = False 
    self.fields['categoria'].required = False
    self.fields['franquia'].required = False