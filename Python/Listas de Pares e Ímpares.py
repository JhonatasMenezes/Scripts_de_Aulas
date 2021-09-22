import sys


lista = []
pares = []
impares = []
resp = ''

while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).upper()
    
    if resp == 'N':
        break
    elif resp == 'S':
        pass
    else:
        print('Valor incorreto! Finalizando programa!')
        sys.exit()

for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f'A lista completa: {lista}')
print(f'A lista de pares: {pares}')
print(f'A lsta de ímoares: {impares}')

