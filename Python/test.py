from Modulos import moeda, util_programas

util_programas.mensagemComLinhas('PROGRAMA DE ANÁLISE', inicio=True)
valor = float(input('Digite um valor: '))
porcMais = float(input(r'Quantos % você deseja calcular a mais: '))
porcMenos = float(input('E quantos % voce deseja calcular a menos: '))

moeda.resumo(valor, porcMais, porcMenos, 'U$')

