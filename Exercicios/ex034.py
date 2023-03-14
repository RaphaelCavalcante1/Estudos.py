Salario = float(input('Qual é o salario do Funcionário? R$'))
if Salario <=1250:
    nsalario = Salario + (Salario * 15 / 100)
else:
    nsalario = Salario + (Salario * 10 / 100)
print('O novo dalario do funcionario e de R$ {:.2f}'.format(nsalario))