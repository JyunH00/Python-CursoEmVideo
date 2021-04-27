'''
Exerício 11: Faça um programa que leia a largura e a altura de uma parece em metros, calcule a sua área e a quantidade
 de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m^2.
'''

##### Resolução #####

### Criação das variáveis ###

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = largura * altura
qTinta = area / 2

### Print do resultado ###

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(qTinta))