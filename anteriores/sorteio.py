import random

numero_da_sorte = random.randint(1,11)
palpite=0

while palpite != numero_da_sorte:
    palpite=int(input("tente novamente: "))
    if palpite > numero_da_sorte:
        print("numero sorteado é menor")
    else:
        print("numero sorteado é maior")
print("Parabéns! Você acertou!!")