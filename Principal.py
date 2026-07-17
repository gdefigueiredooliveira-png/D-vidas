from honoi import hanoi
from fatorial import calcular_fatorial

print(f"Bem vindo coleguinha\n")

while 0 == 0:
    print(f"Digite: \n1 para a função do coleguinha Cerbino  \n2-para a função do coleguinha Gabriel \n3-Para Encerrar")
    escolha = int(input("Digite sua opção:\n"))
    
    match escolha:
        
        case 1:
            numero = int(input("Digite um numero"))
            hanoi(numero)
        case 2:       
            calcular_fatorial()
        case 3:
            break
print("Encerrando...")
        
        