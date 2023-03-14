from random import randint
from time import sleep
pc = randint(0, 10)
print('-=-'*22)
print('Calma! estou pensando em um número de 0 a 10, Tente adivinhar!')
print('-=-'*22)
jogador = int(input('Em que número voce pensou de 0 a 10? ')) #jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == pc:
    print('Parabéns! Voce adivinhou o número em que eu estava pensando!')
else:
    print('HaHa, Eu Ganhei eu pensei no número {} é não no número {}'.format(pc, jogador))
