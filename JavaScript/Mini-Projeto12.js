// Comparar igualdade entre 2 objetos

function Endereco(rua,cidade,cep){
    this.rua = rua,
    this.cidade = cidade,
    this.cep = cep
}

const endereco1 = new Endereco('a','b','c');
const endereco2 = new Endereco('a','b','c');

function saoIguais(objeto1,objeto2){
    if(
    objeto1.rua === objeto2.rua &&
    objeto1.cidade === objeto2.cidade &&
    objeto1.cep === objeto2.cep)
        return true
    else return false;
}

let valid = saoIguais(endereco1, endereco2);
console.log(valid);

function enderecoMemoria(objeto1,objeto2){
    return objeto1 === objeto2;
}

const memo = enderecoMemoria(endereco1,endereco2);
console.log(memo);