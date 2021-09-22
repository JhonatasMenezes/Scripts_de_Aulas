trabalhador = {}

print('='*30)
print('CADASTRO DE TRABALHADORES'.center(30))
print('='*30)
trabalhador['Nome'] = str(input('Nome: '))
trabalhador['Nascimento'] = int(input('Ano nascimento: '))
trabalhador['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))

if trabalhador['CTPS'] == 0:
    pass
else:
    trabalhador['Ano Contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salário'] = float(input('Salário: '))
    
    tempoTrab = 2021 - trabalhador['Ano Contratação']
    trabalhador['Idade'] = 2021 - trabalhador['Nascimento']
    trabRestante = 35 - tempoTrab
    
    trabalhador['Aposenta com'] = trabalhador['idade'] + trabRestante

print('='*30)
print('Dados armazenados: ')
for k, v in trabalhador.items():
    print(f'{k}: {v}')
    
    
    