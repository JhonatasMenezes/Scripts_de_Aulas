algoritmo "PesoIdeal"
var
   P, A, IMC: real
inicio
      Escreva("Digite o seu peso(Kg): ")
      leia(P)
      Escreva("Digite sua altura(m): ")
      leia(A)
      IMC <- P / (A ^ 2)
      Escreval("IMC: ", IMC:5:2)
      Se (IMC >= 18.5) e (IMC <= 25) entao
         Escreval("Parabéns, você está no peso ideal!")
      senao
         Escreval("Você não está na faixa de peso ideal!")
      FimSe
fimalgoritmo