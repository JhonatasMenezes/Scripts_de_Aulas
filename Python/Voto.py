def voto(num=int):
    """
    Função que informa se a pessoa não vota,
    se tem voto opcional ou voto obrigatório.
    :param num: ano de nascimento
    """
    
    final = ''
    idade = 2021 - num
    if idade >= 18:
        final = 'VOTO OBRIGATÓRIO'
    elif idade >= 66 or idade in (16,17):
        final = 'VOTO OPCIONAL'
    elif idade < 18:
        final = 'NÃO VOTA'
    print(f'Com {idade} anos: {final}.')


print('-'*30)
print('CONSULTA DE VOTO'.center(28))
print('-'*30)

idade = int(input('Em que ano você nasceu? '))
voto(idade)
