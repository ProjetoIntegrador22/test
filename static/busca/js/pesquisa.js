
function coletarDados() {
  // Valor do input
  var cepInput = document.getElementById('cepInput').value;
  
  // Seleção do dropdown
  var dropFiltro = document.getElementById('mainFiltro').value;
  
  // Verificar cep válido
  if(/^[0-9]+$/.test(cepInput)) {
    // Se válido coletar dados
    console.log('Collected Data:', { cepInput, dropFiltro });
  } else {
    // CEP inválido
    alert('CEP não encontrado!');
  }
}
