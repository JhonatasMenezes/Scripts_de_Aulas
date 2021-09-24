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
    