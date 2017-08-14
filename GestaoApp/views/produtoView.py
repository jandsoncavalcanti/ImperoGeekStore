from django.http import HttpResponse, JsonResponse
from GestaoApp.forms import ProdutoForm, ProdutoSearchForm, LoteSubForm
from GestaoApp.models import Lote, Produto, Estoque
from decimal import Decimal
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime

@login_required
@transaction.atomic
def criaProduto(request):
  if request.method == "POST":
    produto_form = ProdutoForm(request.POST)
    lote_form = LoteSubForm(request.POST)
    if produto_form.is_valid() and lote_form.is_valid():
      produto = produto_form.save(commit=False)
      lote = lote_form.save(commit=False)

      lote.valorcompraunitario = Decimal(lote_form.cleaned_data.get('valorcompraunitario').replace(".","").replace(",", "."))
      lote.valorvendaunitario = Decimal(lote_form.cleaned_data.get('valorvendaunitario').replace(".","").replace(",", "."))


      produto.precoatual = lote.valorvendaunitario
      produto.save()

      lote.produto = produto
      lote.save()

      estoque = Estoque()
      estoque.produto = produto
      estoque.quantidadetotal = lote.quantidadetotal
      estoque.save()

      messages.add_message(request, messages.SUCCESS, 'Criado com sucesso.')
      produto_form = ProdutoForm()
      lote_form = LoteSubForm()
  else:
    produto_form = ProdutoForm()
    lote_form = LoteSubForm()
  return render(request, 'produto_and_lote_form.html', {'form': produto_form, 'subform': lote_form, 'header_text' : 'Inserir Produto', 'subheader_text' : 'Inserir Lote'})

@login_required
def editaProduto(request, pk):
  produto = get_object_or_404(Produto, pk=pk)
  if request.method == "POST":
    produto_form = ProdutoForm(request.POST, instance=produto)
    if produto_form.is_valid():
      produto_form.save()
      messages.add_message(request, messages.SUCCESS, 'Alterado com sucesso.')
      return redirect('novo_produto')
  else:
    produto_form = ProdutoForm(instance=produto)
  return render(request, 'produto_and_lote_form.html', {'form': produto_form, 'header_text' : 'Editar Produto'})

@login_required
def listaProduto(request):
  produto_list = Produto.objects.all().order_by('descricao')

  if request.method == "POST":
    produto_form = ProdutoSearchForm(request.POST)

    if produto_form['descricao'].value() and not produto_form['descricao'].value() =="":
      produto_list = produto_list.filter(descricao__icontains=produto_form['descricao'].value())
    if produto_form['categoria'].value():
      produto_list = produto_list.filter(categoria_id=produto_form['categoria'].value())
    if produto_form['franquia'].value():
      produto_list = produto_list.filter(franquia_id=produto_form['franquia'].value())
  else:
    produto_form = ProdutoSearchForm()

  paginator = Paginator(produto_list, 10)

  page = request.GET.get('page')
  try:
    produtos = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an integer, deliver first page.
    produtos = paginator.page(1)
  except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    produtos = paginator.page(paginator.num_pages)

  return render(request, 'produto_list.html', {'lista': produtos, 'form' : produto_form, 'remover_url' : '/produto/remove/'})

@transaction.atomic
def removeProduto(request):
  produto = get_object_or_404(Produto, pk=request.GET.get('elemento', None))
  estoque = Estoque.objects.filter(produto=lote.produto).first()
  data = None
  try:
    estoque.delete()
    produto.delete()
    data = {'booleano' : True}
  except:
    data = {'mensagem' : 'Falha ao excluir elemento devido a haver dados que dependem dele', 'booleano' : False}
  return JsonResponse(data)