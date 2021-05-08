'''
Exercício 77: Crie um programa que tenha uma tupla com várias palavras (não usuar acentos). Depois disso, você
deve mostrar, parar cada palavra, quais são as suas vogais
'''

#### Resolução ####

#### Variáveis ####

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', ' praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')


#### Laço ####
for pos, i in enumerate(palavras):
    print(f'\nNa palavra {i.upper()} temos ', end = '')
    for c in range (0, len(palavras[pos])):
        if palavras[pos][c] == 'a':
            print('a', end = ' ')
        elif palavras[pos][c] == 'e':
            print('e', end = ' ')
        elif palavras[pos][c] == 'i':
            print('i', end = ' ')
        elif palavras[pos][c] == 'o':
            print('o', end = ' ')
        elif palavras[pos][c] == 'u':
            print('u', end = ' ')


'''
Maneira muito mais simples!

for p in palavras:
    print(f'\nNa palavra {p} temos ' end = '')
    for letra in p:
        if letra.lower() in 'aeiou':
        print(letra, end = '')
'''


