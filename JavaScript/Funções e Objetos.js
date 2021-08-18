// Funções de Fábrica - camelCase
function criarCelular(marcaCell,tamTela,capBateria){
    return {
        marcaCell,
        tamTela,
        capBateria,
        ligar(){
            console.log('Fazendo ligação...');
        }
    }
}

const celular1 = criarCelular('Apple', 6.5, 3500);
console.log(celular1);
celular1.ligar(); 

// Função Construtor - PascalCase
function Celular(marcaCell,tamTela,capBateria){
    this.marcaCell = marcaCell,
    this.tamTela = tamTela,
    this.capBateria = capBateria,
    this.ligar = function(){
        console.log('Fazendo ligação...');
    }
}

const celular = new Celular('Asus', 5.5, 5000);
console.log(celular);

// Montador de Postagem de Blog
function Postagem(titulo,mensagem,autor){
    this.titulo = titulo,
    this.mensagem = mensagem,
    this.autor = autor,
    this.views = 0,
    this.comments = [],
    this.live = false
}

let postToday = new Postagem('Meu Projeto','Detalhes do projeto','Jhonatas') 
console.log(postToday);


// Dnimamicidade de Objetos
const mouse = {
    cor: 'red',
    marca: 'Razer'
}

mouse.velocidade = 100;
mouse.trocarDpi = function(){
    console.log('trocando velocidade');
}
console.log(mouse)

// Clonando Objetos
const novoObjeto = Object.assign({
    bateria: 5000
},celular);
console.log(novoObjeto);

const objeto2 = {...celular1};
console.log(objeto2);