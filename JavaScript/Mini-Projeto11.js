// Montador de Endereços

function inserirEndereco(rua,cidade,CEP){
    const endereco = {
    rua: rua,
    cidade: cidade,
    CEP: CEP,
    }
    return endereco;
}

const endereco = inserirEndereco('Rua das Cnaleiras', 'São Paulo', 09999123)

function exibirEndereco(obj){
    for(let chave in obj)
        console.log(chave,obj[chave]);
}


exibirEndereco(endereco);