import sys, time


def maior(*num):
    """
    Mostra o maior valor dentro de uma lista ou de 
    uma sequência de valores colocados em parametros.
    :param: *num: aceita uma lista ou vários valores
    """
    maior = 0
    if len(num) < 2:
        maior = num[0][0]
        num = num[0]
        
    for n in num:
        if n >= maior:
            maior = n
    return maior
    
maiorVal = []

print('-'*30)
print('FUNÇÃO MAIOR'.center(30))
print('-'*30)
qtdVal = int(input('Quantos valores quer analizar? [999 para indefinido] '))

if qtdVal == 999:
    while True:
        maiorVal.append(int(input('Digite um valor: ')))
        
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp == 'N':
            break
        elif resp == 'S':
            pass
        else:
            print('Valor inválido! Encerrando...')
            sys.exit()
else:
    for i in range(0, qtdVal):
        maiorVal.append(int(input('Digite um valor: ')))

maiorFinal = maior(maiorVal)

print('-'*30)
print('RESULTADO FINAL'.center(30))
print('-'*30)
print(f'Dos valores {maiorVal} o maior é {maiorFinal}')
