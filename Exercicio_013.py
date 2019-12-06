sal = float(input('Qual é o salário funcionário? R$: '))
aumento = (sal*15/100) + sal
print('Um funcionário que ganhava {:.2f}, com 15% de aumento, passa a receber R$:{:.2f}'.format(sal, aumento))