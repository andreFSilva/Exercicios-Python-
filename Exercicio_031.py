n = float(input('Digite a distância da sua viagem em KM: '))
print('Você esta preste a começar uma viagem de {}Km.'.format(n))
if n < 200:
    print('E o preço da sua passagem será de R${}'.format(n * 0.50))
else:
    print('E o preço da sua passagem será de R${}'.format(n * 0.45))

