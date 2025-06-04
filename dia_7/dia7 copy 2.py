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


#

while True:
    import random
    numero_secreto=random.randint(1,15)
    tentativas=0
    palpite=0
    
    
    print("Bem-vindo ao jogo de Adivinhação!")
    

    while True:
        print("Escolha seu nível de dificuldade: ")
        grau_dificuldade= input(f"(F)Fácil (M)Médio (D)Difícil").lower()
        print(f"Você escolheu {grau_dificuldade} ")

        if grau_dificuldade not in ("f", "m","d"):
            print("Algarismo inválido")
            print (f"você escolheu {grau_dificuldade}")
            continue
        
        if grau_dificuldade == "f":
            tentativas_restantes=8
        elif grau_dificuldade == "m":
            tentativas_restantes = 6
        else:
            tentativas_restantes= 4
        
        print(f"Você terá {tentativas_restantes} tentativas")

        palpites_feitos=[]

        while tentativas_restantes > 0:
            palpite=(input(f"Digite um número de 1-15:"))

            if not palpite.isdigit():
                print("Informação inválida! Digite novamente!")
                continue
            
            palpite=int(palpite)
            print(f"Seu palpite foi {palpite}")
            
            if 1 > palpite or palpite > 15:
                print ("Número Inválido!")
                continue
            
            if palpite in palpites_feitos:
                print("Este número você já palpitou")
                print(f"Palpites já feitos {palpites_feitos}")
                continue
            else:
                palpites_feitos.append(palpite)
                
            
            tentativas +=1
            tentativas_restantes -=1 

            
            if numero_secreto == palpite:
                print(f"Parabéns!! Você acertou em {tentativas}")
                break

            elif numero_secreto > palpite:
                print(f"Errou! Número secreto é maior")
                print(f"Você ainda tem {tentativas_restantes} tentativas")

            else:
                print(f"Errou! Número secreto é menor")
                print(f"Você ainda tem {tentativas_restantes}tentativas")

        else:
            print(f"Você perdeu. Acabaram-se as tentativas!")
            print(f"O número secreto era {numero_secreto}")
        
        jogar_de_novo=(input("Você deseja jogar novamente? (S/N)")).lower()
        if jogar_de_novo != 's':
            print("Fim de Jogo! Obrigado por jogar!")
            break