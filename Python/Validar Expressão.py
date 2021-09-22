exp = str(input('Digite uma expressão: '))
lista = list(exp)
cont1 = lista.count('(')
cont2 = lista.count(')')

if (cont1 + cont2) % 2 == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
    
    
