import random

numero_da_sorte = random.randint(1,10)
palpite=0
tentativas=0

while palpite != numero_da_sorte and tentativas<5:
    palpite=int(input(f"tente adivinhar:  (tentativa nº{tentativas})"))
    tentativas+=1
    if palpite > numero_da_sorte:
        print("numero sorteado é menor")
        
    else:
        print("numero sorteado é maior")
        
if palpite == numero_da_sorte:
    print(f'Parabéns você acertou em {tentativas} tentativas')

else:
    print(f'Que pena o numero sorteado era {numero_da_sorte}')