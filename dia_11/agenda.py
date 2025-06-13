def agenda(nome, telefone, email):
    with open('agenda.txt', 'a', encoding='utf-8') as file:
        file.write(f'Nome: {nome}\n')
        file.write(f'Telefone: {telefone}\n')
        file.write(f'E-mail: {email}\n')
        file.write('------------------------\n')
    print(f'Contato {nome} adicionado à agenda com sucesso!\n\n')  

agenda('gfgf',88-99999999,'gfgdgdf@dfdsf.com')