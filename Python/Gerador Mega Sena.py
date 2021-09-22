from random import randint
from time import sleep

jogos = []

print('-='*18)
print('JOGO MEGA SENA'.center(36))
print('-='*18)

numJogos = int(input('Quantos jogos você deseja? '))
print(f'-=-=-=-= SORTEANDO {numJogos} JOGOS =-=-=-=-=')

for i in range(1, numJogos+1):
    for c in range(0, 6):
        jogos += [randint(1, 60)]
    for n in jogos:
        if jogos.count(n) > 1:
            jogos.remove(n)
            jogos.append(randint(1, 60))
    jogos.sort()
    print(f'Jogo {i}: {jogos}')
    jogos.clear()
    sleep(0.5)

print('-=-=-=-=','BOA SORTE'.center(17),'=-=-=-=-=')
