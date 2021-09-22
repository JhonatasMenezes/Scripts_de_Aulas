matriz = list()

for i in range(3):
    for c in range(3):
        matriz += [int(input(f'Digite um valor para [{i}, {c}]: '))]
print('')
print('-='*20)
print(f'''
[{matriz[0]}][{matriz[1]}][{matriz[2]}]
[{matriz[3]}][{matriz[4]}][{matriz[5]}]
[{matriz[6]}][{matriz[7]}][{matriz[8]}]
''')