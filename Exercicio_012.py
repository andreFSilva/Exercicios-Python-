import math
num = float(input('Qual é o preço do produto ? R$: '))
desconto = num*5/100
print('O produto que custava R${}, na promoção com desconto de 5% vai custar: R${:.2f}'.format(num, (num - desconto)))

