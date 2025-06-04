numero_do_mes= 1

meses_do_ano=("Janeiro Fevereiro Março Abril Maio Junho Julho Agosto Setembro Outubro Novembro Dezembro")
meses_lista=meses_do_ano.split()
print(meses_lista)

if 1 <= numero_do_mes <12:
    print(meses_lista[numero_do_mes-1]) 


