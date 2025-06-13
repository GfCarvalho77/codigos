#abre
with open('material.txt', 'r') as arquivo:
    for linha in arquivo:
        #imprime
        print(linha.strip())

    #fecha