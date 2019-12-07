from random import choice
pri = input('Primeiro aluno: ')
seg = input('Segundo aluno: ')
ter = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')

lista = [pri, seg, ter, quarto]

'''print('Primeiro aluno: {}'.format(lista.append(pri)))
print('Segundo aluno: {}'.format(lista.append(seg)))
print('Terceiro aluno: {}'.format(lista.append(ter)))
print('Quarto aluno: {}'.format(lista.append(quarto)))'''

print('O aluno escolhido foi: ', choice(lista))

