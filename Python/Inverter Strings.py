string = str(input('Digite uma frase: ')).strip().upper()
palavras = string.split()
juntar = ''.join(palavras)
inverso = ''
invsimples = juntar[::-1]

for letra in range(len(juntar) -1, -1, -1):
    inverso += juntar[letra]
    
print(juntar, inverso)
print(invsimples)