from time import sleep

print('=' * 20)
print(' ANÁLISE DE NOMES')
print('=' * 20)
sleep(1.2)
nome = input('Digite seu nome completo: ')
pNome = nome.find(" ")
sleep(1.2)
print('Todas as letras minúsculas: ', nome.lower())
print('Todas maiúsculas: ', nome.upper())
print('Total de letras: ', len(nome.replace(' ','')))
print(f'O primeiro nome tem {pNome} letras')