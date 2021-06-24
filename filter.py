def es_primo(n):
    primo=True
    for i in range(2,n-1):
        if (n % i == 0 ):
            primo = False
    return primo

numeros = [3, 4, 8, 5, 5, 22, 13]


primo= list(filter(es_primo, numeros))

print(primo)

numeros2= [20,21,27,28,30]

primo2= list(filter(es_primo, numeros2))