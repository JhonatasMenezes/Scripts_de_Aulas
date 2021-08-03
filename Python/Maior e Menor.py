num1 = int(input('Digite o 1° número: '))
num2 = int(input('Digite o 2° número: '))
num3 = int(input('Digite o 3° número: '))
maior = num1
menor = num1

if num1 > maior:
    maior = num1
elif num1 < menor:
    menor = num1

if num2 > maior:
    maior = num2
elif num2 < menor:
    menor = num2

if num3 > maior:
    maior = num3
elif num3 < menor:
    menor = num3
    
print(f'O menor número é {menor} e o maior é {maior}.')
