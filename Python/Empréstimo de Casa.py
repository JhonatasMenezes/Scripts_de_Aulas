# Desafio empréstimo bancário
import os
import time

def writeAlone(message):
    for letter in message:
        os.write(letter,'')
        letter += letter
        time.sleep(2)

load = '[::::::::::::::]'

print('='*25)
print('SIMULAÇÃO DE EMPRÉSTIMO')
print('='*25)

valCasa = float(input('Digite o valor da casa: '))
sal = float(input('Digite seu salário mensal: '))
anos = int(input('Digite o tempo em ANOS que deseja parcelar: '))

print('Tudo ok. Agora é só aguardar enquanto fazemos a análise.')
writeAlone(load)

parcelaQtd = anos * 12
parcelaVal = valCasa / parcelaQtd
sal30 = (sal/100) * 30

if parcelaVal > sal30:
    print('Desculpe, o seu salário não é suficiente para o empréstimo.')
elif parcelaVal <= sal30:
    print('Parabéns!!! Seu empréstimo foi aprovado!!!')

