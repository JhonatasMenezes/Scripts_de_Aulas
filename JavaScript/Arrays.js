// Introdução a Arrays
// constantes
const num = [1,2,3];
const marcas = [
    {id:1,nome:'a'},
    {id:2,nome:'b'}
];
const myrray = ['Jhonatas', 24, '12/02/1997'];
const numeros = [1,2,3,4,5,6];
const primeiro = [1,2,3,4];
const segundo = [5,6,7,8];
const frase = ('Olá! Bem vindo ao Javascript!');


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
// remover tudo do array
let test = numeros;
numeros.length = 0;
console.log(numeros);
console.log(test);


// Combinar e Dividir Arrays
const combinado = primeiro.concat(segundo);
console.log(combinado);
const dividio = combinado.slice(1,4);
console.log(dividio);
const combinado2 = [...combinado,...dividio];
console.log(combinado2);
const combinado3 = [...combinado,'##',...dividio,'##'];
console.log(combinado3);
const clonado = [...combinado3];
console.log(clonado);
const unirPontos = combinado2.join('.');
console.log(unirPontos);
const separador = frase.split(' ');
console.log(separador);


// foreach
combinado3.forEach((numero,indice) => console.log(numero,indice));

