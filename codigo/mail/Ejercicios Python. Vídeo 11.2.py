#Ejercicio 1:
#Crea un programa que pida dos números por teclado. El programa tendrá una función
#llamada “DevuelveMax” encargada de devolver el número más alto de los dos
#introducidos.

a = input("Ingrese el Nombre: ")
b = input("Ingrese la Dirección: ")
c = input("Ingrese el Teléfono: ")

datos = []
datos.extend([a,b,c])
print("Los datos personales son: " + "[Nombre]= " + datos[0] + " [Dirección]= " + datos[1] + " [Teléfono]= " + datos[2])
