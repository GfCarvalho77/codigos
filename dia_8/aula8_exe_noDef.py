#calculadora
#inserção de dois argumentos (a,b)
    #solicitação (input)
#definição da operação (+,-,*,/)


print("Bem-Vindo à Calculadora básica!")

while True:
    while True:
        a=(input(f"Informe o primeiro algarismo: "))
        if not a.isdigit():
            print("Dado inválido! Digite novamente")
            continue
        else:
            print(f"Você escolheu: {a}")
        break

    while True:
        b=(input(f"Agora o segundo algarismo: "))
        if not b.isdigit():
            print("Dado inválido! Digite novamente")
            continue
        break
    print(f"Você escolheu a:{a} e b:{b}")
    
    a=int(a)
    b=int(b)

    while True:
        operação = (input(f"Agora defina a operação: (+,-,*, /)"))
        if operação in ['+','-','*','/'] :
            if operação == '+':
                print(f'Você escolheu soma: +')
                calculo = a + b
                print(f'{a} + {b} = {calculo}')
                break

            if operação == '-':
                print(f'Você escolheu subtração: - .')
                calculo = a - b
                print(f'{a} - {b} = {calculo}')
                break

            if operação == '*':
                calculo = a * b
                print(f'{a} * {b} = {calculo}')
                break

            if operação == '/':
                calculo = (a / b)
                print(f'{a} / {b} = {calculo:.2f}')
                break
            
    novo_calculo=input(f"Deseja nova operação? (S/N)").lower()
    if novo_calculo !="s" :
        print('Obrigado por jogar! Até a próxima!')
        break
                

                

