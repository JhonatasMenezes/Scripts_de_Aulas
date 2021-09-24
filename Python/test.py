def escrever(*args):
    lista = []
    for dado in args:
        lista.append(str(dado))
    string = ';'.join(lista)
    return string
    
nome = 'Jhonatas'
idade = 25
    
string = escrever(nome, idade)

print(string)
