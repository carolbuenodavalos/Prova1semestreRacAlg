n = int(input('numero:'))

if n % 2 == 0:

    print(n + 10)

else:

    if n % 3 + n % 7 == 0:
        print(n * 70)


    else:
        print(n)
