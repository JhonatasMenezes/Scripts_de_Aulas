import os
import sys
from operator import itemgetter

jogadores = []
aux = {}
totJogos = 10

os.system('cls')
print('='*30)
print('ESTATÍSTICAS DE JOGADORES'.center(30))
print('='*30)

while True:
    totGols = 0
    semGol = 0
    
    aux['Nome'] = str(input('Nome: '))
    aux['Jogos'] = int(input('Número de jogos: '))
    
    for n in range(0, int(aux['Jogos'])):
        gol = int(input(f"Quantos gols {aux['Nome']} fez na {n+1}ª partida: "))
        totGols += gol
        if gol < 1:
            semGol += 1
    
    aux['Gols'] = totGols
    aux['Jogos Sem Gol'] = semGol
    aux['Média Gols/Partida'] = float(aux['Gols'] / aux['Jogos'])
    aux['Jogos Sem Jogar'] = totJogos - aux['Jogos']
    
    jogadores.append(aux.copy())
    aux.clear()
    
    deletes = {}
    if len(jogadores) > 1:
        for j in range(0, len(jogadores)):
            if jogadores[j]['Gols'] > jogadores[j-1]['Gols']:
                deletes = jogadores[j] 
                del(jogadores[j])
                jogadores.insert(0, deletes)
            
    
    resp = str(input('Adicionar mais jogadores? [S/N] ')).upper()
    
    if resp == 'N':
        break
    elif resp == 'S':
        pass
    else:
        print('Resposta Inválida! Encerrando...')
        sys.exit()

print('='*32)
print(f'RESULTADOS DE {len(jogadores)} JOGADORES'.center(32))
print('='*32)
print('Nº  ', 'NOME'.center(11),'| JOGOS | GOLS ')
for p in range(0, len(jogadores)):
    print(f"{p+1}     {jogadores[p]['Nome'].center(10)} |   {jogadores[p]['Jogos']}   |  {jogadores[p]['Gols']}")

while True:
    resp = int(input('Digite o número do Jogador para detalhes [999 sair]: '))
    os.system('cls')
    if resp == 999:
        break
    for k, v in jogadores[resp - 1].items():
        print('-'*20)
        print(f'{k}: {v}')
    
    print('.'*20)
    