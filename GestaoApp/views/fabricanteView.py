from django.http import HttpResponse, JsonResponse
from GestaoApp.forms import FabricanteForm, FabricanteSearchForm
from GestaoApp.models import Fabricante
from django.shortcuts import redirect, get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def criaFabricante(request):
  if request.method == "POST":
    form = FabricanteForm(request.POST)
    if form.is_valid():
      form.save()
      messages.add_message(request, messages.SUCCESS, 'Criado com sucesso.')
      form = FabricanteForm()
  else:
    form = FabricanteForm()
  return render(request, 'parametros_form.html', {'form': form, 'header_text' : 'Inserir Fabricante', 'lista_url' : 'lista_fabricante', 'novo_url' : 'novo_fabricante'})

@login_required
def editaFabricante(request, pk):
  fabricante = get_object_or_404(Fabricante, pk=pk)
  if request.method == "POST":
    form = FabricanteForm(request.POST, instance=fabricante)
    if form.is_valid():
      form.save()
      messages.add_message(request, messages.SUCCESS, 'Alterado com sucesso.')
      return redirect('novo_fabricante')
  else:
    form = FabricanteForm(instance=fabricante)
  return render(request, 'parametros_form.html', {'form': form, 'header_text' : 'Editar Fabricante', 'lista_url' : 'lista_fabricante', 'novo_url' : 'novo_fabricante'})

@login_required
def listaFabricante(request):
  fabricante_list = Fabricante.objects.all().order_by('descricao')
  
  if request.method == "POST":
    form = FabricanteSearchForm(request.POST)

    if form['descricao'].value() and not form['descricao'].value() =="":
      fabricante_list = fabricante_list.filter(descricao__icontains=form['descricao'].value())
      form = FabricanteSearchForm(initial={'descricao': form['descricao'].value()})
  else:
    form = FabricanteSearchForm()

  paginator = Paginator(fabricante_list, 10)

  page = request.GET.get('page')
  try:
    lista = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an integer, deliver first page.
    lista = paginator.page(1)
  except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    lista = paginator.page(paginator.num_pages)

  return render(request, 'parametros_list.html', {'lista': lista, 'form' : form, 'header_text' : 'Lista de Fabricantes', 'lista_url' : 'lista_fabricante', 'novo_url' : 'novo_fabricante', 'editar_url' : 'edita_fabricante', 'remover_url' : '/fabricante/remove/'})

def removeFabricante(request):
  fabricante = get_object_or_404(Fabricante, pk=request.GET.get('elemento', None))
  data = None
  try:
    fabricante.delete()
    data = {'booleano' : True}
  except:
    data = {'mensagem' : 'Falha ao excluir elemento devido a haver dados que dependem dele', 'booleano' : False}
  return JsonResponse(data)