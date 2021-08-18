// Faixa de preço de objetos

// Objeto
let faixas = [
    {tooltip: 'Até 300',minimo: 0,maximo: 300},
    {tooltip: 'Até 700', minimo: 7000,maximo: 1000},
    {tooltip: 'Até 1000 ou mais',minimo: 1000,maximo:9999999}
]

// Função Fábrica
function criarFaixaFab(tooltip,min,max){
    return {
        tooltip,
        min,
        max
    }
}

let faixas2 = [
    criarFaixaFab('a',1,300),
    criarFaixaFab('b',300,1000),
    criarFaixaFab('c',1000,100000),
]

// Função Construtor
function criarFaixaConst(tooltip,min,max){
        this.tooltip = tooltip,
        this.min = max,
        this.max = min
}    

let faixas3 = [
    new criarFaixaConst('d',10,20),
    new criarFaixaConst('e',20,40),
    new criarFaixaConst('f',50,100)
]

console.log(faixas);
console.log(faixas2);
console.log(faixas3);
