'''Faz uma tabuada'''


x = int(input('Digite um número para ver a sua tabuada. '))
i = 1
for i in range(i, 11):
    print('{} X {} = {}'.format(x, i, x * i))


