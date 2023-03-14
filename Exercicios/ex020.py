from random import shuffle
n1 = str(input('Primeiro Aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
lista = [n1, n2, n3]
shuffle(lista)
print('A ordem escolhida sera')
print(lista)
