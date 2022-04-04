#Entrada
#Faça um programa que receba 3 valores a, b e c que representam os lados de um trianulo, e retorne a sua area
#Para calcular a area use a formula de herao, fornecida abaixo, onde o p é o semi-perimetro

#A = raiz{p(p-a)(p-b)(p-c)
#p = (a+b+c)/2



a = float(input('Digite o valor do primeiro lado do triangulo: '))
b = float(input('Digite o valor do segundo lado do triangulo: '))
c = float(input('Digite o valor do terceiro lado do triangulo: '))

#Processamento

p = (a+b+c)/2
A = (p*(p-a)*(p-b)*(p-c)) ** (1/2)

#Saida

print('\n')

print(f'Os lados do seu triangulo tem os valores: {a},{b} e {c}')
print(f'O semiperimetro do seu triangulo é: {p}')
print(f'Portanto a area do seu triangulo é: {A}')