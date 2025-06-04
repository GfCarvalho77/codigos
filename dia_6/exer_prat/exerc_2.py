#entrada para inserir numeros(strings) (deixar espaço em branco)
entrada="1 5 8 35 42 76"
#transformar strings em números, lista
numeros=[float(num) for num in entrada.split()]
# determinar max/min/soma/media 

maior_numero=max(numeros)
menor_numero=min(numeros)
soma_numero=sum(numeros)
media_numero=float(soma_numero / (len(numeros)))
print(maior_numero)
print(menor_numero)
print(soma_numero)
print(media_numero)

