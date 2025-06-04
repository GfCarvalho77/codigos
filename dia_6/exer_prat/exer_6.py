#Adicionar tarefa
#Remover tarefa
#Listar tarefa

#Exibe Lista de Tarefas
Lista_de_Tarefas=[]
#Pergunta o que deseja fazer? Exibir, Adicionar, Remover (E,A,R) tarefas.
while True:
    print("\nMenu de tarefas: ")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Listar Tarefas")
    print("4. Sair")

    opcao = input("Escolha uma opção")

    if opcao == "1":
        tarefa = input("Informe a tarefa: ")
        Lista_de_Tarefas.append(tarefa)
        print("\nTarefa adicionada com sucesso! ")
        print(Lista_de_Tarefas)

    elif opcao =="2":
        
        for idx, tarefas in enumerate(Lista_de_Tarefas):
            print (idx, tarefas)
        
        idx = int(input("\nQual tarefa deseja remover? "))

        if 0 <= idx <(len(Lista_de_Tarefas)):
            removida=Lista_de_Tarefas.pop(idx)
            print(f"{removida}")
        else:
            print("Índice inválido!")

        #if tarefa_a_remover in Lista_de_Tarefas:
                #Lista_de_Tarefas.remove(tarefa_a_remover)
                #print("\nTarefa removida com sucesso!")
                #print(Lista_de_Tarefas)
                
            #else:
                #print("Erro! Esta tarefa não está na lista!")          
            
    elif opcao=="3":
        print(Lista_de_Tarefas)

    elif opcao=="4":
        print("Fim!")
        break
    

