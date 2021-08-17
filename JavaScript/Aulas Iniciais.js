// Função básica de output
console.log("Jhonatas");

// Variáveis iniciam com o comando 'let' e são case sensitive
let idadE = 24;
let iDade = 45;
console.log(idadE);
console.log(iDade);

// Constanstes (não se pode alterar o valor)
const valorIngressoAdulto = 20;
console.log(valorIngressoAdulto);

// Tipos primirtivos 
// Referência
let nome = 'Jhonatas123 $$$'; // string literal - qualquer caracteres entre aspas
let idade = 25.4; // number literal - qualquer número, inteiro ou decimal
let estaAprovado = true; // boolean
let sobrenome; // undefined
let corSelecionada = null; // serve como uma 'constante' de redefinição

// Tipagem Dinâmica
console.log(typeof nome);
console.log(typeof idade);
console.log(typeof estaAprovado);
console.log(typeof sobrenome);
console.log(typeof corSelecionada);

// Objetos 
let pessoa = {
    nome: 'Júlio',
    idade: 25,
    estaAprovado: true,
    sobrenome: 'de Souza'
};
console.log(pessoa);
console.log(typeof pessoa);
console.log(pessoa.nome, pessoa.idade);

// Arrays
let familia = [26, 45, 50, 17, 'jhonatas', true];
console.log(familia);
console.log(familia[2]); // mostrar índice específico do array
console.log(familia.length);

// Functions
// Nome: Verbo + Substantivo
let corSite = 'azul';
function resetaCor(cor,tonalidade){
    corSite = cor +' '+tonalidade;
};

console.log(corSite);
resetaCor('verde','água');
console.log(corSite);
// criar uma função como exercício
function indiceArray(array, num1, num2){
    console.log(array[num1]);
    console.log(array[num2]);
};

indiceArray(familia, 4, 5);

// Tipos de função: a que retorna algo, e a que não reotorna nada
function adcionarNumero(numero){
    numero =+ numero
};
function somarNumero(numero){
    return numero = numero + numero
};

let soma1 = somarNumero(5);
console.log(soma1)
let soma2 = adcionarNumero(3);
console.log(soma2)

// Operadores Aritiméticos
// + , - , * , / , **
let salario = 100; 
console.log(salario + salario)
console.log(salario - salario)
console.log(salario * salario)
console.log(salario / salario)
console.log(5 ** 5)
// ++ , -- (incremento e decremento)
let numEro = 18;
console.log(++numEro);
console.log(--numEro);

// Operadores Atribuição
// = , += 
valorQualquer = 20; // operador ' = '
console.log(valorQualquer);
valorQualquer += valorQualquer; 
// operador ' += ', representa a operação: valorQualquer = valorQualquer + valorQualquer 
console.log(valorQualquer);

// Operadores de Comparação
// igualdade restrita ' === ' 
console.log(1 === 1);
console.log('1' === 1);
// igualdade irrestrita ' == '
console.log(1 == 1);
console.log('1' == 1);
// Operador Ternário ' = > ? : '
let pontos = 101
let tipo = pontos > 100 ? 'Premium' : 'Comum';
console.log(tipo)

// Operadores Lógicos
// ==, != , < , > , >= , <= , && , || , ! 
let maiorDeIdade = true;
let possuiCNH = false;
// Operador e (&&) - retorna true se todos os operandos forem true
let podeAplicarE = maiorDeIdade && possuiCNH;
console.log('Pode aplicar: ', podeAplicarE);
// OPerador ou (||) - retorna true se algum dos operandos forem true 
let podeAplicarOU = maiorDeIdade || possuiCNH;
console.log('Pode aplicar: ', podeAplicarOU);
// OPerador não (!) - retorna true se algum dos operandos forem true 
let podeAplicarNOT = true != true;
console.log('Pode aplicar: ', podeAplicarNOT);
// Falsy - undefied, null, 0, false, '', NaN (not a number)
// Truthy - Tudo que não seja Falsy
let corPersonalizada = '';
let corPadrao = 'Azul';
let corPerfil = corPersonalizada || corPadrao;
console.log(corPerfil);

// Operadores Bitwise

