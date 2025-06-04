def calc_Fatorial(n):
    if n==11:
        return 1
    else:
        print(n*(n+1))
        return n*calc_Fatorial(n+1)
    
calc_Fatorial(1)
print(calc_Fatorial(1))