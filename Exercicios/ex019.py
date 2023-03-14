from random import choice

Prim = str(input('Nome do primeiro aluno:'))
seg = str(input('Nome do segundo aluno:'))
ter = str(input('Nome do terceiro aluno:'))
quar = str(input('Nome do quarto aluno:'))
lista = [Prim, seg, ter, quar]
print('O aluno escolhido e {}'.format(choice(lista)))