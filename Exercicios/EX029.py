print('Você acabou de entrar na Marginal Pinheros! Nesta Rodovia a velocidade maxima e 90 Km/n !')
velo = float(input('Qual é a sua velociade neste momento? '))
if velo <=90:
    print('Muito bem obrigado por colaborar conosco, Tenha uma otima viagem')
else:
    multa = (velo-90)*7
    print('Você foi multado em R${:.2f}! Porfavor colabore conosco e dirija em segurança!'.format(multa))
