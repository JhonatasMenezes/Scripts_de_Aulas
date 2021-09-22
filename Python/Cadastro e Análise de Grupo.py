import os

geral = []
aux = {}
acimaMedia = []
mulheres = []
mediaIdade = 0
cont = 0

os.system('cls')
print('CADASTRO E ANÁLISE DE GRUPO'.center(30))
print('-'*30)
qtdPessoas = int(input('Deseja cadastrar quantas pessoas? '))

for i in range(1, qtdPessoas+1):
    os.system('cls')
    print(f'Cadastro da {i}ª pessoa'.center(30))
    print('='*30)
    aux['Nome'] = str(input('Digite o nome: '))
    aux['Sexo'] = str(input('Digite o sexo [M/F] : ')).upper()
    aux['Idade'] = int(input('Digite a idade: '))
    
    geral.append(aux.copy())
    aux.clear()
    os.system('cls')
    
qtdCadastro = len(geral)

for i in geral:
    cont += i['Idade']

mediaIdade = float(cont / qtdPessoas)
    
for p in geral:
    if p['Sexo'] == 'F':
        mulheres.append(p)
    if p['Idade'] > mediaIdade:
        acimaMedia.append(p)

print('-'*30)        
print('RESULTADO FINAL'.center(30))
print('-'*30)
print('As pessoas cadastradas foram: ')
for p in range(0, len(geral)):
    print(f"{p+1}: {geral[p]['Nome']}")
print('-'*30)
print(f'- A média de idade do grupo é {mediaIdade:.2f}')
print('- As mulheres são: ', end='')
for p in mulheres:
    print(p['Nome'], end='')
    if p != mulheres[-1]:
        print(', ',end='')
    else:    
        print('.')
print('- Pessoas com idade acima da média: ')
for p in acimaMedia:
    print(p['Nome'],f"com {p['Idade']} anos.",)

    
    