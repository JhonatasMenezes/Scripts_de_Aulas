from Módulos import moeda, util_programas

util_programas.mensagemComLinhas('ANÁLISE DE VALLOR')
preco = float(input('Digite o preço: '))
print(moeda.metade(preco, mensagem=True))
print(moeda.dobro(preco, mensagem=True))
print(moeda.aumentar(preco, 10, mensagem=True))
print(moeda.diminuir(preco, porcentagem=12, mensagem=True))
