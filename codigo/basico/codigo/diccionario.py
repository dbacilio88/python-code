#===========================================================================================================
#Estructura que nos permite almacenar valores de diferentes tipos(enteros, cadenas de texto, decimales)
#E incluso listas y otros diccionarios.
#La principal característica de los diccionarios es que los datos se almacenan asociados a una clave de tal
#forma que se crea una asociación de tipo clave:valor para cada elemento almacenado.
#Los elementos almacenados no estan ordenados. El orden es indiferente a la hora de almacenar informacion
#en un diccionario.
#===========================================================================================================
#Sintaxis: nombreDiccionario={"clave",elemento2} la clave puede se cualquier valor

nombreDiccionario={"Alemania":"Berlín","Francia":"París","Reino Unido":"Londres","España":"Madrid","Perú":"Lima"}
print(nombreDiccionario["Alemania"])
#Agragar elementos al diccionario:
nombreDiccionario["Italia"]="Lisboa"
print(nombreDiccionario)
#Modificar el valor de los diccionarios:
nombreDiccionario["Italia"]="Roma"
print(nombreDiccionario)
#Eliminar elemento:
del nombreDiccionario["España"]
print(nombreDiccionario)
#Cualquier elemento en un diccionario:
otroDiccionario={"Perú":"Lima",23:"Jordan","Mosqueteros":13}
print(otroDiccionario)
#Utilizar una tupla para asignar a los valores de los diccionarios:
mitupla=("España","Francia","Reino Unido","Alemania")
pais={mitupla[0]:"Madrid",mitupla[1]:"París"}
print(pais)

#Almacenar valores a un diccionario: y subdiccionarios
peru={24:"Departamentos","Nombre":"Perú","Provincias":{"ciudades":["Lima","Cusco","Junín"]}}
print(peru["Provincias"])
print(peru)

#devuelven las claves
print(peru.keys())
#devuelve los valores
print(peru.values())
#longirtud del diccionario
print(len(peru))