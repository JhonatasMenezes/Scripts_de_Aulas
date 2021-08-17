// For loop
for (let i = 0; i < 5 ; i++){
    console.log('Estou aprendendo!', i);
}

for (let i = 5; i >= 1; i--){
    if(i % 2 !== 0){
        console.log(i);
    }
}


// While loop
// verifica a condição antes de executar
let a = 5;

while (a >= 1){
    if(a % 2 !== 0){
        console.log(a);
    }
    a--;
}

// Do..While loop
// verifica a condição depois de executar a 1° vez
let b = 1;

do {
    console.log('digitando...', b);
    b++;
} while(b <= 10)


// For..in loop
const pessoa = {
    nome: 'Jhonatas',
    idade: 24,
    cidade: 'SBC'
};

for(let chave in pessoa) { // key-value
    console.log(chave, pessoa[chave]);
}

const cores = ['Verelho', 'Azul', 'Verde'];

for (indice in cores){
    console.log(cores[indice])
}


// For..of loop - melhor com iteração sobre arrays
for(let cor of cores){
    console.log(cor);
}
