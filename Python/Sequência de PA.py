inicio1 = 89
inicio2 = 119
pf1 = 0
pf2 = 0

print(f'Considerando a sequência: 89, 119, 96, 127, 103, 135, 110, 143....')
print('Quantas posições da sequência irão existir entre os números 1000 e 1500?')

while True:    
    if inicio1 < 1500:
        inicio1 += 7    
    elif inicio1 >= 1500:
        break
    
    if inicio2 < 1500:
        inicio2 += 8
    elif inicio2 >= 1500:
        pass    
    
    if inicio1 >= 1000 and inicio1 < 1500:
        pf1 += 1
    
    if inicio2 >= 1000 and inicio2 < 1500:
        pf2 += 1

print(f'\nSão {pf1 + pf2} posições da sequência entre 1000 e 1500.')