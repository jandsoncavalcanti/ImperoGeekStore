$( document ).ready(function() {
  if ($("#lotevenda_list").val()) {
    var lista = JSON.parse($("#lotevenda_list").val());

    if (lista.length > 0) {
      tableObject = document.getElementById("tabela");
      var header = tableObject.createTHead();
      var row = header.insertRow(0);
      var cell = row.insertCell(0);
      cell.innerHTML = "<b>produto</b>";
      var cell = row.insertCell(1);
      cell.innerHTML = "<b>quantidade</b>";
      var cell = row.insertCell(2);
      cell.innerHTML = "<b>valor</b>";
      var cell = row.insertCell(3);
      cell.innerHTML = "<b>remover</b>";
      tableObject.deleteRow(-1);

      var valor = 0;
      for (i = 0; i < lista.length; i++) {
        var row = tableObject.insertRow(-1);
        var cell1 = row.insertCell(0);
        cell1.innerHTML = lista[i]["produto"]["descricao"];
        var cell2 = row.insertCell(1);
        cell2.innerHTML = lista[i]["quantidade"];
        var cell3 = row.insertCell(2);
        cell3.innerHTML = lista[i]["valor"];
        var cell4 = row.insertCell(3);
        cell4.innerHTML = "<a ref=\"#\" onclick=\"remover(" + lista[i]["produto"]["id"] + ")\" >Remover<\/a>";
        valor += parseFloat(lista[i]["valor"]) * lista[i]["quantidade"];
      }
      var desconto_porcentagem = document.getElementById("id_descontoPorcentagem");
      if (desconto_porcentagem.value && valor > 0) {
        valor -= valor*parseFloat(desconto_porcentagem.value)/100;
      }
      var desconto_valor = document.getElementById("id_descontoValor");
      if (id_descontoValor.value && valor > 0) {
        valor -= parseFloat(desconto_valor.value.replace(".","").replace(",", "."));
      }
      var valor_total = document.getElementById("valor_total");
      if (valor_total) {
        valor_total.innerHTML = valor.toFixed(2).toString().replace(/^0+/, '').replace(".", ",");
      }
    }
  }
});

function adicionar(){
  $.ajax({
    url: '/ajax/adicionar/',
    data: {
      'produto' : $("#id_produto").val(),
      'lotevenda_list' : $("#lotevenda_list").val(),
      'produto_valor' : $("#produto_valor").val(),
      'quantidade' : $("#id_quantidade").val(),
      'maximo' : $("#maximo").val(),
    },
    dataType: 'json',
    success: function (data) {
      if (data.resultado && data.teste_b) {
        $("#lotevenda_list").val(data.resultado);
        loadTable(data.resultado);
        $("#id_quantidade").val(1);
        calcula_valor();
      }
      if (data.mensagem) {
        document.getElementById("message").innerHTML = data.mensagem;
      } else {
        document.getElementById("message").innerHTML = "";
      }
    }
  });
}

function loadTable(data) {
  tableObject = document.getElementById("tabela");
  if (tableObject.rows.length == 1) {
    var header = tableObject.createTHead();
    var row = header.insertRow(0);
    var cell = row.insertCell(0);
    cell.innerHTML = "<b>produto</b>";
    var cell = row.insertCell(1);
    cell.innerHTML = "<b>quantidade</b>";
    var cell = row.insertCell(2);
    cell.innerHTML = "<b>valor</b>";
    var cell = row.insertCell(3);
    cell.innerHTML = "<b>remover</b>";
    tableObject.deleteRow(-1);
  }
  var lista = JSON.parse(data);

  var row = tableObject.insertRow(-1);
  var cell1 = row.insertCell(0);
  cell1.innerHTML = lista[lista.length-1]["produto"]["descricao"];
  var cell2 = row.insertCell(1);
  cell2.innerHTML = lista[lista.length-1]["quantidade"];
  var cell3 = row.insertCell(2);
  cell3.innerHTML = lista[lista.length-1]["valor"];
  var cell4 = row.insertCell(3);
  cell4.innerHTML = "<a ref=\"#\" onclick=\"remover(" + lista[lista.length-1]["produto"]["id"] + ")\" >Remover<\/a>";
}

$("#id_produto").change( function() {
  if ($(this).val()) {
    var produto = $(this).val();
    $.ajax({
    url: '/ajax/lote_autocomplete/',
    data: {'produto': produto},
    dataType: 'json',
    success: function (data) {
      if (data.valor) {
        $("#produto_valor").val(data.valor);
      }
      else {
        $("#produto_valor").val(0);
      }
      if (data.quantidade) {
        document.getElementById("id_quantidade").setAttribute("max", data.quantidade);
        $("#maximo").val(data.quantidade);
        document.getElementById("message").innerHTML = "";
      } else {
        document.getElementById("id_quantidade").setAttribute("max", 0);
        $("#maximo").val(0);
        document.getElementById("message").innerHTML = "Esse produto não poderá ser adicionado";
      }
    }
  });
}});

function remover(produto) {

  $.ajax({
    url: 'ajax/remover/',
    data: {
      'produto' : produto,
      'lotevenda_list' : $("#lotevenda_list").val(),
    },
    dataType: 'json',
    success: function (data) {
      $("#lotevenda_list").val(data.resultado);
      tableObject = document.getElementById("tabela");
      tableObject.deleteRow(data.indice+1);
      if (tableObject.rows.length == 1) {
        var header = tableObject.createTHead();
        var row = header.insertRow(0);
        var cell = row.insertCell(0);
        cell.innerHTML = "Não há produtos adicionados";
        tableObject.deleteRow(data.indice+1);
      }
      calcula_valor();
    }
  });
}

$("#id_descontoValor").focusout(function(){
    calcula_valor();
});

$("#id_descontoPorcentagem").focusout(function(){
    calcula_valor();
});

function calcula_valor () {
  lista = $("#lotevenda_list").val();
  var table = document.getElementById("tabela");
  var desconto_porcentagem = document.getElementById("id_descontoPorcentagem");
  var desconto_valor = document.getElementById("id_descontoValor");
  var valor_total = document.getElementById("valor_total");
  var valor = 0;
  if (table) {
    for (var i = 1, row; row = table.rows[i]; i++) {
      valor += parseFloat(row.cells.item(2).innerHTML) * row.cells.item(1).innerHTML;
    }
    if (desconto_porcentagem.value && valor > 0) {
      valor -= valor*parseFloat(desconto_porcentagem.value)/100;
    }
    if (id_descontoValor.value && valor > 0) {
      valor -= parseFloat(desconto_valor.value.replace(".","").replace(",", "."));
    }
  }
  if (valor_total) {
    valor_total.innerHTML = valor.toFixed(2).toString().replace(".", ",");
  }
};

jQuery("input.telefone")
  .mask("(99) 9999-9999?9")
  .focusout(function (event) {  
    var target, phone, element;  
    target = (event.currentTarget) ? event.currentTarget : event.srcElement;  
    phone = target.value.replace(/\D/g, '');
    element = $(target);  
    element.unmask();  
    if(phone.length > 10) {  
      element.mask("(99) 99999-999?9");  
    } else {  
      element.mask("(99) 9999-9999?9");  
    }  
  });