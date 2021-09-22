import sys

aluno = dict()
classe = list()

print('+-'*20)
print('REGISTRO DE ALUNOS'.center(40))
print('+-'*20)

while True:
    aluno['nome'] = str(input('\nDigite o nome do aluno: '))
    aluno['media'] = float(input('Digite a média do aluno: '))
    
    if aluno['media'] > 4 and aluno['media'] < 6:
        aluno['situacao'] = 'Recuperação'
    elif aluno['media'] > 6:
        aluno['situacao'] = 'Aprovado'
    else:
        aluno['situacao'] = 'Reprovado'
    
    classe.append(aluno.copy())
    aluno.clear()
    
    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break
    elif resp == 'S':
        pass
    else:
        print('Informação inválida! Encerrando...')
        sys.exit()

print('+-'*20)        
print('Resultado Final'.center(40))
print('+-'*20)
for aluno in classe:
    print(f"Aluno: {aluno['nome'].rjust(10)}  Média: {aluno['media']:2.2f}  Situação: {aluno['situacao'].rjust(12)}")    
    