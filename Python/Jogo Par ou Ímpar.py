import random
import time
import os

s = 0
c = 0
continua = True

while True:
    print('='*30)
    print('JOGO PAR OU ÍMPAR')
    print('='*30)
    while continua == True:
        n = int(input('Escolha um número: '))
        parimp = str(input('Par ou Ímpar? [P/I] ')).upper()
        rand = random.randint(1, 20)
        s = n + rand
        print(f'Número PC: {rand}')
        time.sleep(2)
        print(f'A soma dos números é {s}')
        time.sleep(2)        
        if ((s % 2) == 0 and parimp == 'P') or ((s%2) == 1 and parimp == 'I'):
            c += 1
            print(f'PARABÉNS!!! GANHOU MAIS 1 PONTO. TOTAL: {c}')
            continua = True
        else:
            print('DESSA VEZ NÃO DEU :/... DERROTA!')
            print(f'VOCÊ FEZ {c} PONTOS.')
            continua = False
    break
     