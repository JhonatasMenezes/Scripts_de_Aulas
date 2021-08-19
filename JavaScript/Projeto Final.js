// Segurança Virtual de uma Festa Vip

// lista de convidados
const lista1 = {
    anfitriao: 'Jhonatas',
    convidado: ['Paulo','Jose', 'Maria']
}
const lista2 = {
    anfitriao: 'Luis',
    convidado: ['Jhonatas','Joao', 'Marina']
}
// função para pesquisar anfitrião
function consultaAnfitriao(anfitriao){
    if(anfitriao === lista1.anfitriao)
        return lista1.anfitriao;
    else if (anfitriao === lista2.anfitriao)
        return lista2.anfitriao;    
    else 
        return 'NOT_FOUND';
}
// função para pesquisar convidado
function consultaNome(anfitriao,nome){
    const anft = consultaAnfitriao(anfitriao);
    if(anft === lista1.anfitriao){
        for(let i of lista1.convidado){
            if(i === nome)
                return true;
        }
    }else if(anft === lista2.anfitriao){    
        for(let i of lista2.convidado){
            if(i === nome)
                return true;
        }
    }
}
// função para cruzamento de dados
function cruzarDados(){
    // receber nomes da pessoa
    nome = document.getElementById('nome').value;
    anfitriao = document.getElementById('anfitriao').value
    const simNao = consultaNome(anfitriao,nome);
    // mostrar resultado do cruzamento de informações
    if(simNao === true)
        document.getElementById('final').innerText = 'Entrada autorizada!';
    else    
        document.getElementById('final').innerText = 'Entrada não autorizada!';
    
} 
    