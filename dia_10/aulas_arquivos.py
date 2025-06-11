import os

def manipular_pasta_arquivos():
    os.mkdir('Nova_Pasta')
    print(f'Nova_Pasta criada')

    os.chdir('Nova_Pasta')

    with open('arquivo.txt', 'w') as arquivo:
        arquivo.write('Este é um arquivo de texto.\n')
    print('arquivo.txt criado na Nova_Pasta')

    arquivos=os.listdir('.')
    print(arquivos)

   
manipular_pasta_arquivos()