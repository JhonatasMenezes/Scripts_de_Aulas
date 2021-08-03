print('==============================')
print('      Viagens Paulistas       ')
print('==============================')
dest = input('Qual o destino da viagem: ')
dist = int(input('Distância em km: '))
valor = 0

if dist <= 200:
    valor = dist * 0.50
elif dist > 200:
    valor = dist * 0.45
    
print(f'Sua viagem até {dest} vai custar R${valor:.2f} no total!')
print('Aproveite a jornada! :)')