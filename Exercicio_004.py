algo = (input('Digite algo: '))
aux = algo
print(' O tipo primitivo desse valor é {}'.format(type(algo)))
print('É um número? {}'.format(aux.isnumeric()))
print('Só tem espaço ? {}'.format(aux.isspace()))
print('É alfabético ? {}'.format(aux.isalpha()))
print('É alfanúmerico ? {}'.format(aux.isalnum()))
print('Esta em maiúscula ? {}'.format(aux.isupper()))
print('Esta em minúscula ? {}'.format(aux.islower()))



