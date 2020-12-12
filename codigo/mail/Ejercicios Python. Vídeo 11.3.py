#Ejercicio 1:
#Crea un programa que pida dos números por teclado. El programa tendrá una función
#llamada “DevuelveMax” encargada de devolver el número más alto de los dos
#introducidos.

a = int(input("Ingrese Número 1: "))
b = int(input("Ingrese Número 2: "))
c = int(input("Ingrese Número 3: "))

def media(a,b,c):
    total = a + b + c
    promedio =  total / 3
    return promedio

print("El promedio artimetico es: ", media(a,b,c))