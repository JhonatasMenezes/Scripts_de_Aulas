// Função que mostra números primos em uma sequência

exibirPrimos(15);

function exibirPrimos(limite){
    for(let i = 2; i <= limite;i++)
        if(numeroPrimo(i)) console.log(i);
}

function numeroPrimo(num){
    for(let n = 2; n < num;n++){
        if(num % n === 0)
            return false;
    }
    return true;
}
