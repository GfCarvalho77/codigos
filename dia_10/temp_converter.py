import conversoes

temperatura_c=float(input("Digite a temperatura em °C: "))
temperatura_f=conversoes.fahrenheit_para_celsius(temperatura_c)
temperatura_k=conversoes.celsius_para_kelvin(temperatura_c)

print(f"{temperatura_c}°C equivalem a {temperatura_f:.2f}°F e {temperatura_k}K")