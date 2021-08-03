print('==============================')
print('     RADAR DE VELOCIDADE      ')
print('==============================')
vel = int(input('Velocidade atual do veículo em Km/h: '))
mult = 0
 
if vel > 80:
    mult = (vel - 80) * 7.123
    print('Limite de velocidade excedido!')
    print(f'Multa no valor de R${mult:.2f}')
else:
    print('Parabéns, você está dentro dos limites!')
    
print('==============================')
print('Efetue o pagamento em até 30 dias, ou então,')
print('procure os orgãos necessários para recorrer!')