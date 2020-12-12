#===========================================================================================================
#Estructura similar a las listas, las tuplas son inmutables, es decir no se pueden modificar 
#Despupés de su creación, no permite añadirm eliminar, mover elementos, etc (no append, no remove, no extend).
#Si permite extraer porciones, pero el resultado de la extraxion es una tupla nueva.
#No permite búsqueda (no index), Si permite comprobar si un elemento se encuentra en la tupla. ojo
#Qué utilidad o ventaja tienen al respecto de las listas?.(más rápidad, menos espacio, (mayor optimización)
#formatean strings, puede utilizarse como diccionario.) las listas no.
#===========================================================================================================
#Sintaxis: nombreTupla=(elemento1,elemento2,....) => paréntesis opcionales. índice igual que las listas.


mitupla=("Christian","Bacilio",30,"Masculino")
print(mitupla)
#Convertir una tupla a lista:
milista=list(mitupla)
milista.extend(["Huancayo","Junín"])
print(milista)
#Convertir una lista a tupla
tuplaNueva = tuple(milista)
print(tuplaNueva)
#Verificar si un elemento se encuentra en una tupla:
print("Christian" in tuplaNueva)

#cuantos elementos hay en nuestra tupla:
cantidad = tuplaNueva.count(30)
print(cantidad)
#longitud de una tupla:
print(len(tuplaNueva))

#Tuplas unitarias: se coloca una coma. para definir una tupla unitaria.
unico = ("David",)
print(unico)
print(len(unico))

#Tupla sin paarentesis. (Empaquetado de tupla)
parentesis = "carlos", 12, 12.3
print(parentesis)

#Desempaquetado de tuplas a variables.
nombre, apellido, edad, genero = mitupla
print(nombre)
print(apellido)
print(edad)
print(genero)
