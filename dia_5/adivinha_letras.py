#define palavra secreta
palavra_secreta='bergamota'
#cria um array (letras_secretas)em branco com para inserir as letras descobertas e informar quais ainda faltam.
letras_descobertas = ["_"] * len(palavra_secreta)
#define quantas tentativas o usuário terá.
tentativas_restantes=8

#Cria um laço até que as tentativas se esgotem ou a palavra toda seja descoberta
while "_" in letras_descobertas and tentativas_restantes > 0:
    print("Palavra:", " ".join(letras_descobertas))
    letra_da_vez=input("Digite uma letra: ").lower()

    #Cria uma condicional  para análise para letras_tentativas sobre palavra_secreta
    if letra_da_vez in palavra_secreta:
        #Se verdadeiro
            # Palavra_secreta é percorrida, é capturada cada letra (letras desta palavra) e seu respectivo índice. Ali em cada laço a  letra_secreta é endereçada ao um índice.
            for idx, letra_atual_secreta in enumerate(palavra_secreta):
                  if letra_da_vez == letra_atual_secreta:
                    # Se letra_da_vez está em letra_atual_secreta => ela é adicionada a letras_secretas            
                    letras_descobertas[idx]=letra_da_vez   
                    #Print letras secretas
                    print(letras_descobertas)

    #Falso notifica erro e informa quantidade de tentativas
    print("Você errou letra\nVocê ainda possui {tentativas_restantes} tentativa(s)")
    tentativas_restantes -=1

#Se em letras_secretas não houver "_"
    if "_" not in letras_descobertas:
         #Parabeniza jogador
        print("Parabéns você acertou palavras em {tentativas_restantes} tentativa(s)")    
        # Senão: Notifica que perdeu o jogo e informa qual palavra secreta.
        print("Que pena, você perdeu!! Palavra secreta era {palavra_secreta}")
           