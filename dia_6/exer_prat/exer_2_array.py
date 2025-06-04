entrada=(input(f"Digite 03 números: " ))
array=[float(num) for num in entrada.split()]
print(f'Array é {array}')
for num in array:
    print (num)

print(f"Você escolheu {array}")
maior=max(array)
menor=min(array)
soma=sum(array)
media=sum(array) / (len(array))
print(maior)
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
print(f'A soma dos números é {soma}')
print(f'A media dos números é {media}')