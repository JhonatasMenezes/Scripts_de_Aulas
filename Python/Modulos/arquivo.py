from Modulos.utilidades import mensagemTopo

def arquivoExiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
        

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

    
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
         mensagemTopo('CONTEÚDO DO ARQUIVO')
         for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]} anos')
    finally:
        a.close()


def adicionarTexto(arquivo, *args):
    try:
        a = open(arquivo, 'at')
    except:
        print
    else:
        try:
            lista = []
            for dado in args:
                lista.append(str(dado))
            string = ';'.join(lista)
            a.write(f'{string}')
            a.write('\n')
        except:
            print('Houve um ERRO na escrita dos dados!')
        else:
            print('Novo registro adicionado com sucesso!')
            a.close()
            