// custom.js

var resumoIncremento = [];

$(document).ready(function() {
  $('.adicionar-produto').on('click', function() {
    var produtoId = $(this).data('produto-id');
    var produtoNome = $(this).data('produto-nome');
    adicionarProduto(produtoId, produtoNome);
  });
});

function adicionarProduto(produtoId, produtoNome) {
  resumoIncremento.push(produtoNome);
  atualizarResumoIncremento();
  $('<input>').attr({
    type: 'hidden',
    name: 'produtos',
    value: produtoId
  }).appendTo('#pedido-form');
}

function atualizarResumoIncremento() {
  $('#resumo-incremento').text('Produtos adicionados: ' + resumoIncremento.join(', '));
}
