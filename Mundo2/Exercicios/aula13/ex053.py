'''
Exercício 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

Ex:
Apos a sopa
A sacada da casa
A torre da derrota
O lobo ama o bolo
Anotaram a data da maratona
'''

### Resolução ###

print('-=-'*30)
print('Escreva uma frase e direi se ela é um palíndromo!')
print('-=-'*30)


### Criação de Variáveis ###

frase = str(input('Escreva uma frase! (Evite acentos): ')).upper() # Usuário escreve a frase e o programa deixa tudo em minúscula

# Junta a frase e tirando os espaços para comparação
fraseNova = frase.split()
fraseNova = ''.join(fraseNova)

# Variável de para o laço
tamanhoString = len(fraseNova) - 1

# Compara o número de letras iguais
comparador = 0

for fimIn in range(tamanhoString, -1, -1):
    if fraseNova[fimIn] == fraseNova[comparador]:
       comparador +=1
    else:
        break

# Aprendi no vídeo!
inverso = fraseNova[::-1] # GENIAL
'''
inverso = ''
for fimIn in range(tamanhoString, -1, -1):
     inverso += fraseNova[fimIn]
'''

# Prints
if comparador == len(fraseNova):
    print(' A frase {} ao contrário é {}, sua frase é um palíndromo!'.format(fraseNova, inverso))
else:
    print('A frase {} ao contrário é {}, sua frase não é um palíndromo!'.format(fraseNova, inverso))




'''
Poderia comparar inverso com fraseNova!
'''