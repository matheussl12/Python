print('**RADAR ELETRÔNICO**\n')

vel = int(input('Digite sua velocidade total: \n'))

if vel <= 80:
    print('Velocidade dentro do limite permitido, tenha uma boa viagem!')
else:
    # O valor da multa é de R$ 5,00/Km.
    multa = ( vel - 80) * 5
    print("Você foi multado!! \n O valor da multa é de R${:.2f}".format(multa))