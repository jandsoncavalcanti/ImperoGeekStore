# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
from GestaoApp.forms import LoteForm, LoteSearchForm, LoteSubForm, ProdutoSearchForm
from decimal import Decimal
from GestaoApp.models import Lote, Estoque
from django.shortcuts import redirect, get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
import datetime
from decimal import Decimal

@login_required
@transaction.atomic
def criaLote(request):
  if request.method == "POST":
    lote_form = LoteForm(request.POST)
    if lote_form.is_valid():
      lote = lote_form.save(commit=False)
      lote.valorcompraunitario = Decimal(lote_form.cleaned_data.get('valorcompraunitario').replace(".","").replace(",", "."))
      lote.valorvendaunitario = Decimal(lote_form.cleaned_data.get('valorvendaunitario').replace(".","").replace(",", "."))
      lote.produto.precoatual = lote.valorvendaunitario

      lote.produto.save()
      lote.save()

      estoque = Estoque.objects.filter(produto=lote.produto).first()
      estoque.quantidadetotal += lote.quantidadetotal
      estoque.save()

      messages.add_message(request, messages.SUCCESS, 'Criado com sucesso.')
      lote_form = LoteForm()
  else:
    lote_form = LoteForm()
  return render(request, 'produto_and_lote_form.html', {'subform': lote_form, 'subheader_text' : 'Inserir Lote'})

@login_required
@transaction.atomic
def editaLote(request, pk):
  lote = get_object_or_404(Lote, pk=pk)
  if request.method == "POST":
    lote_form = LoteSubForm(request.POST, instance=lote)
    produto_form = ProdutoSearchForm(instance=lote.produto)
    produto_form.fields['descricao'].widget.attrs['readonly'] = True
    if lote_form.is_valid():
      try:
        lote_edit = lote_form.save(commit=False)
        lote_edit.valorcompraunitario = Decimal(lote_form.cleaned_data.get('valorcompraunitario').replace(".","").replace(",", "."))
        lote_edit.valorvendaunitario = Decimal(lote_form.cleaned_data.get('valorvendaunitario').replace(".","").replace(",", "."))
        lote_last = Lote.objects.filter(produto=lote.produto).last()

        estoque = Estoque.objects.filter(produto=lote.produto).first()
        estoque.quantidadetotal += (lote_edit.quantidadetotal - Lote.objects.filter(pk=lote.pk).first().quantidadetotal)
        estoque.full_clean()
        estoque.save()

        if lote_last == lote:
          lote_edit.produto.precoatual = lote_edit.valorvendaunitario
          lote_edit.produto.save()
        lote_edit.save()
        messages.add_message(request, messages.SUCCESS, 'Alterado com sucesso.')
        return redirect('novo_lote')
      except ValidationError as e:
        raise e
  else:
    custoTotal = lote.quantidadetotal * lote.valorcompraunitario
    lote_form = LoteSubForm(instance=lote, initial={'valorcompraunitario' : str(lote.valorcompraunitario).replace(".",","), 'valorvendaunitario': str(lote.valorvendaunitario).replace(".",","), 'custoTotal': str(custoTotal).replace(".",","), })
    produto_form = ProdutoSearchForm(instance=lote.produto)
    produto_form.fields['descricao'].widget.attrs['readonly'] = True
  return render(request, 'produto_and_lote_form.html', {'form' : produto_form, 'subform': lote_form, 'header_text' : 'Produto do lote', 'subheader_text' : 'Alterar Lote'})

@login_required
def listaLote(request):
  lote_list = Lote.objects.all().order_by('produto__descricao','-datainsercao')

  if request.method == "POST":
    lote_form = LoteSearchForm(request.POST)
    if lote_form['produto'].value():
      lote_list = lote_list.filter(produto_id=lote_form['produto'].value())
    if lote_form['categoria'].value():
      lote_list = lote_list.filter(categoria=categoria)
    if lote_form['franquia'].value():
      lote_list = lote_list.filter(franquia=franquia)
  else:
    lote_form = LoteSearchForm()

  paginator = Paginator(lote_list, 10)

  page = request.GET.get('page')
  try:
    lotes = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an integer, deliver first page.
    lotes = paginator.page(1)
  except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    lotes = paginator.page(paginator.num_pages)

  return render(request, 'lote_list.html', {'lotes': lotes, 'form' : lote_form, 'remover_url' : '/lote/remove/'})

@transaction.atomic
def removeLote(request):
  lote = get_object_or_404(Lote, pk=request.GET.get('elemento', None))
  lote_list = Lote.objects.filter(produto=lote.produto)
  data = None
  try:
    if lote.quantidadevendida == 0:
      if lote == lote_list.last():
        if lote_list.count() > 1:
          lote.produto.precoatual = lote_list[len(lote_list) - 2].valorvendaunitario
        else:
          lote.produto.precoatual = Decimal(0)
        lote.produto.save()

      estoque = Estoque.objects.filter(produto=lote.produto).first()
      estoque.quantidadetotal -= lote.quantidadetotal
      estoque.full_clean()
      estoque.save()
      lote.delete()

      data = {'booleano' : True}
    else:
      data = {'mensagem' : 'Falha ao excluir elemento devido a quantidade vendida de elementos do lote ser maior que zero', 'booleano' : False}
  except:
    data = {'mensagem' : 'Falha ao excluir elemento devido a haver dados que dependem dele', 'booleano' : False}
  return JsonResponse(data)