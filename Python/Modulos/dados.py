def validaValorInteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
        except KeyboardInterrupt:
            print('O usuário escolheu sair!')
            return 0
        except ValueError:
            print('\033[0;31mERRO: por favor, digite um valor inteiro válido!\033[m')
        else:
            return valor
        finally:
            pass


def validaValorReal(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
        except KeyboardInterrupt:
            print('O usuário escolheu sair!')
            return 0
        except ValueError:
            print('\033[0;31mERRO: por favor, digite um valor real válido!\033[m')
        else:
            return valor
        finally:
            pass