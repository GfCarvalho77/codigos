# numero só pode dividir por ele mesmo e 1
# precisa se maior que 1
# iterar num range de 2 => numero 
    # no laço cada numero é divido pelos anteriores
    # se for divisível ele não é primo

def calc_primo(numero):
    if numero <=1:
        return False
    for i in range(2,numero):
        if numero %i==0:
            return False
    return True

num=(input(f"Informe o algarismo: "))
num = (int(num))

calc_primo(num)

if calc_primo(num):
    print("É primo")
else:
    print ("Não é primo")

        
