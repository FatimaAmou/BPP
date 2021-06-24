

import pdb

pdb.set_trace()

def maximo(lista):
    return max(lista)

elementos =[[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

maximos= list(map(maximo,elementos))

print(maximos)

