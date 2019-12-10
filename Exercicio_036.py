casa = float(input('Valor da casa R$ '))
sal = float(input('Salário do comprador R$ '))
anos = int(input('Quantos anos de financiamento ? '))
emprestimo = casa / (anos * 12)

print('Para pagar a casa de R${:.2f} em {:.2f} anos a prestação será de R${:.2f}'.format(casa, anos, casa / (anos * 12)))
if sal / 100 * 30 < emprestimo:
    print('Empréstimo NEGADO!')
else:
    print('O empréstimo pode ser CONCEDIDO. ')

