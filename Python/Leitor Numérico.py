print('=' * 20)
print('  LEITOR NUMÉRICO')
print('=' * 20)
num = input('Digite um número entre 0 e 9999: ')

if len(num) == 1:
    print('Unidade:   ', num[0])
elif len(num) == 2:
    print('Unidade   ', num[1])
    print('Dezena:   ', num[0])
elif len(num) == 3:
    print('Unidade:  ', num[2])
    print('Dezena:   ', num[1])
    print('Centena:  ', num[0])
elif len(num) == 4:
    print('Unidade:  ', num[3])
    print('Dezena:   ', num[2])
    print('Centena:  ', num[1])
    print('Milhar:   ', num[0])
else:
    print('NÚMERO INVÁLIDO!')