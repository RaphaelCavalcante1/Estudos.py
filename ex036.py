valor = float(input('\33[1;32mQual é o valor da casa? R$ \33[m'))
salario = float(input('\33[1;34mQual é o seu salario? R$ \33[m'))
anos = int(input('\33[1;36mEm quantos anos você vai pagar? \33[m'))
prestacao = valor / (anos * 12)
minimo = salario * 30 / 100
print('Para comprar uma casa de {:.2f} R$ em {} anos\na prestação sera de {:.2f} R$'.format(valor, anos, prestacao))
if prestacao <= minimo:
    print('\33[1;32mPARABÉNS! O financiamento da sua casa foi aprovado!\33[m')
else:
    print('\33[1;31mFINANCIAMENTO RECUSADO!\33[m')