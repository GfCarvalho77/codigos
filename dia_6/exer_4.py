frase="O Grêmio é campeão do Mundo".lower()
contagem={}

for letra in frase:#laço para analise das letras na frase
    if letra.isalpha(): #condição de analise somente das letras
        if letra in contagem: # 
            contagem[letra]+=1
        else:
            contagem[letra]=1

print(contagem)