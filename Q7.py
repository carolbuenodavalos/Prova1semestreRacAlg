A = float(input('Digite o valor do coeficiente A: '))
B = float(input('Digite o valor do coeficiente B: '))
C = float(input('Digite o valor do coeficiente C: '))

#Processamento
#y = A*(x**2) + B*x + C
#rdelta é a raiz de delta
#x1 é a primeira raiz possivel da equação e x2 a segunda
#quando o delta é maior que 0 tem 2 raizes, quando é igual a 0 tem uma e quando é menor que 0 não ha raizes reais
delta = B**2-4*A*C
rdelta = delta**(1/2)
x1 = (-B+rdelta)/(2*A)
x2 = (-B-rdelta)/(2*A)

#Saida
print('\n')
if delta > 0:
    print(f'a equação apresenta duas raizes reais que são x1={x1} e x2={x2}')
elif delta == 0:
    print(f'a equação possui uma raiz real que é x={x1}')
else:
    print('a equação não possui raizes reais')