num = int(input('Digite um número inteiro: '))
print('''Escolha umas das opções abaixo para converter:
[ 1 ] CONVERSÂO PARA BINÁNARIO
[ 2 ] CONVERSÂO PARA OCTAL
[ 3 ] CONVERSÃO PARA HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}!'.format(num, bin(num)))
elif opcao == 2:
    print('{} convertido para OCTAL é  igual a {}!'.format(num, oct(num)))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}!'.format(num, hex(num)))
else:
    print('Opção invalida. Tente Novamente!')
