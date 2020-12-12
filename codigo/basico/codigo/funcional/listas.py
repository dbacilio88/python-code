import random

def arreglo(n):

    lista = []

    for i in range(n):
        numero = random.random() * i
        lista.append(round(numero))
    return lista

listar = arreglo(5)
print(listar)

def impares(lista):
    l = []
    for i in lista:
        #print(i)
        if i % 2 == 1:
            #print(i)
            l.append(i)
    return l

def pares(lista):
    l = []
    for i in lista:
        #print(i)
        if i % 2 == 0:
            #print(i)
            l.append(i)
    return l

print(impares(listar))
print(pares(listar))