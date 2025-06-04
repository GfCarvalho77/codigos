frutas=['banana','pera','uva','abacaxi','mamão','laranja','bergamota']
frutas[3]='morango'

print(frutas[5])
print(frutas[6])

frutas.append('abacaxi')
print(frutas)

frutas.insert(4,'limão')
print(frutas)

frutas.insert(6,'Pitaia')
print(frutas)

frutas.append('banana')
print(frutas)

frutas.remove('uva')
print(frutas)

frutas.pop(9)
print(frutas)

frutas.insert(2,'uva')
print(frutas)

print(len(frutas))

if "maçã" in frutas:
    print("Maçã está em frutas")
else:
    print("Maçã não está na lista")

tupla_frutas=tuple(frutas)
print(tupla_frutas)

tupla_cores=("amarelo","vermelho","verde")
print(tupla_cores)

lista_cores=list(tupla_cores)
print(lista_cores)