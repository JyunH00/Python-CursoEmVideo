'''
Exercício 80: Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os numa lista,
já na posição correta de inserção (sem usar o sort())

No final mostre a lista ordenada na lista
'''

#### Resolução ####

#### Variáveis ####

numLista = []

#### Laço #### (Mudei o código)
for posL in range(0, 5):
    numI = int(input('Digite um valor: '))
    if posL == 0 or numI >= numLista[-1]:
        numLista.append(numI)
        print('Adicionado ao final da lista...')
    elif numI <= numLista[0]:
            numLista.insert(0,numI)
            print('Adicionado na posição 0 da lista...')
    elif posL == 2:
        if numI <= max(numLista):
            numLista.insert(1, numI)
            print('Adicionado na posição 1 da lista...')
    elif posL == 3:
        if numI <= numLista[1]:
            numLista.insert(1, numI)
            print('Adicionado na posição 1 da lista...')
        elif numI <= numLista[2]:
            numLista.insert(2, numI)
            print('Adicionado na posição 2 da lista...')
    elif posL == 4:
        if numI <= numLista[1]:
            numLista.insert(1, numI)
            print('Adicionado na posição 1 da lista...')
        elif numI <= numLista[3]:
            numLista.insert(2, numI)
            print('Adicionado na posição 2 da lista...')
print(numLista)

'''
Resolução do vídeo muito mais simples!

lista = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]
                lista.insert(pos, n)
                break
            pos += 1
'''