
total_geral=0

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

        grade_pontuações = {
            'f':    [32, 28, 25, 18, 15, 11, 7, 5],
            'm':    [50, 47, 44, 41, 38, 35],
            'd':    [55, 60, 65, 70]
        }

        def calculo_por_turno(grau_dificuldade,tentativas_restantes):
            resultado_por_turno = grade_pontuações.get(grau_dificuldade)
            return resultado_por_turno[tentativas_restantes-1]

        resultado_por_turno=(calculo_por_turno(grau_dificuldade,tentativas_restantes))
        print(f"Seu resultado neste turno foi {resultado_por_turno}")
        
        total_geral = total_geral + resultado_por_turno
        print(f"Total geral de pontos {total_geral}")

        
        jogar_de_novo=(input("Você deseja jogar novamente? (S/N)")).lower()
        if jogar_de_novo != 's':
            print("Fim de Jogo! Obrigado por jogar!")
            break