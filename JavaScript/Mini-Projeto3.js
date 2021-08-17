// FizzBuzz
// Diviível por 3 -> Fizz
// Diviível por 5 -> Buzz
// Diviível por 5 -> FizzBuzz
// Não dovosível por 3 ou 5 -> entrada
// Se a entrada não for um número, retornar mensagem dizendo isso.

function fizzBuzz(entrada){
    if(typeof entrada != typeof 1){
        return 'Digite um número por favor!';
    } else if((entrada % 3 === 0) && (entrada % 5 === 0)){
        return 'FizzBuzz';
    } else if((entrada % 3) === 0){
        return 'Fizz';
    } else if((entrada % 5) === 0){
        return 'Buzz';
    } else {
        return entrada;
    }
}

const resultado = fizzBuzz(15);
console.log(resultado);