// Função de soma que retorna 
// soma de multiplos de 3 e 5
function somar(limite){
    let soma = 0;
    for(let i = 1;i <= limite;i++){
        
        if((i % 3) === 0 || (i % 5) === 0){
            soma += i;
            console.log(i,'é multiplo de 3 ou 5!')
        } else{
            console.log(i,'não é multiplo de 3 ou 5!')
        }
    }
    console.log('Soma total', soma);
}
somar(12);