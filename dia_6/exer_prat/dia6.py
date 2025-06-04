peso=(float(input("Digite seu peso (kg)")))
altura=(float(input("Agora informe sua altura(m)")))

imc=peso/altura**2
imc=(round(imc,2))

if imc < 18.5:
    print(f"Seu IMC é {imc}. Você está abaixo do peso")
elif 18.5 <= imc <=24.9:
    print (f"Seu IMC é {imc}. Você com peso ideal.")
elif 25 == imc <= 29.99:
    print(f"Seu IMC é {imc}. Você está com sobrepeso.")
else:
    print(f"Seu IMC é {imc}. Você está com obesidade.")
