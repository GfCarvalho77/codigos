def conversor_celsius(f):
    return (f-32) * 5/9

temperatura_farenheit = 80

temperatura_celsius = conversor_celsius(temperatura_farenheit)

print(f'{temperatura_celsius:.2f}')


def dados_de_soma():
    resultado= 5 + 3
    return resultado

print(dados_de_soma())

numero=8

def calcular():
    numero=10
    print(numero)
calcular()

contador = 7

def calculando():
    global contador
    contador +=1
    return contador

calculando()
print(contador)