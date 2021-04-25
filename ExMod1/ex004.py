algo = input('Digite algo: ')

tipoalgo = type(algo)

print('O tipo primitivo da sua variável é {}'.format(tipoalgo))

print('Sua variável é um número? {}'.format((algo.isnumeric())))
print('Sua variável é um alfabético? {}'.format((algo.isalpha())))
print('Sua variável é um alfanumérico? {}'.format((algo.isalnum())))
print('Está em letras maiúsculas? {}'.format((algo.isupper())))
print('Está em letras minúsculas? {}'.format((algo.islower())))
print('Está capitalizada? {}'.format((algo.istitle())))