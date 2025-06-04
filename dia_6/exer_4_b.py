frase = "Aprender Python é aprender a pensar"
frase=frase.lower()
palavras= frase.split()
dicionario = {}

for palavra in palavras:
    if palavra.isalpha():
        if palavra in dicionario:
            dicionario[palavra] +=1
        else:
            dicionario[palavra]=1
        ...

# Mostrar o resultado
for palavra, quantidade in dicionario.items():
    print(f"A palavra '{palavra}' aparece {quantidade} vez(es)")

    print(palavras)