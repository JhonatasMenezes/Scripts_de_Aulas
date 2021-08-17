// Função que exibe asteriscos

exibirAsteriscos(10);

function exibirAsteriscos(limite){
    if(limite > 10)
        return console.log('Apenas até 10 números por favor!'); 
    let string = '';
    for(let i = 0; i <= limite;i++){
        string += '*';
        console.log(string);
    }
}