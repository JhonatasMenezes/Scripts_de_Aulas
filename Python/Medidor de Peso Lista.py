import sys

lista = []
aux = []
maisPesado = []
maisLeve = []

print('=-'*20)
print('Medidor de Peso'.center(40))
print('=-'*20)
print('Digite as informções a seguir')

while True:
    aux.append(str(input('Nome: ')))
    aux.append(str(input('Peso: ')))
    lista.append(aux[:])
    
    if len(lista) == 1:
        maisPesado = lista[:]
        maisLeve = lista[:]
    else:
        if aux[1] > maisPesado[0][1]:
            maisPesado.clear()
            maisPesado.append(aux[:])
        elif aux[1] == maisPesado[0][1]:
            maisPesado.append(aux[:])
            
        if aux[1] < maisLeve[0][1]:
            maisLeve.clear()
            maisLeve.append(aux[:])    
        elif aux[1] == maisLeve[0][1]:
            maisLeve.append(aux[:])
    
    aux.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break
    elif resp == 'S':
        pass
    else:
        print('Informação inválida. Programa encerrado!')
        sys.exit()

print(f'No total, foram {len(lista)} pessoas cadastradas.')

print('As pessoas mais pesadas são: ')
for p in range(0, len(maisPesado)):
    print(f'{maisPesado[p][0]} com {maisPesado[p][1]}.00Kg') 

print('As pessoas mais leves são: ', end='')
for p in range(0, len(maisLeve)):
    print(f'{maisLeve[p][0]} com {maisLeve[p][1]}.00 Kg') 
    