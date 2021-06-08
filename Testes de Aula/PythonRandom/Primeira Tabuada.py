#algoritmo para exibir a tabuada de qualquer número
    #definição da única váriavel necessária 
    n = int(input('Digite um número: '))
  #exibiçao do resultado
  print('Aqui está a tabuada de {}: '.format(n)),'\n'
  print('='*11)
  print('{} x {:2} = {}'.format(n, 0, 0),'\n'
  '{} x {:2} = {}'.format(n, 1, n*1),'\n'
  '{} x {:2} = {}'.format(n, 2, n*2), '\n'
  '{} x {:2} = {}'.format(n, 3, n*3), '\n'
  '{} x {:2} = {}'.format(n, 4, n*4),'\n'
  '{} x {:2} = {}'.format(n, 5, n*5),'\n'
  '{} x {:2} = {}'.format(n, 6, n*6),'\n'
  '{} x {:2} = {}'.format(n, 7, n*7),'\n'
  '{} x {:2} = {}'.format(n, 8, n*8),'\n'
  '{} x {:2} = {}'.format(n, 9, n*9),'\n'
  '{} x {:2} = {}'.format(n, 10, n*10))
  print('='*11)
