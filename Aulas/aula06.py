#Especificando o tipo da variável com int()#
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1 + n2

#Uso de .format em print#
#Uso de números dentro das chaves é opcional#

print('A soma entre {0} e {1} é {2}'.format(n1, n2, s) )