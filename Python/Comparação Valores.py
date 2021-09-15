from typing import OrderedDict


valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))

if valor1 > valor2:
    print(f'Valor {valor1} maior que {valor2}')
elif valor2 > valor1:
    print(f'Valor {valor2} maior que {valor1}')
elif valor1 == valor2:
    print('Valores iguais!')
else:
    print('OPÇÃO INVÁLIDA!')