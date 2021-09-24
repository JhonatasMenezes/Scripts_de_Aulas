import os

def mensagemComLinhas(mensagem, inicio=False):
    if inicio == True:
        os.system('cls')
    mensagem = str(mensagem)
    tam = len(mensagem) + 4
    print('-'*tam)
    print(mensagem.center(tam))
    print('-'*tam)
    
    
def linhaUnica(tamanho):
    print('-'*tamanho)
    
    
def validaValorInteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
        except KeyboardInterrupt:
            print('O usuário escolheu sair!')
            return 0
        except ValueError:
            print('\033[0;31mERRO: por favor, digite um valor inteiro válido!\033[m')
        else:
            return valor
        finally:
            pass


def validaValorReal(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
        except KeyboardInterrupt:
            print('O usuário escolheu sair!')
            return 0
        except ValueError:
            print('\033[0;31mERRO: por favor, digite um valor real válido!\033[m')
        else:
            return valor
        finally:
            pass
        

def textoCor(texto,cor,end1='\n'):
    print(f'\033[0;{cor}m{texto}\033[m',end=end1)
