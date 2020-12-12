#Estructura de control de flujo (condicionales y bucles)
#Condicionales: flujo de ejecución de un programa:  Orden que se ejecutan sus intrucciones (compuesto por varias instrucciones)
#Condicionales: flujo de instrucciones: Arriba a abajo
# instruccion IF bloque, condicion a evaluar a nuestro programa si es verdad o es falsa.
#===========================================================================================================
#Sintaxis: | if  condicion
#          |      instriccion
#          v      instriccion



def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="desaprobado"   #sangria identación | ámbito de las variables: una variables solamente es accecible dentro de un ámbito
    return valoracion

#Cualquier valor que se ingresa por input es texto.
#ingresar un valor por teclado: int convierte a entero
print("Programa de evaluación de alumnos")
#input: admite parametros antes del cursos parpadeante.
nota = int(input("Ingrese la nota: "))
resultado = evaluacion(nota)
print(resultado)


        