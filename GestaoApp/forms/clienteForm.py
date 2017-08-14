# -*- coding: utf-8 -*-
from dal import autocomplete
from django import forms
from GestaoApp.models import Cliente

class ClienteSearchForm(forms.Form):
  cliente = forms.ModelChoiceField(queryset=Cliente.objects.none(),widget=autocomplete.ModelSelect2(url='cliente_autocomplete',attrs={'data-minimum-input-length': 3, 'data-placeholder' : 'Nome'}),required=False)

#class ClienteForm(forms.Form):
#  nome = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Nome'}),required=False)
#  telefone = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Nome'}),required=False)
#  email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control', 'placeholder' : 'Nome'}),required=False)