from arreglo import generateArray

def factorial(n):
    
    if(n==1):
        #print(n)
        return 1
    else:
      #  print(n * factorial(n-1))
        return n * factorial(n-1)

print(factorial(10))

arr = generateArray(15,1,100)

#arreglo = [5, 8, 2, 4, 1, 0, 3]

def ordenarBurbuja(lista):

    for i in range(0, len(lista)-1+1):
        for j in range(0, len(lista)-1):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j +1]
                lista[j + 1] = aux

def mostrarArrglo(lista):
    print(lista)

ordenarBurbuja(arr)
mostrarArrglo(arr)

