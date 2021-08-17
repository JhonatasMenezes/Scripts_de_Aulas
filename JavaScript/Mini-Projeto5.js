// Par ou Impar
exibirTipo(5);

function exibirTipo(limite){
    for(let ind = 0;ind < limite; ind++){
        if((ind % 2) == 0){
            console.log(ind,'PAR');
        } else{
            console.log(ind,'ÌMPAR');
        }
    }
}
