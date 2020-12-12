#================================================================================================================
#Continuamos trabajando con condicionales en este vídeo. 
#Vemos la concatenación de operadores de comparación para evaluar varias condiciones encadenadas.
#Nota: no hay e switch en python
#Concatenación de operadores de comparación
#operadores lógicos and y or
#operador in
#================================================================================================================

edad = 107

if 0 < edad < 100:
    print("Edad es correcta.")
else:
    print("Edad es incorrecta.")


#Evaluar el salario de una empresa:

presidente = int(input("Ingresar el salario del Presidente: "))
director = int(input("Ingresar el salario del Director: "))
jefe = int(input("Ingresar el salario del Jefe: "))
adminitrativo = int(input("Ingresar el salario del Administrativo: "))
#covierte a string = str
print("[Salario del Presidente] ", presidente)
print("[Salario del Presidente] " + str( presidente))

if adminitrativo<jefe<director<presidente:
    print("Todo funciona correctamente.")
else:
    print("Algo falla en la empresa")

#and = traducir y si ademas
#or = o sino

#Otorgar beca
#distancia > 40Km
#hermanos > 2
#salario familiar <= 20000
#tiene q cumplir los tres requisitos.
#=================
#Ejercicio con and
#=================
print("Programa de Becas año 2020")
distancia = int(input("Introduce la distancia en Kilometros: "))
print(distancia)
hermanos = int(input("Introduce el número de hermanos: "))
print(hermanos)
salario = int(input("Introduce el salario bruto: "))
print(salario)

if  distancia > 40 and hermanos > 2 and salario<=20000:
    print("Tiene derecho a beca.")
else:
    print("No tiene derecho a beca.")

#and deberia cumplir todas las condiciones.    

#=================
#Ejercicio con or
#=================
print("Programa de Becas año 2020")
distancia = int(input("Introduce la distancia en Kilometros: "))
print(distancia)
hermanos = int(input("Introduce el número de hermanos: "))
print(hermanos)
salario = int(input("Introduce el salario bruto: "))
print(salario)

if  distancia > 40 and hermanos > 2 or salario<=20000:
    print("Tiene derecho a beca.")
else:
    print("No tiene derecho a beca.")


#=================
#Ejercicio con in
#=================
#permite evaluar varias condiciones.

print("Asignaturas opcionales año 2020. ")
print("Ing informatica, pruebas de software, usabilidad y accesibilidad")
carreras = input("Escribe la asignatura escogida: ")

if  carreras in ("Ing informatica","pruebas de software","usabilidad","accesibilidad"):
    print("Asignatura escogida: " + carreras)
else:
    print("La asignatura escogida no esta contemplada")


#python es case sensitive.
#lower() = transforma a minusculas
#upper() = transforma a mayusculas