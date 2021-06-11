from time import sleep
from random import choice

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = (n1, n2, n3, n4)
escolhido = choice(lista)
print('...')
sleep(0.5)
print('...')
sleep(1.8)
print('O aluno escolhido foi {}'.format(escolhido))
