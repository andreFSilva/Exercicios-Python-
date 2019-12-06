from math import hypot
'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hi = (co **2 + ca**2)**(1/2)
print('A hipotenusa vai midir {:.2f}'.format(hi))'''


#Fazendo o calculo da hipotenusa com o função Math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)

print('A hipotenusa vai midir {:.2f}'.format(hi))
