#define palavra secreta
palavra_secreta='azerbaijão'
#cria um array (letras_secretas)em branco com para inserir as letras descobertas e informar quais ainda faltam.
letras_descobertas=["_"] * len(palavra_secreta)
letras_erradas=[]


#define quantas tentativas o usuário terá.
tentativas_restantes=8

#Cria um laço até que as tentativas se esgotem ou a palavra toda seja descoberta
while tentativas_restantes > 0 and "_" in letras_descobertas:
    
    #printar palavra semi-prenchida
    print("Palavra:" , " ".join(letras_descobertas))
   
    #input da letra_da_vez
    print("letras_erradas: ", (letras_erradas))
    print(f"Você possui: {tentativas_restantes} tentativas restantes")
    letra_da_vez=input("Informe a letra: ").lower()      

    #Cria uma condicional  para análise para letras_tentativas sobre palavra_secreta
    if letra_da_vez in palavra_secreta:
        #Se verdadeiro
        # Palavra_secreta é percorrida, é capturada cada letra e seu respectivo índice. Ali em cada laço a  letra_secreta é endereçada ao um índice.
        for idx, letra_atual_secreta in enumerate(palavra_secreta):  
                  
                    # Se letra_da_vez está em letra_atual_secreta => ela é adicionada a letras_secretas
                    if letra_da_vez == letra_atual_secreta:
                           letras_descobertas[idx]=letra_da_vez
                       
    else:
        print ("Você errou tente novamente!")
        tentativas_restantes -=1
        letras_erradas.append(letra_da_vez)
        
        
                                        

    #Falso notifica erro e informa quantidade de tentativas
    
    #subtrai tentativa
    

#Se em letras_secretas não houver "_"
    
         #Parabeniza jogador
            
        # Senão: Notifica que perdeu o jogo e informa qual palavra secreta.
        