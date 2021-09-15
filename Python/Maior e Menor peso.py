pesos = []
maior = 0
menor = 0

for p in range(0, 5):
    peso = input(f'Peso da {p+1}ª pessoa: ')
    pesos += [peso]
    if p == 1:
        maior = peso
        menor = peso

for i in pesos:
    if i > maior:
        maior = i
    if i < menor:
        menor = i    

print(maior, menor)