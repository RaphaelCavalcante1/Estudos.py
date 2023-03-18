num1 = int(input('Escolha um valor inteiro: '))
num2 = int(input('Escolha outro valor inteiro: '))
if num1 > num2:
    print('{} é maior que {}'.format(num1, num2))
elif num2 > num1:
    print('{} é maior que {}'.format(num2, num1))
else:
    print('Não exite valor maior, Os dois são iguais')
