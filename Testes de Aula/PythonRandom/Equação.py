#Início do algoritomo  
#algoritmo para resolver uma pequena equação de 2° grau
print('a² / b³ = x')
      #definição de vaiáveis com perguntas ao usuário
n1 = int(input('Defina o valor de a: '))
n2 = int(input('Defina o valor de b: '))
      #váriaveis definidas
    #execução da fórmula
print('a² = {}'.format(n1**2))
print('b³ = {}'.format(n2**3))
print('{} / {} = x'.format((n1**2),(n2**3)))
  #exibição do resulado na tela :)
print('Com base nas informações o valor de x é {:.4}'.format((n1**2) / (n2**3)))

