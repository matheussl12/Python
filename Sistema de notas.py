

print('***SISTEMA DE NOTAS ***\n')

np1 = float(input('Digite o valor de sua nota da NP1: \n'))
np2 = float(input('Digite o valor de sua nota da NP2: \n'))

media = (np1 + np2) / 2

if media < 7:
    print("Você esta de exame!")
    nexame = float(input('Digite a nota do exame: \n'))
    nexame = (np1 + np2 + nexame) / 3
    if nexame >= 5:
        print("Você foi aprovado pelo exame! \nSua nota final é {:.1f}".format(nexame))
    else:
        print("Você foi reprovado nesta disciplina.")
else:
    print("Você está aprovado! \n Sua média final é {:.1f} ".format(media))