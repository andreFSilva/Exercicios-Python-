sal = float(input('Informe o salário do funcionário R$: '))
# 10 ou 15%
if sal > 1250:
    print('Quem ganhava \033[0;30;41m{}\033[m passa a ganhar R${:.2f}'.format(sal, sal + (sal / 100 * 10)))
elif sal <= 1250:
    print('Quem ganhava \033[0;30;42m{}\033[m passa a ganhar R${:.2f}'.format(sal, sal + (sal / 100 * 15)))

