#Nome/ telefone / endereço
agenda={
    "Alexandra":{
        "idade": 47,
        "Endereço": "Pelotas/RS"
    }
}
print("Bem-Vindo a Agenda!")
print("Informe os dados cadastrais:\n")
while True:
    (print("O que você deseja fazer?\n Digite:\n (L) para listar \n (C) para cadastro\n (E) para editar\n (D) para deletar\n (S) para sair\n"))
    ação_inicial=input("Escolha uma opção: ").lower()

    if ação_inicial == 'e':
        nome_dados_a_editar=input(f"Informe nome para edição de dados: ")
        
        #verificar se nome está / ou não na lista
        if nome_dados_a_editar in agenda:
            #Deseja editar nome ou dados?

            #estando na lista, rolar os dados e perguntar o que editar.
            edição=input(print("Deseja editar nome [N] dados [D]:  ")).lower()

            if edição == 'n':
                nome_correto=input(print("Informe nome correto: "))

                agenda[nome_correto] = agenda[nome_dados_a_editar]
            
            del agenda[nome_dados_a_editar]

            print("Nome atualizado com sucesso.")

            for valor, chave in agenda

            if edição == 'd':
                for chave, valor in agenda[nome_dados_a_editar].items():
                    print(f"{nome_dados_a_editar.title()}\n")
                    print(f"{chave}:{valor}")
                
                nova_idade=input("Informe idade correta: ")
                novo_endereço=input("Informe novo endereço: ")

                agenda[nome_dados_a_editar]={
                    "idade": nova_idade,
                    "Endereço": novo_endereço
                }

        else:
            print("Pessoa não encontrada na agenda.")
        
        #mostrar cursos para mudar/não mudar


    
    if ação_inicial == 'l':
        for nome, dados in agenda.items():
            print(f"{nome.title()}:")

            for chave, valor in dados.items():
                print(f"{chave.title()}:{valor}")
            print(f"")

    if ação_inicial == 's':
        print("Obrigado, até a próxima!")
        break
    
    if ação_inicial == 'c':
     
        while True:
            nome_completo=input(f"Informe nome da pessoa (sair p/ encerrar): ")
            
            if nome_completo.lower() == 'sair':
                break
            nome=nome_completo.split()[0]
            idade=input(f"Digite idade de {nome}")
            endereço=input(f"Informe endereço de {nome}")
            agenda[nome]={
                "Idade": idade,
                "Endereço": endereço
                }
    


