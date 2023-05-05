velocidade = float(input('Digite a velocidade do carro em km/h: '))
multa = (velocidade-80) * 7
print('Processando...')
if velocidade <= 80:
    print('Você não foi multado, diriga com segurança!')
else:
    print('Você excedeu o limite de velocidade o valor da multa será {.:2f} R$'.format(multa))


