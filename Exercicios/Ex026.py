nm = str(input('Digite Uma frase :')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(nm.count('A')))
print('A letra A aparece a primeira vez na posição {}'.format(nm.find('A')+1))
print('A última letra A aparece na posição {}'.format(nm.rfind('A')+1))