n1 = float(input('Qual sua primeira nota? '))
n2 = float(input('Qual sua segunda nota? '))
media = (n1 + n2) / 2
if media < 5.0:
    print('A media do aluno foi {:.1f} \n\33[1;31mREPROVADO\33[m '.format(media))
elif media > 7.0:
    print('A media do aluno foi {:.1f}  \n\33[1;32mAPROVADO\33[m'.format(media))
else:
    print('A media do aluno foi {:.1f}  \n\33[1;33mRECUPERAÇÂO\33[m'.format(media))

