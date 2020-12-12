#Ejercicio 1:
#Crea un programa que pida dos números por teclado. El programa tendrá una función
#llamada “DevuelveMax” encargada de devolver el número más alto de los dos
#introducidos.

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

def DevuelveMax(_a,_b):
    if _a > _b:
        print(_a)
    elif _b > _a:
        print(_b)
    else:
        print("Son iguales.")

print("El número mayor es: ")
DevuelveMax(a,b)
