n = 0

while True:
    print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[digite qualquer valor negativo para sair]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        print('VOCÊ ESCOLHEU SAIR! TCHAU!')
        break
    for i in range(1, 11):
        print(f'{n} x {i} = {(n*i)}')
