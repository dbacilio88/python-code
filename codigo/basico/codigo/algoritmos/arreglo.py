import random

def generateArray(cant, init, stop):
    arreglo = []
    
    for i in range(int(cant)):
        numero = random.random() * stop  - init
        arreglo.append(round(numero))
    
    return arreglo
        
#print(generateArray(15,1,10))


