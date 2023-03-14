km = float(input('Quantos km tem sua viagem? '))
print('Você esta preste a iniciar uma viagem de {}Km'.format(km))
if km <= 200:
    cn = km * 0.50
    print('Sua viagem deu {}Km teve o valor total de R${:.2f}'.format(km, cn))
else:
    cn = km * 0.45
    print('Sua viagem de {}Km teve o valor total de R${:.2f}'.format(km, cn))

