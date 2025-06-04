"""frutas=["maçã","pera","uva"]"""

"""#for fruta in frutas:
        print("Fruta:",fruta)"""

frutas=["maçã","pera","uva","abacaxi","pera","banana"]
"""for i in range(1,5):
    print("Fruta: ", frutas[i])"""

frutas=["maçã","pera","uva","abacaxi","pera","banana"]

"""i=0
while i <= len(frutas):
    print("Frutas",frutas[i])
    i+=1"""

"""print(frutas[i])"""

"""i=0
for i in range(15):
   if 6 <= i <=8: 
        continue
   print(i)"""

"""N=int(input("Digite intervalo multiplicação: "))
D=int(input("Digite multiplicador"))"""

"""for N in range(1,N+1):
    print(N,"x",D,"=",N*D)"""

#Quantos pares e ímpares
#range (n,z)
# pares => precisa ser divisível por 0
    # pares = p+=1
# ímpares => não podem ser divisíveis por 0
    # ímpares => pares = p+1=


N_inicial=int(input("Digite o numero menor: "))
N_final=int(input("Digite o numero menor: "))

if N_inicial > N_final:
    N_inicial , N_final = N_final, N_inicial

pares = 0
impares = 0

for i in range (N_inicial,N_final+1):
    if i % 2 == 0:
        pares+=1
    else:
        impares+=1
print("Números pares: ", pares)
print("Números ímpares: ", impares)