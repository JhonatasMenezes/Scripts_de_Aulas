def mensagemComLinhas(mensagem):
    mensagem = str(mensagem)
    tam = len(mensagem) + 4
    print('-'*tam)
    print(mensagem.center(tam))
    print('-'*tam)
    
def linhaUnica(tamanho):
    print('-'*tamanho)
    