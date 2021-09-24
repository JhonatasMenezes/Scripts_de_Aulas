def dobro(num):
    """
    Dobra um número.
    :param num: numero inteiro ou real
    """
    return num*2
    
def metade(num):
    """
    Mostra a metade de um valor.
    :param num: número inteiro ou real
    """
    return num/2
    
def aumentar(num, porcentagem=100):
    """
    Retorna a porcentagem de um valor
    :param num: um número inteiro ou real 
    :param porcentagem: porcentagem do valor total a ser retornada
    """
    return (num/100) * porcentagem
    
def diminuir(num, porcentagem=100):
    """
    Retorna o valor com uma porcentagem a menos
    :param num: um número inteiro ou real 
    :param porcentagem: porcentagem a ser tirada do valor total
    """
    return num - ((num/100)*porcentagem)
    