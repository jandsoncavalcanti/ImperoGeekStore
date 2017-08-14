# -*- coding: utf-8 -*-
from django.http import HttpResponse
from GestaoApp.forms import ClienteSearchForm
from GestaoApp.models import Cliente
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def selecionaCliente(request):
  cliente_list = Cliente.objects.all().order_by('nome')
  if request.method == "POST":
    form = ClienteSearchForm(request.POST)
    if form.is_valid():
      if form.cleaned_data.get('cliente') is not None:
        messages.add_message(request, messages.SUCCESS, u'Cliente Selecionado.')
      else:
        messages.add_message(request, messages.SUCCESS, u'Cliente Não Selecionado.')
  else:
    form = ClienteSearchForm()

  paginator = Paginator(cliente_list, 10)

  page = request.GET.get('page')
  try:
    lista = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an integer, deliver first page.
    lista = paginator.page(1)
  except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    lista = paginator.page(paginator.num_pages)
  return render(request, 'cliente_selection.html', {'form': form, 'lista' : lista, 'header_text' : 'Selecionar Cliente', 'subheader_text' : 'Lista de Clientes'})