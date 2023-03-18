from datetime import date
print('\33[32mA\33[m\33[33mL\33[m\33[32mI\33[m\33[33mS\33[m\33[32mT\33[m\33[33mA\33[m\33[32mM\33[m\33[33mE\33[m\33[32mN\33[m\33[33mT\33[m\33[32mO\33[m')
ano = int(input('Qual o ano de seu nascimento? '))
sub = date.today().year - ano
print('QUEM NASCEU EM {} TEM {} ANOS EM {}.'.format(ano, sub, date.today().year))
if sub > 18:
    t = sub - 18
    print('VOCÊ JA PASSOU DA IDADE DE SE ALISTAR NA JUNTA MILITAR')
    print('VOCÊ DEVERIA TER SE ALISTADO A {} ANOS'.format(t))
elif sub == 18:
    print('VOCÊ DEVE SE ALISTAR NA JUNTA MILITAR IMEDIATAMENTE POIS JA FEZ {} ANOS'.format(sub))
elif sub < 18:
    anodl = 18 - sub
    print('INFELIZMENTE VOCÊ ESTA MUITO NOVO PARA SE ALISTAR A JUNTA MILITAR')
    print('SUA DATA DE ALISTAMENTO SERA NO ANO DE {}'.format(date.today().year + anodl))
