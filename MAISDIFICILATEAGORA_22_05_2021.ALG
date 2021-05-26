algoritmo "MaisDificilAteAgora_22_05_2021"
var
   in, fim, con: inteiro
inicio
      Escreva("Início: ")
      leia(in)
      Escreva("Fim: ")
      leia(fim)
      Escreval("-------------------")
      Escreval("  C O N T A N D O  ")
      Escreval("-------------------")
      Se (fim > in) entao
         con <- in
         Enquanto (con <= fim) faca
              Escreva(con,"...")
              con <- con + 1
         Fimenquanto
      senao
        Se (in > fim) entao
           con <- in
           Enquanto (con >= fim) faca
              Escreva(con,"...")
              con <- con - 1
           FimEnquanto
        FimSe
      FimSe
fimalgoritmo