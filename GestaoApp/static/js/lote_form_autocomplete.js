$("#id_antiga_descricao").change(function () {
	if ($(this).val()) {
    var produto = $(this).val();
    $.ajax({
      url: '/ajax/lote_autocomplete/',
      data: {'produto': produto},
      dataType: 'json',
      success: function (data) {
        if (data.valor) {
          document.getElementById("valor").innerHTML = "Valor unitário atual: " + data.valor.toString();
        } else {
        	document.getElementById("valor").innerHTML = " ";
        }
        if (data.quantidade) {
          document.getElementById("quantidade").innerHTML = "Quantidade atual: " + data.quantidade.toString();
        } else {
        	document.getElementById("quantidade").innerHTML = " ";
        }
      }
    });
	} else {
		document.getElementById("valor").innerHTML = " ";
		document.getElementById("quantidade").innerHTML = " ";
	}
});

$( document ).ready(function() {
  if ($("#id_custoTotal").val() && $("#id_quantidadeTotal").val() && $("#id_valorVenda").val()) {
    document.getElementById("lucro_total").innerHTML = "Lucro sobre lote: " + ((parseFloat($("#id_valorVenda").val().replace(".","").replace(",", ".")) * $("#id_quantidadeTotal").val()) - parseFloat($("#id_custoTotal").val().replace(".","").replace(",", "."))).toFixed(2).toString().replace(".", ",");
  }
  if ($("#id_custoUnitario").val() && $("#id_valorVenda").val()) {
    document.getElementById("lucro_unidade").innerHTML = "Lucro sobre unidade: " + (parseFloat($("#id_valorVenda").val().replace(".","").replace(",", ".")) - parseFloat($("#id_custoUnitario").val().replace(".","").replace(",", "."))).toFixed(2).toString().replace(".", ",");
  }
  if ($("#id_produto").val()) {
    $.ajax({
      url: '/ajax/lote_autocomplete/',
      data: {'produto': $("#id_produto").val()},
      dataType: 'json',
      success: function (data) {
        if (data.valor) {
          document.getElementById("valor").innerHTML = "Valor unitário atual: " + data.valor.toString();
        } else {
          document.getElementById("valor").innerHTML = " ";
        }
        if (data.quantidade) {
          document.getElementById("quantidade").innerHTML = "Quantidade atual: " + data.quantidade.toString();
        } else {
          document.getElementById("quantidade").innerHTML = " ";
        }
      }
    });
  }
});