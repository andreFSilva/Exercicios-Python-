x = float(input('Largura da parede: '))
y = float(input('Altura da parede: '))
litro = 2
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.3f}m².'.format(x, y, (x * y)))
print('Para pintar essa parede, você precisará de {:.4f}L de tinta. '.format((x * y) / litro))
