#Notificar usuário do jogo e informar o numero de tentativas
#Determinar o numero de tentativas (Nt)
#Tentativas_restantes
#Determinar o número secreto (Ns)
#looping para digito correto e tentativas 
#Pedir o número determinado do usuário(Nu) e
#comparar o Nu  e Ns
# Se Nu == Ns parabenizar usuário e informar em quantas tentativas ele acertou
# Se Nu != Ns notificar erro e informar tentativas restantes
# Se Nt = 0 informar que jogo acabou e qual era o Ns
#perguntar se deseja jogar novamente



while True:     #Looping para repetir jogo até pedir pra cancelar
    import random

    numero_secreto= random.randint(1,15)    #define numero randômico
    tentativas=0
    tentativas_restantes=5    
    palpite=0

    
    print("Jogo de Adivinhação!! Você tem 05 tentativas")
    while tentativas_restantes > 0:
        palpite=(input(f"Digite um número de 1-15: "))
        
        if not palpite.isdigit(): #validação do dado
            print("Número inválido!!")
            continue

        palpite=int(palpite)
        tentativas +=1
        tentativas_restantes -=1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas}")
            break
        
        elif palpite > numero_secreto:
            print(f"O numero secreto é menor")
            print(f"{tentativas}ª tentativa")
        
        else:
            print(f"O número secreto é maior")
            print(f"{tentativas}ª tentativa")
        
    else:
        print(f"Acabaram suas tentativas!")
        print("O número secreto é: {numero_secreto}")
        
    jogar_de_novo = (input(f"Deseja jogar novamente?(S/N)")).lower()
    if jogar_de_novo !='s':
        print("Obrigado e até a próxima!")
        break



    
