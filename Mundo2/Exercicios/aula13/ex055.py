'''
Exercício 55: Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor lidos.
'''

### Resolução ###

print('-=-'*30)
print('Coloque o peso de 5 pessoas e direi qual a mais pesada e qual a mais leve!')
print('-=-'*30)

### Criação de Variáveis ###

maior = 0
menor = 100000000
for peso in range(1,6):
    pesoPessoa = float(input('Digite o peso da {}º pessoa: '.format(peso)))
    if pesoPessoa > maior:
        maior = pesoPessoa
    elif pesoPessoa < menor:
        menor = pesoPessoa

print('O maior peso lido foi {:.1f}kg'.format(maior))
print('O menor peso lido foi {:.1f}kg'.format(menor))

'''
Resolução melhor: 

maior = 0
menor = 0
for peso in range(1,6):
    pesoPessoa = float(input('Digite o peso da {}º pessoa: '.format(peso)))
    if peso == 1:
        maior = pesoPessoa
        menor = pesoPessoa
    else:
        if pesoPessoa => maior:
            maior = pesoPessoa
        elif pesoPessoa <= menor:
            menor = pesoPessoa        
'''