#Entrada
#contrua um algoritmo para determinar se o individuo esta com um peso favoravel
#essa situação é determinada atraves do IMC(Indice de Massa Corporea)
#que é definida como sendo a relação entre o peso(PESO) e o quadrado da altura(ALTURA) do individuo
#ou seja, IMC = PESO/ALTURA**2 e a situação seja dada pela tabela

#abaixo de 17 = muito abaixo do peso
#entre 17 e 18.49 = abaixo do peso
#entre 18.5 e 24.99 = peso normal
#entre 25 e 29.99 = acima do peso
#entre 30 e 34.99 = obesidade I
#entre 35 e 3.9.99 = obesidade II
#acima de 40 = obesidade III(morbida)

PESO = float(input('Digite seu peso em quilogramas: '))
ALTURA = float(input('Digite sua altura em metros: '))

#Processamento

IMC = PESO/(ALTURA**2)

#Saida
print('\n')

print(f'Seu peso é: {PESO}kg')
print(f'Sua altura é: {ALTURA}m')
print('\n')

if IMC<17:
    print(f'Seu IMC é : {IMC}, portanto você esta muito abaixo do peso')
elif IMC<=18.49:
    print(f'Seu IMC é : {IMC}, portanto você esta abaixo do peso')
elif IMC<=24.99:
    print(f'Seu IMC é : {IMC}, portanto você esta com peso normal')
elif IMC<=29.99:
    print(f'Seu IMC é : {IMC}, portanto você esta acima do peso')
elif IMC<=34.99:
    print(f'Seu IMC é : {IMC}, portanto você esta com obesidade I')
elif IMC<=39.99:
    print(f'Seu IMC é : {IMC}, portanto você esta com obesidade II')
else:
    print(f'Seu IMC é : {IMC}, portanto você esta com obesidade III(morbida)')