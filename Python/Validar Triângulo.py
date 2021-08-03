a = int(input('Primeiro lado: '))
b = int(input('Segundo lado: '))
c = int(input('Terceiro lado: '))

if (b - c) < a < (b + c) and (a - c)  < b < (a + c) and (a - b)  < c < (a + b):
    print('Triângulo possível.')
else:
    print('Triângulo impossível.')