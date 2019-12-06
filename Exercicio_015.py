n = int(input("Quantos dias alugado ? "))
x = float(input('Quantos km rodados ? '))

dia = 60
km = 0.15
total = (dia * n) + (x * km)
print('Total a pagar é de R$: {:.2f}'.format(total))
