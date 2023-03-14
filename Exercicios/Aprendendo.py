nome = str(input('Qual é o seu nome? ')).strip().capitalize()
if nome == 'Raphael':
    print('{}, Que nome lindo você tem, Tenha um Bom dia!'.format(nome))
else:
    print('Olá {}, Tenha um Bom Dia!'.format(nome))