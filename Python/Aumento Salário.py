sal = float(input('Valor do salário: '))
nSal = float

if sal >= 1250:
    nSal = sal + (sal * 0.10)
else:
    nSal = sal + (sal * 0.15)
    
print(f'Novo salário: R${nSal:.2f}')