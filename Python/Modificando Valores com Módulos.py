from Modulos import moeda, utilidades

utilidades.mensagemComLinhas('PROGRAMA DE ANÁLISE', inicio=True)
valor = utilidades.validaValorNumerico('Digite um valor: ')
porcMais = float(input(r'Quantos % você deseja calcular a mais: '))
porcMenos = float(input('E quantos % voce deseja calcular a menos: '))

moeda.resumo(valor, porcMais, porcMenos, 'U$')
