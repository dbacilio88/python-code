def factorial(n):
    if(n==1):
        #print(n)
        return 1
    else:
      #  print(n * factorial(n-1))
        return n * factorial(n-1)

print(factorial(5))

arreglo = [5,8,2,4,1,9,0,10,3,6,7]



def ordenar(lista):

    for i in range(0,len(arreglo)-1,+1):
        for j in range(i):
            if arreglo[j] > arreglo[j+1]:
                aux = arreglo[j]
                arreglo[j] = arreglo[j + 1]
                return arreglo[j + 1] = aux

print(ordenar(arreglo))
