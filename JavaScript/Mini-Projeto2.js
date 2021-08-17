// Escrever função que entre 2 valores retorna o maior valor
 
function max(num1, num2){
    if (num1 > num2){
        console.log('O número ',num1,' é maior!');
    } 
    else if (num1 == num2){
        console.log('Os números são iguais!')
    }
    else{
        console.log('O número ',num2,' é maior!');
    }           
}

max(8, 9);

function maxTernario(n1, n2){
    result =  n1 > n2 ? n1 : n2;
    return result;     
}

console.log('O maior número é',maxTernario(3,6)+'.');