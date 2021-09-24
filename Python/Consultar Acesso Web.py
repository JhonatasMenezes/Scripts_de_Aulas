import requests

try:
    response = requests.get(str(input('Digite o site para a verificação de status (http:// + site): ')))
    print('\033[0;32mTudo certo! O site está no ar!\033[m')
except response:
    print('\033[0;31mERRO: Não consegui acessar o site.\033[m')
