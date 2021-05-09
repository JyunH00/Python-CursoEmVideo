'''
Exercício 83: Crie um programa onde o usuário digita uma expressão qualquer que use parênteses. Seu aplicativo deverá
analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

# Resolução #

# Variáveis #

parenLista = []

exp = str(input('Digite a expressão: '))

for i in range(0, len(exp)):
    if exp[i] in '(':
        parenLista.append(exp[i])
    elif exp[i] in ')':
        parenLista.append(exp[i])

if parenLista.count('(') == parenLista.count(')'):
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

'''
Lógica do professor um pouco diferente! Veja o vídeo!
'''
