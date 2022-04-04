prod_1 = float(input('Valor 1° produto: '))
prod_2 = float(input('Valor 2° produto: '))
prod_3 = float(input('Valor 3° produto: '))

if prod_1 <= prod_2 and prod_1 <= prod_3:
    print('Compre o primeiro produto.')
elif prod_2 <= prod_3:
    print('Compre o segundo produto.')
else:
    print('Compre o terceiro produto')