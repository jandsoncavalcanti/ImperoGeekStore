# -*- coding: utf-8 -*-
from dal import autocomplete
from django import forms
from GestaoApp.models import Lote, Categoria, Franquia

class LoteSubForm(forms.ModelForm):
  class Meta:
    model = Lote
    fields = ('quantidadetotal',)
    widgets = {
      'quantidadetotal' : forms.NumberInput(attrs={'min': '1', 'class' : 'form-control', 'onkeydown': 'return(PreventNegative(this, event))', 'style' : ' margin-top: 10px;', 'placeholder' : 'Quantidade do produto no lote'},),
    }

  custoTotal = forms.CharField(widget=forms.TextInput(attrs={'onkeydown': 'return(MascaraMoeda(this, event));', 'class' : 'form-control', 'style' : ' margin-top: 10px;', 'placeholder' : 'Custo Total do produto no lote'},),)
  valorcompraunitario = forms.CharField(widget=forms.TextInput(attrs={'onkeydown': 'return(MascaraMoeda(this, event))', 'class' : 'form-control', 'style' : ' margin-top: 10px;', 'placeholder' : 'Custo Unitário do produto no lote'},),)
  valorvendaunitario = forms.CharField(widget=forms.TextInput(attrs={'onkeydown': 'return(MascaraMoeda(this, event))', 'class' : 'form-control', 'placeholder' : 'Novo valor de venda do produto'},),)

  def clean(self):
    cleaned_data = super(LoteSubForm,self).clean()
    custoUnitarioClean = cleaned_data.get("valorcompraunitario")
    valorVendaClean = cleaned_data.get("valorvendaunitario")

    if custoUnitarioClean:
      if float(custoUnitarioClean.replace(".","").replace(",", ".")) <= 0.0:
        raise forms.ValidationError(u"O campo Valor Unitário do produto tem que ter valor maior que 0.00")
    else:
      raise forms.ValidationError(u"É Obrigatório preencher o campo Valor Unitário do produto")
      
    if valorVendaClean:
      if float(valorVendaClean.replace(".","").replace(",", ".")) <= 0.0:
        raise forms.ValidationError(u"O campo Valor Unitário de venda tem que ter valor maior que 0.00")
      if custoUnitarioClean:
        if float(valorVendaClean.replace(".","").replace(",", ".")) <= float(custoUnitarioClean.replace(".","").replace(",", ".")):
          raise forms.ValidationError(u"O campo Valor Unitário de venda tem que ter valor maior que o campo Valor Unitário do produto")
    else:
      raise forms.ValidationError(u"É Obrigatório preencher o campo Valor Unitário de venda")
    return self.cleaned_data

class LoteForm(forms.ModelForm):
  class Meta:
    model = Lote
    fields = ('produto', 'quantidadetotal',)
    widgets = {
      'produto': autocomplete.ModelSelect2(url='produto_autocomplete',forward=['categoria','franquia'],attrs={'data-minimum-input-length': 3, 'data-placeholder' : 'Descrição do produto - Ex.: Obi-Wan tam G'},),
      'quantidadetotal' : forms.NumberInput(attrs={'min': '1', 'class' : 'form-control', 'onkeydown': 'return(PreventNegative(this, event))', 'style' : ' margin-top: 10px;', 'placeholder' : 'Quantidade do produto no lote'},),
    }

  categoria = forms.ModelChoiceField(queryset=Categoria.objects.none(),widget=autocomplete.ModelSelect2(url='categoria_autocomplete',attrs={'data-minimum-input-length': 3, 'data-placeholder' : 'Categoria - Ex.: Camisa, Livro, Filme'},), required=False)
  franquia = forms.ModelChoiceField(queryset=Franquia.objects.none(),widget=autocomplete.ModelSelect2(url='franquia_autocomplete',attrs={'data-minimum-input-length': 3, 'data-placeholder' : 'Franquia - Ex.: Halo, Game of Thrones, Star Wars'},), required=False)
  custoTotal = forms.CharField(widget=forms.TextInput(attrs={'onkeydown': 'return(MascaraMoeda(this, event));', 'class' : 'form-control', 'style' : ' margin-top: 10px;', 'placeholder' : 'Custo Total do produto no lote'},),)
  valorcompraunitario = forms.CharField(widget=forms.TextInput(attrs={'onkeydown': 'return(MascaraMoeda(this, event))', 'class' : 'form-control', 'style' : ' margin-top: 10px;', 'placeholder' : 'Custo Unitário do produto no lote'},),)
  valorvendaunitario = forms.CharField(widget=forms.TextInput(attrs={'onkeydown': 'return(MascaraMoeda(this, event))', 'class' : 'form-control', 'placeholder' : 'Novo valor de venda do produto'},),)

  def clean(self):
    cleaned_data = super(LoteForm,self).clean()
    custoUnitarioClean = cleaned_data.get("valorcompraunitario")
    valorVendaClean = cleaned_data.get("valorvendaunitario")

    if custoUnitarioClean:
      if float(custoUnitarioClean.replace(".","").replace(",", ".")) <= 0.0:
        raise forms.ValidationError(u"O campo Valor Unitário do produto tem que ter valor maior que 0.00")
    else:
      raise forms.ValidationError(u"É Obrigatório preencher o campo Valor Unitário do produto")
      
    if valorVendaClean:
      if float(valorVendaClean.replace(".","").replace(",", ".")) <= 0.0:
        raise forms.ValidationError(u"O campo Valor Unitário de venda tem que ter valor maior que 0.00")
      if custoUnitarioClean:
        if float(valorVendaClean.replace(".","").replace(",", ".")) <= float(custoUnitarioClean.replace(".","").replace(",", ".")):
          raise forms.ValidationError(u"O campo Valor Unitário de venda tem que ter valor maior que o campo Valor Unitário do produto")
    else:
      raise forms.ValidationError(u"É Obrigatório preencher o campo Valor Unitário de venda")
    return self.cleaned_data

class LoteSearchForm(forms.ModelForm):
  class Meta:
    model = Lote
    fields = ('produto',)
    widgets = {
      'produto': autocomplete.ModelSelect2(url='produto_autocomplete',forward=['categoria','franquia'],attrs={'data-minimum-input-length': 3, 'data-placeholder' : 'Descrição do produto - Ex.: Obi-Wan tam G'},),
    }

  categoria = forms.ModelChoiceField(queryset=Categoria.objects.none(),widget=autocomplete.ModelSelect2(url='categoria_autocomplete',attrs={'data-minimum-input-length': 3, 'data-placeholder' : 'Categoria - Ex.: Camisa, Livro, Filme'},), required=False)
  franquia = forms.ModelChoiceField(queryset=Franquia.objects.none(),widget=autocomplete.ModelSelect2(url='franquia_autocomplete',attrs={'data-minimum-input-length': 3, 'data-placeholder' : 'Franquia - Ex.: Halo, Game of Thrones, Star Wars'},), required=False)

  def __init__(self, *args, **kwargs):
    super(LoteSearchForm, self).__init__(*args, **kwargs)
    self.fields['produto'].required = False