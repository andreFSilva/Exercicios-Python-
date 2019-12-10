from random import randint
from time import sleep
print('-=-' * 30)
print('Vou penser em um número entre 0 a 5. Tenta adivinhar!')
print('-=-' * 30)

processando = randint(0, 5)
n = int(input('Em que número eu pensei ? '))
print('PROCESSANDO...')
sleep(3)
if n == processando:
    print('PARABÉNS! Você conseguiu me vencer.')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(processando, n))
