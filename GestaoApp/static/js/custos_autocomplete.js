$("#id_custoTotal").keydown(function() {
	if ($("#id_custoTotal").val() && $("#id_quantidadetotal").val() > 0) {
		$("#id_valorcompraunitario").val((parseFloat($("#id_custoTotal").val().replace(".","").replace(",", ".")) / $("#id_quantidadetotal").val()).toFixed(2).toString().replace(".", ","));
	} else {
		$("#id_valorcompraunitario").val(null);
	}
/*
  if ($("#id_custoTotal").val() && $("#id_quantidadetotal").val() > 0 && $("#id_valorvendaunitario").val()) {
    document.getElementById("lucro_total").innerHTML = "Lucro sobre lote: " + ((parseFloat($("#id_valorvendaunitario").val().replace(".","").replace(",", ".")) * $("#id_quantidadetotal").val()) - parseFloat($("#id_custoTotal").val().replace(".","").replace(",", "."))).toFixed(2).toString().replace(".", ",");
  } else {
    document.getElementById("lucro_total").innerHTML = "Lucro sobre lote: ";
  }

  if ($("#id_valorcompraunitario").val() && $("#id_valorvendaunitario").val()) {
    document.getElementById("lucro_unidade").innerHTML = "Lucro sobre unidade: " + (parseFloat($("#id_valorvendaunitario").val().replace(".","").replace(",", ".")) - parseFloat($("#id_valorcompraunitario").val().replace(".","").replace(",", "."))).toFixed(2).toString().replace(".", ",");
  } else {
    document.getElementById("lucro_unidade").innerHTML = "Lucro sobre unidade: ";
  }
*/
});

$("#id_valorcompraunitario").keydown(function() {
	if ($("#id_valorcompraunitario").val() && $("#id_quantidadetotal").val() > 0) {
		$("#id_custoTotal").val((parseFloat($("#id_valorcompraunitario").val().replace(".","").replace(",", ".")) * $("#id_quantidadetotal").val()).toFixed(2).toString().replace(".", ","));
	} else {
		$("#id_custoTotal").val(null);
	}
/*
  if ($("#id_valorcompraunitario").val() && $("#id_valorvendaunitario").val()) {
    document.getElementById("lucro_unidade").innerHTML = "Lucro sobre unidade: " + (parseFloat($("#id_valorvendaunitario").val().replace(".","").replace(",", ".")) - parseFloat($("#id_valorcompraunitario").val().replace(".","").replace(",", "."))).toFixed(2).toString().replace(".", ",");
  } else {
    document.getElementById("lucro_unidade").innerHTML = "Lucro sobre unidade: ";
  }

  if ($("#id_custoTotal").val() && $("#id_quantidadetotal").val() > 0 && $("#id_valorvendaunitario").val()) {
    document.getElementById("lucro_total").innerHTML = "Lucro sobre lote: " + ((parseFloat($("#id_valorvendaunitario").val().replace(".","").replace(",", ".")) * $("#id_quantidadetotal").val()) - parseFloat($("#id_custoTotal").val().replace(".","").replace(",", "."))).toFixed(2).toString().replace(".", ",");
  } else {
    document.getElementById("lucro_total").innerHTML = "Lucro sobre lote: ";
  }
*/
});

$("#id_quantidadetotal").keydown(function() {
  if ($("#id_valorcompraunitario").val() && $("#id_quantidadetotal").val() > 0) {
    $("#id_custoTotal").val((parseFloat($("#id_valorcompraunitario").val().replace(".","").replace(",", ".")) * $("#id_quantidadetotal").val()).toFixed(2).toString().replace(".", ","));
  }

  if ($("#id_custoTotal").val() && $("#id_quantidadetotal").val() > 0) {
    $("#id_valorcompraunitario").val((parseFloat($("#id_custoTotal").val().replace(".","").replace(",", ".")) / $("#id_quantidadetotal").val()).toFixed(2).toString().replace(".", ","));
  }
/*
  if ($("#id_valorcompraunitario").val() && $("#id_valorvendaunitario").val()) {
    document.getElementById("lucro_unidade").innerHTML = "Lucro sobre unidade: " + (parseFloat($("#id_valorvendaunitario").val().replace(".","").replace(",", ".")) - parseFloat($("#id_valorcompraunitario").val().replace(".","").replace(",", "."))).toFixed(2).toString().replace(".", ",");
  } else {
    document.getElementById("lucro_unidade").innerHTML = "Lucro sobre unidade: ";
  }

  if ($("#id_custoTotal").val() && $("#id_quantidadetotal").val() > 0 && $("#id_valorvendaunitario").val()) {
    document.getElementById("lucro_total").innerHTML = "Lucro sobre lote: " + ((parseFloat($("#id_valorvendaunitario").val().replace(".","").replace(",", ".")) * $("#id_quantidadetotal").val()) - parseFloat($("#id_custoTotal").val().replace(".","").replace(",", "."))).toFixed(2).toString().replace(".", ",");
  } else {
    document.getElementById("lucro_total").innerHTML = "Lucro sobre lote: ";
  }
*/
});
/*
$("#id_valorvendaunitario").keydown(function() {
  if ($("#id_valorcompraunitario").val() && $("#id_valorvendaunitario").val()) {
    document.getElementById("lucro_unidade").innerHTML = "Lucro sobre unidade: " + (parseFloat($("#id_valorvendaunitario").val().replace(".","").replace(",", ".")) - parseFloat($("#id_valorcompraunitario").val().replace(".","").replace(",", "."))).toFixed(2).toString().replace(".", ",");
  } else {
    document.getElementById("lucro_unidade").innerHTML = "Lucro sobre unidade: ";
  }

  if ($("#id_custoTotal").val() && $("#id_quantidadetotal").val() > 0 && $("#id_valorvendaunitario").val()) {
    document.getElementById("lucro_total").innerHTML = "Lucro sobre lote: " + ((parseFloat($("#id_valorvendaunitario").val().replace(".","").replace(",", ".")) * $("#id_quantidadetotal").val()) - parseFloat($("#id_custoTotal").val().replace(".","").replace(",", "."))).toFixed(2).toString().replace(".", ",");
  } else {
    document.getElementById("lucro_total").innerHTML = "Lucro sobre lote: ";
  }
});
*/