// Ler propriedades de um objeto e exibir no console quando for uma string.

const filme = {
    titulo: 'Liga da Justiça',
    ano: 2021,
    diretor: 'Zack Snyder',
    personagem: 'Superman',
    horas: 4.15
}

exibirStrings(filme);

function exibirStrings(lista){
    for(dado in lista)
        if(typeof lista[dado] === 'string')
            console.log(lista[dado]);    
}