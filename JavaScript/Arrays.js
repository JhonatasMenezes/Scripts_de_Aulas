// Introdução a Arrays
// constantes
const num = [1,2,3];
const marcas = [
    {id:1,nome:'a'},
    {id:2,nome:'b'}
];
const myrray = ['Jhonatas', 24, '12/02/1997'];
const numeros = [1,2,3,4,5,6];


// Add elementos
console.log(num);
//inicio
num.unshift(0);
console.log(num);
// meio
num.splice(1,0,'a');
console.log(num);
//final
num.push(5);
console.log(num);
// exercise
console.log(myrray);
myrray.unshift('id: 1')
myrray.splice(2,0,'Solteiro')
myrray.push('email@email.com')
console.log(myrray);
let len = myrray.length
console.log(len);


// Encontrar elementos
console.log(myrray);
// tipos primitivos
console.log(myrray.indexOf(24));
console.log(myrray.lastIndexOf(24));
console.log(myrray.indexOf(2) !== -1);
console.log(myrray.includes('id: 1'));
// tipo referência
let marca = marcas.find(function(marca){
   return marca.nome === 'a'; 
});
let marca2 = marcas.find(marca => marca.nome === 'a');
console.log(marca);
console.log(marca2);


// Remover elementos
console.log(numeros);
//inicio
let remPrm = numeros.shift()
//meio
let remMei = numeros.splice(2,1)
//final
let remUlt = numeros.pop();

console.log(remPrm);
console.log(remUlt);
console.log(remMei);
console.log(numeros);



// Dividir Elementos


// Dividir Arrays


// Combinar Arrays

