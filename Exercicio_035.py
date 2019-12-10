print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if (a < b + c) and (a < b + c) and (c < a + b):
    print('os segmentos acima \033[0;0;44mPODEM FORMAR\033[m um triângulo. ')
else:
    print('os segmentos acima \033[0;0;44mNÃO PODEM FORMAR\033[m um triângulo. ')

print('-=-' * 20)
if a != b and b != c and c != a:
    print('Esse é um triângulo ESCALENO')
elif a == b and a == b and b != c:
    print('Esse triângulo é ISÓSCELES')
elif a == b and b == c and c == a:
    print('Esse triângulo é EQUILÁTERO')