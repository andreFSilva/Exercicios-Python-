from datetime import date
ano = int(input('Que ano você analisar ? Digite zero para analisar o ano atual. '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0) and (ano % 400 == 0):
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('Esse ano {} não é BISSEXTO.'.format(ano))


