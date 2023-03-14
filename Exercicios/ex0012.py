prc = float(input('Qual valor do produto? R$'))
multi = prc * 5
div = multi / 100
print('Se o valor do produto e {:.2f} com 5% de desconto ele ficara {:.2f}'.format(prc, prc-div))