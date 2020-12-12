#===========================================================================================================
#Estructura de control de flujo (condicionales y bucles)
# Bucles: Tipos: bucle for, (repetir una o varias lineas de código n veces)
# Determinados: se ejecutan un número determinado de veces, se sabe a priori cuantas veces se va a ejecutar el 
# codigo del interior del bucle. 
# Indeterminados: Se ejecutan un numero indeterminado de veces, no se sabe a priori cuantas veces de va a 
# ejecutar el codigo del interior del bucle, el numero de veces que se ejecite dependera de las circunstancias
# durante la ejecucion del programa.
#===========================================================================================================
#Sintaxis: | Declaración del bucle:
#          |      Cuerpo del bucle  (n veces | o determinado de veces)
#          v    
# Bucle for (determinado).
# Sintaxis: for variable in elemento a recorrer: (lista, tupla, cadena de texto)
#               cuerpo del bucle  (con identación)

numeros = [1,2,3]

for i in numeros:
    print("número: ", i)

estaciones=["primavera", "verano", "otoño", "invierno"]

for e in estaciones:
    print("Estacion: " + e)


#bucle for, recorriendo strings, tipo range, notaciones especiales con print    
#https://www.datacamp.com/community/tutorials/python-print-function?utm_source=adwords_ppc&utm_campaignid=10267161064&utm_adgroupid=102842301792&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=278443377095&utm_targetid=aud-392016246653:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9060924&gclid=Cj0KCQjwgJv4BRCrARIsAB17JI4G4VUOZNkR9QODYAGLWlGmDaY65oEwPrKHqPWur6kHJuLQz1NiOmwaAkvQEALw_wcB
for i in ["Christian","Bacilio","De la Cruz"]:
    print(i) #end evita el saldo de línea
 
email = False #False o True en mayúscula
#my_email = input("ingrese su email: ")

#end = elimina el salto de línea

for i in "dbacilio88gmail.com":
#for i in my_email:
    if "@" and "." in i:
        email = True

    if(i == "@"):
        email = True


#if email == True:
if email:
    print("Email correcto. ")
else:
    print("Email incorrecto. ")


#bucle range
for i in range(5):
    print("Hola", i)