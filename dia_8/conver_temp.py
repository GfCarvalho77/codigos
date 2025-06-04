#Conversor de Temperaturas
#Crie funções para converter temperaturas entre Celsius, Fahrenheit e Kelvin.
# escala inicial
# temp_incial
# escala final
#temperatura final
# escala final =>
    # escala inicial =>
    # temperatura final => temperatura_incial/escala inicial / escala final ser convertida=>

def celsius_para_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def celsius_para_kelvin(c):
    return c + 273.15

def kelvin_para_celsius(k):
    return k - 273

def kelvin_para_farenheit(k):
    return (k - 273.15) * 9/5 + 32

#informe a escala : celsius
#informe a temperatura: 34
# informe a escala desejada: kelvin

#if escala_desejada = kelvin:
    #if escala_original = celsius:
    #  celsius_para_kelvin(c)

escala_original=0
temperatura_inicial=0
escala_final=0
temperatura_final=0

while True:

    while True:
        escala_original=(input(f'Informe a escala original (C / K / F): ').lower())

        if escala_original in ['c','k','f']:
            break
        else:
            print ('Dado inválido! Informe corretamente!')
            continue
    
    while True:
        escala_final=(input(f'Informe a escala_final (C / K / F): ').lower())
        if escala_final in ['c','k','f']:
            if escala_original == escala_final:
                print(f"Erro! É a mesma escala! Original: {escala_original} e Final:{escala_final}. Escolha outra. ")
                continue
        
        else:
            print ('Dado inválido! Informe corretamente!')
            continue
        
    
        if escala_original == ('c').lower():
            c = (input(f'Informe a temperatura: '))
            c=(int(c))
            
            if escala_final== ('k').lower():
                kelvin= celsius_para_kelvin(c)
                print(f'A temperatura em kelvin é: {kelvin}')
                break

            elif escala_final == ('f').lower():
                celsius_para_fahrenheit(c)
                fahrenheit=celsius_para_fahrenheit(c)
                print(f'A temperatura em farenheit é: {fahrenheit}')
                break
        
        if escala_original == ('k').lower():
            k = (input(f'Informe a temperatura: '))
            k=(int(k))

            if escala_final== ('c').lower():
                celsius= kelvin_para_celsius(k)
                print(f'A temperatura em kelvin é: {celsius}')
                break

            elif escala_final == ('f').lower():
                fahrenheit=kelvin_para_farenheit(k)
                print(f'A temperatura em farenheit é: {fahrenheit:.2f}')
                break


    