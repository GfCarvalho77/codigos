#informar a quantidade sequencial
#criar a sequencia original e iniciá-la [0,2,2]
#criar laço (quantidade sequencial) => fazer somatório dos dois números antecessores e incluir na sequência original

quantidade_inicial=10
fibonacci=[0,1]

for n in range(quantidade_inicial-2):
    fibonacci.append(fibonacci[-1]+fibonacci[-2])

print(fibonacci)