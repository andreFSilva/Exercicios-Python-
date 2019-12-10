n = str(input('Digite uma frase: ')).strip().lower()

print('A letra A aparece {} vezes na frase.'.format(n.count('a')))
print('A primeira letra A aparece na posição {}. '.format(n.find('a')+1))
print('A ultima letra A apareceu na posição {}.'.format(n.rfind('a')+1))
