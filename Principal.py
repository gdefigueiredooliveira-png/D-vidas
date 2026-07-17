from fatorial import calcular_fatorial
while True:
    print('Olá Coleguinha Tudo bem?')
    while True:
        try:
            print("+---------------------------------------------+")
            print("|                                             |")
            print("|  1- Funçao da Torre de Hanói do Cerbino     |")
            print("|  2- Função de Fatorial do Gabriel           |")
            print('|  3- Sair                                    |')
            print("|                                             |")
            print("+---------------------------------------------+")
            opcao=int(input('Escolha uma Dessas Opções: '))
            break
        except ValueError:
            print("+---------------------------------------------+")
            print("|                                             |")
            print("|             DIGITE APENAS NÚMEROS           |")
            print("|                                             |")
            print("+---------------------------------------------+")
    if opcao==2:
        calcular_fatorial()
    elif opcao==3:
        break
    else:
        print("+---------------------------------------------+")
        print("|                                             |")
        print("|             ESTA OPÇÃO NÃO EXISTE           |")
        print("|                                             |")
        print("+---------------------------------------------+")