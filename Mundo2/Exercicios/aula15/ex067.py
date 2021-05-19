'''
Exercício 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo
usuário. O programa será interrompido quando o número solicitado for negativo.
'''

#### Resolução ###

print('-=-'*20)
print('Tabuada v3.0')
print('-=-'*20)

### Variáveis ###

numInt = 0
### Laço While ###

while True:
    print('-' * 50)
    numInt = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 50)
    if numInt < 0:
        break
    for contador in range (1, 11):
        resultado = numInt * contador
        print(f'{numInt} X {contador:2} = {resultado:2}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')