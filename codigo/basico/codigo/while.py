import math
#===============================================================================
# Bucle: while: indeterminado.
#===============================================================================
#Sintaxis: While condicion:
                #Cuerpo del bucle
i = 1
while i <= 10: #mientras
    print("Ejecución " + str(1))       
    i = i + 1     
                            
print("Terminó la ejecución")  

edad = int(input("Ingrese su edad: "))
contador = 0
while edad < 5 or edad > 100:
    print("Edad Incorrecta: negativa, vuelva a intentarlo")
    edad = int(input("Ingrese su edad: "))
    contador = contador + 1

print("Gracias por colaborar, puedes continuar.")
print("Cantidad de errores: " + str(contador))
print("Tu edad es " + str(edad))
#como hacer q un bucle sea infinito.
#Raiz cuadrada de un número: positivo
print("Programa de cálculo de raíz cuadrada: ")
numero = int(input("Ingrese un número: "))
intentos = 0

while numero < 0:
    print("No se puede halla la raíz de un número negativo: ")

    if intentos == 2:
        print("Has consumido demasiados intentos. el programa ha finalizado. ")
        break;
    
    numero = int(input("Introduzca un número, por favor: "))
    if numero < 0:
        intentos = intentos + 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))



