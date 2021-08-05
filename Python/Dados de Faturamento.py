
sP = 67836.43
rJ = 36678.66
mG = 29229.88
eS = 27165.48
outros = 9849.53

totalFaturamento = sP + rJ + mG + eS + outros

porcSP =  ( sP / totalFaturamento)  * 100
porcRJ = ( rJ / totalFaturamento)  * 100
porcMG = ( mG / totalFaturamento)  * 100
porcES =  ( eS / totalFaturamento)  * 100
porcOutros = ( outros / totalFaturamento)  * 100

print(f'O faturamento total foi de {totalFaturamento}.')
print('As porcentagens de cada estado em sequência são')
print(f'SP = %{porcSP:2.2f}')
print(f'RJ = %{porcRJ:2.2f}')
print(f'MG = %{porcMG:2.2f}')
print(f'ES = %{porcES:2.2f}')
print(f'Outros = %{porcOutros:.2f}')

print(porcSP+porcRJ+porcMG+porcES+porcOutros)