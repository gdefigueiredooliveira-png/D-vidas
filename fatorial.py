def calcular_fatorial():
    while True:
        try:
            numero = int(input('Digite um número: '))
            break
        except:
            print("+---------------------------------------------+")
            print("|                                             |")
            print("|             DIGITE APENAS NÚMEROS           |")
            print("|                                             |")
            print("+---------------------------------------------+")

    fatorial = 1
    print(f'\nCálculo de {numero}:')

    for i in range(numero, 0, -1):
        print(i, end="")
        fatorial *= i

        if i > 1:
            print(" X ", end="")
        else:
            print(" = ", end="")

    print(fatorial, "\n")

calcular_fatorial()