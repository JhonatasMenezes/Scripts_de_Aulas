algoritmo "Cadastro de Pessoas"
var
   Sex, Resp:caractere
   Idad, Cab, ResultM, ResultF: inteiro
inicio
      ResultM <- 0
      ResultF <- 0
      Repita
      Escreval("==========================")
      Escreval("    SELETOR DE PESSOAS    ")
      Escreval("==========================")
      Escreva("Qual o sexo? [M/F] ")
      leia(Sex)
      Escreva("Qual a idade? ")
      leia(Idad)
      Escreval("Qual a cor do cabelo? ")
      Escreval("=========================")
      Escreval("[1] Preto")
      Escreval("[2] Castanho")
      Escreval("[3] Ruivo")
      Escreval("[4] Loiro")
      leia(cab)
      Escreval("==========================")
      Se (Sex = "M") e (Idad >= 18) e (Cab = 2) entao
         ResultM <- ResultM + 1
      Fimse
      Se (Sex = "F") e (Idad >= 25) e (Idad <= 30) e (Cab = 4) entao
         ResultF <- ResultF + 1
      FimSe
      Escreva("Continuar cadastro? [S/N]")
      leia(Resp)
      limpatela
      Ate (Resp = "N")
      Escreval("Total de homens com mais de 18 anos e cabelo castanho: ",ResultM)
      Escreval("Total de mulheres entre 25 e 30 anos e cabelo loiro: ",ResultF)
fimalgoritmo