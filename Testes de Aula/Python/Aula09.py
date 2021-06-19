frase = 'Curso em Video Python'
frase1 = '   Aprenda Python  '
#fatiamento de strings
print(frase[9])
print(frase[9:14], frase[9::3])
print(frase[3:21:2])
print(frase[:5], frase[15:])

#análise de strings
print(len(frase))
print(frase.count('o', 0, 21))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

#transformação
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase1.strip(),'|',frase1.lstrip(),'|',frase1.rstrip())

#divisão
print(frase.split())

#junção
print('-'.join(frase))