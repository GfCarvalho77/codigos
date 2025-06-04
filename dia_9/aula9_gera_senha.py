#import random Importa o módulo random, que serve para gerar coisas aleatórias (números, escolhas, etc).

# import string Importa o módulo string, que tem conjuntos de caracteres prontos, como:

#string.ascii_letters: todas as letras maiúsculas e minúsculas (a-zA-Z)

#string.digits: os dígitos (0123456789)

#string.punctuation: símbolos como !@#$%^&*()_+ etc

import random
import string

def password_generator(tamanho):
    caracteres=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(caracteres) for i in range(tamanho))
    print(password)

password_generator(7)

def sorteio():
    #caracteres3=string.digits
    #na variável *num_sorteio* / são escolhidos(choice) de maneira aleatória(random) um determinado numero de caracteres (tamanho) que fazem parte de string digits sendo  unidos sem espaços(join)
    #num_sorteio6=''.join(random.choice(caracteres3) for _ in range(tamanho))
    # num_sorteio2=''.join(random.choice(caracteres3) for _ in range(3))
    # num_sorteio=''.join(random.choice(caracteres3) for i in range(tamanho))
    
    num_sorteio6=random.randint(0,15)
    print(num_sorteio6)

sorteio()