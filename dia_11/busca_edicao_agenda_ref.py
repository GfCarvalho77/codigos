#função para buscar e editar contatos em uma agenda telefônica
#Abre a agenda e a lê. A variável recebe linha por linha separada
#Cria um laço por toda extensão da agenda
#procura a linha que contem determinado nome
# Se encontrar, altera o telefone do contato

def alterar_telefone(nome_procurado, novo_telefone):
    with open('agenda.txt', 'r', encoding='utf-8') as file:
        linhas = file.readlines()  # Lê todas as linhas separadas

    for i in range(len(linhas)):
        # Procura a linha que contém o nome
        if linhas[i].strip() == f'Nome: {nome_procurado}':
            # A linha seguinte é o telefone
            linhas[i + 1] = f'Telefone: {novo_telefone}\n'
            print(f'Telefone do contato {nome_procurado} alterado com sucesso!')
            break  # Para de procurar depois de encontrar
    else:
        print(f'Contato {nome_procurado} não encontrado.')

    # Escreve as linhas alteradas de volta no arquivo
    with open('agenda.txt', 'w', encoding='utf-8') as file:
        file.writelines(linhas)