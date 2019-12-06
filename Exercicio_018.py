import math

angulo = float(input('Digite o ângulo que você deseja. '))

seno = math.sin(math.radians(angulo))
print('O ângulo de {:.0f}° tem o seno de {:.2f}°'.format(angulo, seno))

cosseno = math.cos(math.radians(angulo))
print('O ângulo de {:.0f}° tem o cosseno de {:.2f}°'.format(angulo, cosseno))

tan = math.tan(math.radians(angulo))
print('O ângulo de {:.0f}° tem a tangente de {:.2f}°'.format(angulo, tan))
