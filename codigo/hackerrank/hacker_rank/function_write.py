def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))


"""Se agrega un día adicional al calendario casi cada cuatro años a partir del 29 de febrero, y el día se denomina día bisiesto .
    Corrige el calendario por el hecho de que nuestro planeta tarda aproximadamente 365,25 días en orbitar el sol. Un año bisiesto contiene un día bisiesto.

En el calendario gregoriano, se utilizan tres condiciones para identificar los años bisiestos:

El año se puede dividir uniformemente por 4, es un año bisiesto, a menos que:
El año se puede dividir uniformemente por 100, NO es un año bisiesto, a menos que:
El año también es divisible uniformemente por 400. Entonces es un año bisiesto.
Esto significa que en el calendario gregoriano, los años 2000 y 2400 son años bisiestos, mientras que 1800, 1900, 2100, 2200, 2300 y 2500 NO son años bisiestos. Fuente

Tarea

Dado un año, determine si es un año bisiesto. Si es un año bisiesto, devuelva el booleano True; de lo contrario, vuelva False.

Tenga en cuenta que el código auxiliar proporcionado lee de STDIN y pasa argumentos a la is_leapfunción. Solo es necesario completar la is_leapfunción.
"""