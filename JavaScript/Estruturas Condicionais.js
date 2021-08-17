// If..Else
let hora = 10;

if (hora > 6 && hora < 12){ // condição
    // bloco de código
    console.log('Bom dia!');
}
else if(hora > 12 && hora < 18){
    // bloco de código
    console.log('Boa Tarde!');
}
else {
    console.log('Boa Noite!');
}


// Switch case
let permissao;
permissao = 'comum';

switch(permissao){
    case 'comum':
    console.log('Usuário comum');
    break;
        
    case 'gerente':
    console.log('Usuário gerente');
    break;
    
    case 'diretor':
    console.log('Usuário diretor');
    break;
    
    default:
    console.log('Usuario não reconhecdo!');    
}

