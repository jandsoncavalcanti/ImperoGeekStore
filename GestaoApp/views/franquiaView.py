from django.http import HttpResponse, JsonResponse
from GestaoApp.forms import FranquiaForm, FranquiaSearchForm
from GestaoApp.models import Franquia
from django.shortcuts import redirect, get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def criaFranquia(request):
  if request.method == "POST":
    form = FranquiaForm(request.POST)
    if form.is_valid():
      form.save()
      messages.add_message(request, messages.SUCCESS, 'Criado com sucesso.')
      form = FranquiaForm()
  else:
    form = FranquiaForm()
  return render(request, 'parametros_form.html', {'form': form, 'header_text' : 'Inserir Franquia', 'lista_url' : 'lista_franquia', 'novo_url' : 'nova_franquia'})

@login_required
def editaFranquia(request, pk):
  franquia = get_object_or_404(Franquia, pk=pk)
  if request.method == "POST":
    form = FranquiaForm(request.POST, instance=franquia)
    if form.is_valid():
      form.save()
      messages.add_message(request, messages.SUCCESS, 'Alterado com sucesso.')
      return redirect('nova_franquia')
  else:
    form = FranquiaForm(instance=franquia)
  return render(request, 'parametros_form.html', {'form': form, 'header_text' : 'Editar Franquia', 'lista_url' : 'lista_franquia', 'novo_url' : 'nova_franquia'})

@login_required
def listaFranquia(request):
  franquia_list = Franquia.objects.all().order_by('descricao')
  
  if request.method == "POST":
    form = FranquiaSearchForm(request.POST)

    if form['descricao'].value() and not form['descricao'].value() =="":
      franquia_list = franquia_list.filter(descricao__icontains=form['descricao'].value())
    if form['fabricante'].value():
      franquia_list = franquia_list.filter(fabricante_id=form['fabricante'].value())

    form = FranquiaSearchForm(initial={'descricao': form['descricao'].value(), 'fabricante' : form['fabricante'].value()})
  else:
    form = FranquiaSearchForm()

  paginator = Paginator(franquia_list, 10)

  page = request.GET.get('page')
  try:
    lista = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an integer, deliver first page.
    lista = paginator.page(1)
  except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    lista = paginator.page(paginator.num_pages)

  return render(request, 'parametros_list.html', {'lista': lista, 'form' : form, 'header_text' : 'Lista de Franquias', 'lista_url' : 'lista_franquia', 'novo_url' : 'nova_franquia', 'editar_url' : 'edita_franquia', 'is_franquia' : True, 'remover_url' : '/franquia/remove/'})

def removeFranquia(request):
  franquia = get_object_or_404(Franquia, pk=request.GET.get('elemento', None))
  data = None
  try:
    franquia.delete()
    data = {'booleano' : True}
  except:
    data = {'mensagem' : 'Falha ao excluir elemento devido a haver dados que dependem dele', 'booleano' : False}
  return JsonResponse(data)