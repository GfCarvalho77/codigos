texto = "Rato roeu roupa Rei de Roma Roma Rato roeu roupa Rei Rei Roma"
palavras = texto.split()

contagem={}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra]+=1
    else:
        contagem[palavra]=1
print(contagem)