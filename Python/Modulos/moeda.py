import os 

def dobro(num, mensagem=False):
    """
    Dobra um número.
    :param num: numero inteiro ou real
    :param mensagem: se True, retorna uma mensagem para ser exibida no terminal
    """
    if mensagem == True:
        result = num*2
        retorno = f'O dobro de {num:.2f} é {result:.2f}'
        return retorno
    else:
        return num*2
    
def metade(num, mensagem=False):
    """
    Mostra a metade de um valor.
    :param num: número inteiro ou real
    :param mensagem: se True, retorna uma mensagem para ser exibida no terminal
    """
    if mensagem == True:
        result = num/2
        retorno = f'A metade de {num:.2f} é {result:.2f}'
        return retorno
    else:
        return num/2
    
def aumentar(num, porcentagem=100, mensagem=False):
    """
    Retorna a porcentagem de um valor
    :param num: um número inteiro ou real 
    :param porcentagem: porcentagem do valor total a ser retornada
    :param mensagem: se True, retorna uma mensagem para ser exibida no terminal
    """
    if mensagem == True:
        result = num + (num/100) * porcentagem
        retorno = f'Aumentando {porcentagem}%, temos {result:.2f}'
        return retorno
    else:
        return num + (num/100) * porcentagem
    
def diminuir(num, porcentagem=100, mensagem=False):
    """
    Retorna o valor com uma porcentagem a menos
    :param num: um número inteiro ou real 
    :param porcentagem: porcentagem a ser tirada do valor total
    :param mensagem: se True, retorna uma mensagem para ser exibida no terminal
    """
    if mensagem == True:
        result = num - ((num/100)*porcentagem)
        retorno = f'Diminuindo {porcentagem}%, temos {result:.2f}'
        return retorno
    else: 
        return num - ((num/100)*porcentagem)
    
def resumo(num, porcentagemMais, porcentagemMenos, moeda=' '):
    """
    Resume de forma completa todas as funcionalidades
    prsentes neste módulo, mostrando, de maneira
    formatada, todos os valores resultantes.
    
    :param num: um valor a ser analisado
    :param porcentagemMais: porcentagem a ser acrescentada na funcao aumentar()
    :param porcentagemMenos: porcentagem a ser subtraída na funcao diminuir()
    """
    dob = dobro(num)
    met = metade(num)
    aum = aumentar(num, porcentagemMais)
    dim = diminuir(num, porcentagemMenos)
    
    os.system('cls')
    print('-'*30)
    print('ANÁLISE DO VALOR'.center(30))
    print('-'*30)
    print('Valor analisado:'.ljust(20),f'{moeda} {num:.2f}')
    print('Valor dobrado:'.ljust(20),f'{moeda} {dob:.2f}')
    print('Valor pela metade:'.ljust(20),f'{moeda} {met:.2f}')
    print(f'Valor + {porcentagemMais}% :'.ljust(20),f'{moeda} {aum:.2f}')
    print(f'Valor - {porcentagemMenos}%:'.ljust(20),f'{moeda} {dim:.2f}')
    print('-'*30)
    print('FIM DA EXECUÇÃO'.center(30))
    print('-'*30)
    
    