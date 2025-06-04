def add_nota(aluno):
    aluno["nota a"]= int(input("Informe nota A: "))
    aluno["idade"] = 18

aluno_teste={
    "nome": "João",
}

add_nota(aluno_teste)
print(aluno_teste)