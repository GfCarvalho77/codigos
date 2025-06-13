frase_geral="Rato roeu a roupa do Rei de Roma Rato Rei Roma"
frase_analise=frase_geral.split()
print(frase_analise)

palavras_unicas=set(frase_analise)

print(palavras_unicas)

aluno = {
    "Nome": "Guilherme",
    "idade": 48,
    "Profissão": "Programador",
    "Curso" : "Análise de sistemas" 
}

print(aluno["Nome"])
aluno["CEP"]="83413-160"
print(aluno["CEP"])
aluno["Endereço"]="Rua Alípio da Silva, 301/Ap.15"
print(aluno["Endereço"])

del aluno["CEP"]
print(aluno)

for chave, valor in aluno.items():
    print(f'{chave}:{valor}')

#Conjuntos

lista=[1,1,2,2,3,3,4,4,5,5,6,7,8]
set_lista = set(lista)
print(set_lista)

set_lista.add(22)
print(set_lista)

set_lista.remove(4)
print(set_lista)

#Intersecção

conjunto_a={1,2,3,4,5}
conjunto_b={3,4,5,6,7,8,9}

intersecção=conjunto_a.intersection(conjunto_b)
print(intersecção)

união = conjunto_a.union(conjunto_b)
print(união)

diferença=conjunto_a.difference(conjunto_b)
print(diferença)

diferença_simétrica= conjunto_a.symmetric_difference(conjunto_b)
print(diferença_simétrica)