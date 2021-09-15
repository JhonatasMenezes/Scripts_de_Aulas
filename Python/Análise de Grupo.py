somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = ''
totmul20 = 0

for p in range(1, 5):
    print(f'------- {p}ª PESSOA -------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')). strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmul20 += 1
    
mediaidade = somaidade / 4
print(f'A media de idade do grupo é de {mediaidade}.')
print(f'O homem mais velho tem {maioridade} anos e se chama {nomevelho}.')
print(f'Ao todo são {totmul20} mulheres com menos de 20 anos.')