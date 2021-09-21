# Tuplas
# tuplas são imutáveis
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche[0])

print(lanche[-1])

print(sorted(lanche))

# Fatiamento: [de:até:passo]
print(lanche[::-1])

print(lanche[:2])

# iterar sobre tupla
for c in lanche:
    print(f'Escrevendo {c}')
    
# se precisar mostrar posição
for cont in range(0, len(lanche)):
    print(f'Escrevendo {lanche[cont]}, pos {cont}')

for p, c in enumerate(lanche):
    print(f'Escrevendo {c}, pos {p}')

# concatenando tuplas
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a

print(c)
print(d)
print(c.count(5))
print(d.index(8))
print(d.index(5, 1))

pessoa = ('Jhonatas', 24, 'M', 77.8)
print(pessoa)
del(pessoa)
print(pessoa)




# Listas
listas = []

# Dicionários
dicionarios = {}

