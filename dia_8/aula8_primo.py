
def calcula_primo(numero):
    for i in range(2,numero):
        if numero < 1:
            return False
        elif numero %i == 0:
            return False
    return True

num=(input(f"Digite um número:"))
num=(int(num))

if calcula_primo(num):
    print(f"Número {num} é primo")
else:
    print(f"Número {num} NÃO é primo")