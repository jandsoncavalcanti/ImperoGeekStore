from django.conf.urls import url
from django.contrib.auth.views import *
from django.core.urlresolvers import *
from . import views

urlpatterns = [
	url(r'^$', login, {'template_name': 'login.html'}, name='login'),
	url(r'^index/$', views.index, name='index'),
	url(r'^categoria/$', views.criaCategoria, name='nova_categoria'),
	url(r'^lista_categoria/$', views.listaCategoria, name='lista_categoria'),
	url(r'^categoria/edit/(?P<pk>\d+)/$', views.editaCategoria, name='edita_categoria'),
	url(r'^categoria/remove/$', views.removeCategoria, name='remover_categoria'),
	url(r'^categoria_autocomplete/$', views.CategoriaAutocompleteView.as_view(), name='categoria_autocomplete',),
	url(r'^fabricante/$', views.criaFabricante, name='novo_fabricante'),
	url(r'^lista_fabricante/$', views.listaFabricante, name='lista_fabricante'),
	url(r'^fabricante/edit/(?P<pk>\d+)/$', views.editaFabricante, name='edita_fabricante'),
	url(r'^fabricante/remove/$', views.removeFabricante, name='remover_fabricante'),
	url(r'^fabricante_autocomplete/$', views.FabricanteAutocompleteView.as_view() ,name='fabricante_autocomplete',),
	url(r'^franquia/$', views.criaFranquia, name='nova_franquia'),
	url(r'^lista_franquia/$', views.listaFranquia, name='lista_franquia'),
	url(r'^franquia/edit/(?P<pk>\d+)/$', views.editaFranquia, name='edita_franquia'),
	url(r'^franquia/remove/$', views.removeFranquia, name='remover_franquia'),
	url(r'^franquia_autocomplete/$', views.FranquiaAutocompleteView.as_view(), name='franquia_autocomplete',),
	url(r'^produto/$', views.criaProduto, name='novo_produto'),
	url(r'^lista_produto/$', views.listaProduto, name='lista_produto'),
	url(r'^produto/edit/(?P<pk>\d+)/$', views.editaProduto, name='edita_produto'),
	url(r'^produto/remove/$', views.removeProduto, name='remover_produto'),
	url(r'^produto_autocomplete/$', views.ProdutoAutocompleteView.as_view(), name='produto_autocomplete',),
	url(r'^lote/$', views.criaLote, name='novo_lote'),
	url(r'^lista_lote/$', views.listaLote, name='lista_lote'),
	url(r'^lote/edit/(?P<pk>\d+)/$', views.editaLote, name='edita_lote'),
	url(r'^lote/remove/$', views.removeLote, name='remover_lote'),
	url(r'^venda/inicio/$', views.selecionaCliente, name='venda_inicio'),



	url(r'^cliente_autocomplete/$', views.ClienteAutocompleteView.as_view(), name='cliente_autocomplete',),
]