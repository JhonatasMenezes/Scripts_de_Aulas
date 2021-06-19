n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua media foi {:.2f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa. Parabéns!')
else:
    print('Sua nota foi ruim! ESTUDE MAIS!')
