// algoritmo que caucula a média de um aluno com base em duas notas
Algoritmo "Média_Nota"
   Var
      //definição das variáveis
      nota1, nota2, media: real
Inicio
    //pede as notas do aluno e armazena nas variáveis
    escreva("Digite a primeira nota do aluno: ")
    leia(nota1)
    escreva("Digite a segunda nota do aluno: ")
    leia(nota2)
    //calcula a média entre duas notas e mostra na tela
    media <- (nota1 + nota2) / 2
    escreval("A média do aluno é: ", media)
    // verifica a médiae informa se o aluno foi aprovado ou reprovado
    se (media >= 6) entao
       escreva("O aluno foi aprovado!")
    senao
       escreva("O aluno foi reprovado!")
    fimse
Fimalgoritmo