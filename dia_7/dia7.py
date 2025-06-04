#Notificar usuário do jogo e informar o numero de tentativas
#Determinar o numero de tentativas (Nt)
#Determinar o número secreto (Ns)
#Pedir o número determinado do usuário(Nu)
#looping para digito correto e tentativas 
#comparar o Nu  e Ns
# Se Nu == Ns parabenizar usuário e informar em quantas tentativas ele acertou
# Se Nu != Ns notificar erro e informar tentativas restantes
# Se Nt = 0 informar que jogo acabou e qual era o Ns
#perguntar se deseja jogar novamente

import random

while True:

    secreto = random.randint(1,15)
    palpite = 0
    tentativa = 0
    tentativas_restantes = 7

    print("Vamos jogar adivinhação? Você tem 5 tentativas!")
    

    while tentativas_restantes > 0:
        palpite = (input("Digite um numero de 1-15: "))
        if not palpite.isdigit():
            print("Digite um numero válido")
            continue

        palpite=int(palpite)
        tentativa += 1
        tentativas_restantes -= 1

        if palpite == secreto:
            print(f"Parabéns você acertou! Fez isso em {tentativa}(s)")
            break
        elif palpite < secreto:
            print (f"Errou! O número é maior.")
            print(f"Tentativas restantes: {tentativas_restantes}")
        else:
            print (f"Errou! O número é menor.")
            print(f"Tentativas restantes: {tentativas_restantes}")

    else:
        print(f"Você perdeu, acabaram as tentativas!")
        print (f"O número escolhido era {secreto}")

    jogar_novamente=input(f"Deseja jogar novamente? (S/N)").lower()
    if jogar_novamente !="s" :
        print('Obrigado por jogar! Até a próxima!')
        break