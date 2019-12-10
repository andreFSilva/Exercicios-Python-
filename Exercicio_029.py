vel = int(input('Qual e velocidade atual do carro ? '))
mult = 7

if vel < 80:
    print('Tenha um bom dia. Direija com segurança.')
else:
    print('MULTADO! Você excedeu o limeite permitido que é de 80Km/h')
    print('Voce deve pagar uma multa de R${}!'.format(mult * (vel - 80)))
    print('Tenha um bom dia. Direija com segurança.')