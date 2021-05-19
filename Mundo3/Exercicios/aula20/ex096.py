'''
Exercício 96: Faça um programa que tema um função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
'''
# Resolução #

# Funções #

def area(a, b):
    areaAB = a * b
    print(f'A área de um terreno {a:.1f}x{b:.1f} é de {areaAB:.1f}m².')


#Programa principal

print('Controle de Terrenos')
print('-----------------------')

a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
area(a, b)