def fatorial(n):
    f=1
    for num in range (1, n+1):
        f=f*num
    return f

numero = 5
print(f'O fatorial do número {numero} é: {fatorial(numero)}')