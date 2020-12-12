#Estructura de datos que nos permite almacenar gran cantidad de valores.(Reservar varios espacios de memoria)
#En python ls listas pueden guardar diferentes tipos de valores a diferencia de otros lenguajes de programación.
#Se pueden expandir dinámicamente, añadiendo nuevos elementos.
#Definiendo una lista:
#Sintaxis de una lista en Python: nombreLista=["elemento1","elemento2"...] (indice = posición del elemento dentro de la lista, no es igual al número de la lista )
listas=["José",5,"Pepe",True,78.5]
#imprimir todo los elementos de la lista:
print(listas[:])
#imprimir segun el índice:
print(listas[0])
print(listas[-1])

print("===============================")
print("[lista]")
for a in listas:
    print(a)
print("===============================")

#Mostar la lista completa: - Porciones
print(listas[:])
#Debe acceder a los tres primeros elementos: 0 inclusive, 3 excusive
print(listas[0:3])
#Debe acceder a los tres primeros elementos: omitiendo el 0, 3 excusive
print(listas[:3])
#Debe acceder a los dos primeros elementos: omitiendo el 0, 3 excusive
print(listas[:2])
#Debe acceder a los dos primeros elementos: 1 inclusive, 3 excusive
print(listas[1:3])
#Debe acceder a los dos últimos elementos: 1 inclusive, omitimos el segundo indice
print(listas[2:])
#Agregar elementos a la lista: [APPEND] al final de la lista:
listas.append("Carlos")
print(listas[:])
#Agregar elemento en un indice especifico, punto intermendio. dependiendo del índice donde
#querramos agragar.
listas.insert(2,"Roberto")
print(listas[:])
#Agregar varios elementos, al final de la lista:(como si concatenaramos otra lista).
listas.extend(["Ernesto", "Ana"])
print(listas[:])
#Visualizar el índice de un elemento de una lista:
indice = listas.index("Ernesto")
print(indice)
#Verificar que un elemento se encuentra en una lista:
flat = "Pepe" in listas
print(flat)
#Eliminar elementos de una lista:
listas.remove("Ana")
print(listas[:])
#invertir la lista
listas.reverse()
print(listas[:])
#Eliminar el ultimo elemento de la lista:
listas.pop()
print(listas[:])
#Repite 3 veces (*)
a = ["Hola","Como estas?"] * 3
print(a[:])
b = ["Muy","Bien"]
c = a + b
print(c[:])
