# Escreva um algoritmo que leia um número e informe se ele é divisível por 3 e por 7, de forma concomitante

# entrada
numerodeentrada = int(input('Digite um numero: '))

# divisao concomitante para descobrirmos se é divisivel por ambos, devemos verificar se o restante da divisão pelo
# dividendo é igual a 0 (ZERO)
restodivisao = (numerodeentrada % 5) + (numerodeentrada % 12)

# saída
print('\n')

if restodivisao == 0:
    print('O número', numerodeentrada, 'é divisível por 5 e 12.')

elif restodivisao != 0:
    print('O número', numerodeentrada, 'não é divisivel por 5 e 12.')
