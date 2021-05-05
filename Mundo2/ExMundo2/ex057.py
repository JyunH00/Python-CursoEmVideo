'''
Exercício 57: Faça um programa que leia o sexo de uma pessoa, mas só aceita os valores 'M' ou 'F'. Caso esteja errado,
peça a digitação novamente até ter um valor correto.
'''

#### Resolução ####

print('-=-'*20)
print('Escreva o sexo de uma pessoa válida!')
print('-=-'*20)

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Dados inválidos, por pavor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))


'''
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0] -> pega a primeira letra
'''