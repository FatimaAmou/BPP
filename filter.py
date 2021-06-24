def es_primo(n):
    primo=True
    for i in range(2,n-1):
        if (n % i == 0 ):
            primo = False
    return primo

numeros = [3, 4, 8, 5, 5, 22, 13,10,20]


primo= list(filter(es_primo, numeros))

print(primo)
