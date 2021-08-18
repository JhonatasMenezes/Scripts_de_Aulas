// Função Math

// random (gera números aleaórios)
console.log(Math.random())
// max (mostra o valor maximo em uma lista)
console.log(Math.max(2, 4, 8))
//min (mostra o valor mínimo em uma lista)
console.log(Math.min(3,5,1,9))

// String
// tipo ptimitivo
const mensagem = 'Primeira mensagem.';
// tipo objeto (trasnforma uma string em um objeto)
const mensagem2 = new String(' Segunda mensagem.');

console.log(mensagem);
console.log(mensagem2);

// Funções de string mais usadas
// indice (mostra o caractere presente em certo índice)
console.log(mensagem[2])

// length (tamanho da string)
console.log(mensagem.length)

// include (confere se certo parâmetro esta presente na string)
console.log(mensagem2.includes('Segunda'))
console.log(mensagem2.includes('Primeira'))

// startsWith/endsWith (confere o final e o início da string)
console.log(mensagem.startsWith('Pri'))
console.log(mensagem.startsWith('Seg'))
console.log(mensagem.endsWith('Pri'))
console.log(mensagem.endsWith('random'))

// indexOf (procura o índice de certo parâmetro)
console.log(mensagem.indexOf('mensagem'))

// replace (troca strings pelo parâmetro inserido)
console.log(mensagem2.replace('Segunda','Nova'))

// trim (remove espaços por padrão, mas pode remover caracteres tabém se for passado em parâmetros)
console.log(mensagem2.trim())

// split (divide strings em objetos)
console.log(mensagem.split(' '))

// Template Literals
// Object {}
// Boolean true,false
// String '', ""
// Template ``
const mensagem3 = `Primeira linha da string.
Segunda linha da string.
E assim por diante.`;
console.log(mensagem3);
// Mensagem dinâmica
const nome = 'Jhonatas'
const numero = 10
const email = 
`Boa tarde ${nome} ${numero * 5}!

Venho através deste repassar a seguinte mensagem.

Att, Jhonatas.
`;
console.log(email);


// Date
const data1 = new Date();
console.log(data1);
const data2 = new Date('01/01/2021 20:01');
console.log(data2);
const data3 = new Date(2021,07,17,20,03); // dessa forma o mês é contado em array, sempre 1 a mais
console.log(data3);
// métodos
data3.setFullYear(2022); data3.setMonth(0);
console.log(data3);
console.log(data3.toDateString());
console.log(data3.toTimeString());


