n = float(input('Digite um valor: '))
print(n)

n2 = str(input('Digite algo:'))

print(n2.isalpha()) # é letra
print(n2.isnumeric())# é número
print(n2.isalnum())# é letra e número
print(n2.isupper())# apenas letra maiúscula

n3 = bool(input('Digite outro valor: '))
print(n3)