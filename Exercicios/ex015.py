d = int(input('Quantos dias alugados?'))
k = float(input('quantos km rodados?'))
g = d * 60
u = k * 0.15
t = g + u
print('se o carro foi alugado por {} dias e rodou {} km o valor pelo aluguel dele ficou {:.2f}'.format(d, k, t))