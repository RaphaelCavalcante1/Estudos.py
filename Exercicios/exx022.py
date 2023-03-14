Nome = str(input('Digite o seu nome completo:')).strip()
print('Seu nome em letra maiúscula é {}'.format(Nome.upper()))
print('Seu nome em letra minúscula é {}'.format(Nome.lower()))

letras = len(Nome) - Nome.count(' ')

print('Seu nome ao todo tem {} letras'.format(letras))

nomesplitado = Nome.split()

print('Seu primeiro nome é {} e ele tem {} letras'.format(nomesplitado[0], len(nomesplitado[0])))
