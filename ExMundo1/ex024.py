'''
Exercício 24: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
'''

##### Resolução #####

### Criação das variáveis ###

cidade = str(input('Em que cidade você nasceu? '))
cidade = cidade.lower()
cidade = cidade.split()

### Print do resultado ###

print('santo' in cidade[0])

'''
Outra resolução 

cidade = str(input('Em que cidade você nasceu? ')).strip()

### Print do resultado ###

print(cid[:5].lower == 'santo')
'''