nome = str(input('Digite o seu nome completo: ')).strip()
nome1= nome.split()
print('Seu primeiro nome é {}'.format(nome1[0]))
print('Seu último nome é {}'.format(nome1[len(nome1)-1]))