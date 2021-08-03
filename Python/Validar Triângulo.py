print('\033[33m-=-\033[m'*10)
print('\033[1;36mValidação de Triângulos\033[m')
print('\033[33m-=-\033[m'*10)
print('Digite os valores dos lados do triângulo.')

a = int(input('\033[4;34mPrimeiro lado:\033[m '))
b = int(input('\033[4;35mSegundo lado:\033[m '))
c = int(input('\033[4;36mTerceiro lado:\033[m '))

if (b - c) < a < (b + c) and (a - c)  < b < (a + c) and (a - b)  < c < (a + b):
    print('\033[1;32mTriângulo possível.\033[m')
else:
    print('\033[1;31mTriângulo impossível.\033[m')