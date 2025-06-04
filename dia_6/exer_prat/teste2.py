lista_de_compras = ["Arroz", "Feijão", "Macarrão", "Sabonete"]

for i in range(len(lista_de_compras)):
    print((i+1),'-',lista_de_compras[i])

for idx, item in enumerate(lista_de_compras):
    print((idx+1),'-',item)

remover=int(input("Informe o numero que deseja remover"))-1
if 0 <= remover < (len(lista_de_compras)):
    lista_de_compras.pop(remover)
    print(lista_de_compras)