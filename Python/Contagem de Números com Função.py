import sys
import time

def tituloCont(comeco,fim, passo):
    tam = 28 + len(str(comeco) + str(fim) + str(passo))
    print('-'*tam)
    print(f'CONTANDO DE {comeco} até {fim} de {passo} em {passo}'.center(tam))
    print('-'*tam)

def contador(inicio,fim,passo):
    if inicio < fim and passo > 0:
        tituloCont(inicio, fim, passo)
        while inicio <= fim:
            print(inicio,end=' ')
            inicio += passo
            time.sleep(0.5)
        print('')
        return
    elif inicio < fim and passo <= 0:
        print('Contagem impossível! Passo = 1 por padrão:')
        passo = 1
        tituloCont(inicio, fim, passo)
        while inicio <= fim:
            print(inicio,end=' ')
            inicio += passo
            time.sleep(0.5)
        print('')
        return
    if fim < inicio and passo > 0:
        tituloCont(inicio,fim,passo)
        while fim <= inicio:
            print(inicio, end=' ')
            inicio -= passo
            time.sleep(0.5)
        print('')
        return
    elif fim < inicio and passo <= 0:
        passo = (passo - passo * 2)
        tituloCont(inicio, fim, passo)
        while fim <= inicio:
            print(inicio,end=' ')
            inicio -= passo
            time.sleep(0.5)
        print('')
        return


contador(1, 10, 1)
contador(10, 1, 1)
print('-'*32)

print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
final = int(input('Fim: '))
passo = int(input('Passo: '))

contador(ini,final,passo)