import time
import sys
from Modulos.utilidades import *
from Modulos.arquivo import *
from Modulos.dados import *

opcoesMenu = [['Ver pessoas cadastradas','Adicionar uma nova pessoa','Sair do sistema'],['Voltar ao menu principal', 'Sair do sistema']] 



arq = 'arquivo_nomes.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
    time.sleep(3)
    
while True:
    os.system('cls')
    # Criar um menu principal com opção ao usuário ja com tratamento de erros e problemas
    escolha = menuPrincipal(opcoesMenu[0])    
    # estrutura condicional para a opção do usuário
    if escolha == 1:
        # listar conteúdo de um arquivo
        os.system('cls')
        lerArquivo(arq)
        time.sleep(2)
        
        a = menuSimples(opcoesMenu[1])
        if a == 1:
            pass
        elif a == 2:
            sys.exit()
    elif escolha == 2:
        # adicionar nova pessoa ao arquivo
        mensagemTopo('NOVO CADASTRO',inicio=True)
        nome = str(input('Nome: '))
        idade = validaValorInteiro('Idade: ')
        adicionarTexto(arq,nome,idade)
        
        a = menuSimples(opcoesMenu[1])
        if a == 1:
            pass
        elif a == 2:
            sys.exit()
    elif escolha == 3:
        linhaUnica(35)
        textoCor('Você escolheu sair. Até Mais!')
        time.sleep(3)
        sys.exit()
    # mostrar pessoas do arquivo
    # inserir novas pessoas
    # sair do sistema
