from django.http import HttpResponse, JsonResponse
from GestaoApp.forms import CategoriaForm, CategoriaSearchForm
from GestaoApp.models import Categoria
from django.shortcuts import redirect, get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def criaCategoria(request):
  if request.method == "POST":
    form = CategoriaForm(request.POST)
    if form.is_valid():
      form.save()
      messages.add_message(request, messages.SUCCESS, 'Criado com sucesso.')
      form = CategoriaForm()
  else:
    form = CategoriaForm()
  return render(request, 'parametros_form.html', {'form': form, 'header_text' : 'Inserir Categoria', 'lista_url' : 'lista_categoria', 'novo_url' : 'nova_categoria'})

@login_required
def editaCategoria(request, pk):
  categoria = get_object_or_404(Categoria, pk=pk)
  if request.method == "POST":
    form = CategoriaForm(request.POST, instance=categoria)
    if form.is_valid():
      form.save()
      messages.add_message(request, messages.SUCCESS, 'Alterado com sucesso.')
      return redirect('nova_categoria')
  else:
    form = CategoriaForm(instance=categoria)
  return render(request, 'parametros_form.html', {'form': form, 'header_text' : 'Editar Categoria', 'lista_url' : 'lista_categoria', 'novo_url' : 'nova_categoria'})

@login_required
def listaCategoria(request):
  categoria_list = Categoria.objects.all().order_by('descricao')
  
  if request.method == "POST":
    form = CategoriaSearchForm(request.POST)

    if form['descricao'].value() and not form['descricao'].value() =="":
      categoria_list = categoria_list.filter(descricao__icontains=form['descricao'].value())
      form = CategoriaSearchForm(initial={'descricao': form['descricao'].value()})
  else:
    form = CategoriaSearchForm()

  paginator = Paginator(categoria_list, 10)

  page = request.GET.get('page')
  try:
    lista = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an integer, deliver first page.
    lista = paginator.page(1)
  except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    lista = paginator.page(paginator.num_pages)

  return render(request, 'parametros_list.html', {'lista': lista, 'form' : form, 'header_text' : 'Lista de Categorias', 'lista_url' : 'lista_categoria', 'novo_url' : 'nova_categoria', 'editar_url' : 'edita_categoria', 'remover_url' : '/categoria/remove/'})

def removeCategoria(request):
  categoria = get_object_or_404(Categoria, pk=request.GET.get('elemento', None))
  data = None
  try:
    categoria.delete()
    data = {'booleano' : True}
  except:
    data = {'mensagem' : 'Falha ao excluir elemento devido a haver dados que dependem dele', 'booleano' : False}
  return JsonResponse(data)