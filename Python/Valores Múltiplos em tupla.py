num = (int(input('Digite o valor: ')),
       int(input('Digite o valor: ')),
       int(input('Digite o valor: ')),
       int(input('Digite o valor: ')))
       
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1} posição.')
else:
    print('O valor 3 não foi digitado.')

print('Os valores pares digitados foram ', end='')

for n in num:
    if n % 2 == 0:
        print(n, end='')