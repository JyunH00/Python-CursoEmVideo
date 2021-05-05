'''
Exercício 49: Refaça o DESAFIO 009. Mostrando a tabuada de um número que o usuário escolher, só que agora
utilizando o laço FOR
'''

### Resolução ###

### Criação das variáveis ###

tNumero = int(input('Digite um número para ve sua tabuada: '))

### Laço ###

print('-'*12)
for c in range(1, 11): # Vai da 1 a 10
    print('{} * {:2} = {:2}'.format(tNumero, c, tNumero*c))
print('-'*12)