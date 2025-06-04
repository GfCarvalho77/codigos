números_aleatórios=("25 13 72 3 55 88 7 66 23")
#quebrar a string
numeros = [float(num) for num in números_aleatórios.split()]
print(numeros)

#ordem crescente
numeros_ordem_crescente = sorted(numeros)
print(numeros_ordem_crescente)
numeros_ordem_decrescente= sorted(numeros,reverse=True)
print(numeros_ordem_decrescente)