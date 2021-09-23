def area(larg, comp):
    return larg * comp
    
def title(msg):
    tam = len(msg) + 4
    print('-' * (tam))
    print(str(msg).center(tam))
    print('-' * (tam))

title('CALCULAR ÁREA (retângulo)')

largura = float(input('Digite a largura do terreno em M: '))
comprimento = float(input('Digite o comprimento em M: '))

print(f"Para esse comprimento e largura, a área é {area(largura,comprimento):.2f} m2")