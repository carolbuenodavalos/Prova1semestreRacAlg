# Criar um algoritmo que a partir da idade e peso do paciente calcule a dosagem de determinado medicamento e imprima
# a receita informando quantas gotas do medicamento o paciente deve tomar por dose. Considere que o medicamento em
# questão possui 500 mg por ml, e que cada ml corresponde a 20 gotas. Adultos ou adolescentes desde 12 anos,
# inclusive, se tiverem peso igual ou acima de 60 quilos devem tomar 1000 mg; com peso abaixo de 60 quilos devem
# tomar 875 mg. Para crianças e adolescentes abaixo de 12 anos a dosagem é calculada pelo peso corpóreo conforme a
# tabela a seguir:

# Dosagem:
# 5 a 9kgs - 125mg
# 9.1 a 16kgs - 250mg
# 16.1 a 24kgs - 375mg
# 24.1 a 30kg - 500mg
# acima de 30kg - 750mg


# entrada de dados

idade = int(input('Digite a idade do paciente: '))

print('\n')

peso = float(input('Digite o peso do paciente: '))


# saida e somas:
# para descobrirmos o numero de gotas é necessario usar a seguinte formula " (dosagem recomenda * gotas por ML)/500mg (equivalente a 1ml)

print('\n', '--------------------------------------''\n')

if (idade >= 12):

    if (peso < 60):
        dosagem = (875 * 20) / 500
        print('Número de gotas indicado:', int(dosagem), '.')

    elif (peso > 60):
        dosagem = (1000 * 20) / 500
        print('Número de gotas indicado:', int(dosagem), '.')


elif (idade < 12):

    if (peso <= 9):
        dosagem = (125 * 20) / 500
        print('O Número de gotas indicado é:', int(dosagem), '.')

    elif peso <= 16:
        dosagem = (250 * 20) / 500
        print('O Número de gotas indicado é:', int(dosagem), '.')

    elif(peso <= 24):
        dosagem = (375 * 20) / 500
        print('O Número de gotas indicado é:', int(dosagem), '.')

    elif(peso <= 30):
        dosagem = (500 * 20) / 500
        print('O Número de gotas indicado é:', int(dosagem), '.')

    elif(peso > 30):
        dosagem = (750 * 20) / 500
        print('O Número de gotas indicado é:', int(dosagem), '.')

