import math

def evaluarEdad(edad):

    if edad < 0:
        raise ZeroDivisionError("No se permite edades negativas.") #Lanzamiendo de excepcion

    if edad < 20:
        return "Eres muy joven "
    elif  edad < 40:
        return "Eres joven "
    elif edad < 65:
        return "Eres maduro "
    elif edad < 100:
        return "Cuidate.."

print(evaluarEdad(15))



def calcularRaiz(numero):

    if numero < 0:
        raise ValueError("El numero no puede ser negativo: ")

    else:
        return math.sqrt(numero)

num = (int(input("Ingrese un número: ")))

try:
    print(calcularRaiz(num))
except ValueError as ErrorDeNumeroNegativo:  #as dar un alias
    print(ErrorDeNumeroNegativo)             #Imprimimos el error de la captura de exception.

print("Programa terminado.")