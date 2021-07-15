// Grade Average
algoritmo "semnome"
var
   n1, n2, media: real
inicio
      escreva("Digite a primeira nota: ")
      leia(n1)
      escreva("Digite a segunda nota: ")
      leia(n2)
      media <- (n1 + n2) / 2
      escreval("A méddia do aluno foi:", media)
      se (media >= 7) entao
         escreval("Aluno aprovado!")
      senao
           se (media >= 5) e (media <= 7) entao
             escreval("Aluno de recuperação!")
           senao
             escreval("ALUNO REPROVADO!!!")
           fimse
      fimse
fimalgoritmo
