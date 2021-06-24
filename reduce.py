from functools import reduce

import numpy as np

elementos= (np.random.random(60) for i in range(60))

def suma(a,b):
    return a+b

sumatoria= reduce(suma, elementos)
print(sumatoria)

acumulado=0
for i in elementos:
    acumulado +=1
print('Sumatoria sin reduce=', acumulado)