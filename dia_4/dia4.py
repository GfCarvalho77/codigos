""" clima = "nublado"

if clima== "ensolarado":
    print ("clima ensolarado")
elif clima == "nublado":
    print("clima nublado")
else:
    print("clima chuvoso") """
produto= None


idade=int(input("Qual sua idade?"))
if idade < 16 :
    print("Você não pode votar ainda")
elif idade > 16 and idade < 18 or idade >=65 :
    print("Voto para você é opcional.")
else:
    print ("Você é obrigado por lei a votar")