from datetime import date
dt = int(input('Qual é o ano que você quer analisar? Digite 0 para analisar 0 ano atual: '))
if dt == 0:
    dt = date.today().year
if dt % 4 == 0 and dt %  100 != 0 or dt % 400 == 0:
    print('O ano de {} é BISSEXTO'.format(dt))
else:
    print('O ano de {} NÂO É BISSEXTO'.format(dt))