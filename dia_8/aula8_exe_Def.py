#calculadora
#inserção de dois argumentos (a,b)
    #solicitação (input)
#definição da operação (+,-,*,/)

def soma(a,b):
    return a+b

def subtração(a,b):
    return a-b

def multiplicação(a,b):
    return a*b

def divisão(a,b):
    if b == 0:
        print("Erro => divisão por zero!!")
    else:
        return round (a/b,2)

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
                resultado= soma(a,b)                
                break

            elif operação == '-':
                print(f'Você escolheu subtração: - .')
                resultado= subtração(a,b)
                break

            elif operação == '*':
                resultado = multiplicação(a,b)
                break

            elif operação == '/':
                resultado = divisão(a,b)
                break
            else:
                print("Operação inválida!!")
            
    print(f"O resultado entre {a}{operação}{b}= {resultado}")
            
    novo_calculo=input(f"Deseja nova operação? (S/N)").lower()
    if novo_calculo !="s" :
        print('Obrigado por jogar! Até a próxima!')
        break
                

                

