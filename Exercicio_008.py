"""Escreva um programa que leia um valor em metros e o exiba convertido em milímetros"""

metros = int(input("Por favor informe uma quantidade em metro: "))
m = metros
km = metros / 1000
h = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
milimetros= (metros*1000)

print('A medida de {:.1f}m corresponde a'.format(m))
print('{}km'.format(km))
print('{}hm'.format(h))
print('{}dam'.format(dam))
print('{}dm'.format(dm))
print('{}cm'.format(cm))



print('{}mm'.format(milimetros))