din = float(input('quantos reais você tem na carteira? R$'))
print('com R$ {:.2f} você pode comprar US$ {:.2f}'.format(din, din / 5.22))
print('com R$ {:.2f} você pode comprar EUR {:.2f}'.format(din, din / 5.50))
print('com R$ {:.2f} você pode comprar VEF {:.2f}'.format(din, din / 0.45))