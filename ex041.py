from datetime import date
nasc = int(input('Ano de nascimento? '))
sub = date.today().year - nasc
if sub <= 9:
    print('O atleta tem {} ele é um atleta mirim'.format(sub))
elif sub <= 14:
    print('O atleta tem {} ele é um atleta infantil'.format(sub))
elif sub <= 19:
    print('O atleta tem {} ele é um atleta junior'.format(sub))
elif sub <= 25:
    print('O atleta tem {} ele é um atleta sénior'.format(sub))
elif sub > 25:
    print('O atleta tem {} ele é um atleta master'.format(sub))

