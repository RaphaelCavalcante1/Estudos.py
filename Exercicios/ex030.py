from random import randint
from time import sleep
num = randint(0,9999)
num1 = num % 2
print('-=-'*28)
print('Calma, Estou escolhendo um número de 0 a 9999 e te direi se ele é par ou ímpar!')
print('-=-'*28)
sleep(2)
if num1 == 0:
    print('Bom, Pensei no número {} é ele e par'.format(num))
else:
    print('Bom, Eu escolhi o número {} é ele e ímpar'.format(num))


