#entradasConstruir um algoritmo que leia dois números e efetue a adição. Caso o valor somado seja maior que 20,
# este deverá ser apresentado somando-se a ele mais 8; caso o valor somado seja menor ou igual a 20,  este deverá ser apresentado subtraindo-se 5

#entradas
Numero1= float(input('Digite o primeiro numero:'))
Numero2=float(input('Digite o segundo numero:'))

#soma
somaDosNumeros = Numero1 + Numero2

#resultados
if somaDosNumeros > 20:
  print(somaDosNumeros +8)

elif somaDosNumeros <= 20:
  print(somaDosNumeros - 5)