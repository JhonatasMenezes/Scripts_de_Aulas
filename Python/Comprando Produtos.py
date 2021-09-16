total = 0
acimaMil = 0
baratoVal = 0
maisBarato = ''
qtdProd = 0

print('-'*45)
print('            MERCADAO DO POVO')
print('-'*45)
while True:
    produto = str(input('Nome do Produto: '))
    valor = float(input('Preço: R$ '))
    
    total += valor
    qtdProd += 1
    if qtdProd == 1:
        baratoVal = valor
        
    if valor >= 1000:
        acimaMil += 1
    if valor < baratoVal:
        baratoVal = valor
        maisBarato = produto
    perg = str(input('Continuar Compra? [S/N] ')).upper()
    if perg == 'N':
        print(f'''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
           Informações da compra
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Valor total gasto: {total}
Quantidade de produtos acima de R$ 1000: {acimaMil}
Produto mais barato: {maisBarato}
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
               VOLTE SEMPRE!!!
        ''')  
        break      
    else:
        True