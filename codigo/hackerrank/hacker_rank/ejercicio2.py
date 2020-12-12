#!/bin/python

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = 4

    check = {True: "Not Weird", False: "Weird"}

    print(check[
        n%2==0 and (
            n in range(2,6) or 
            n > 20)
    ])


    print ("Not Weird" if not n%2 and (n in range(2,6) or n>20) else "Weird")
    
    if n <= 5 and 2 >= n:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")
    else:
        print("Weird")



 # 
 #Consulte la pestaña Tutorial para saber cómo resolverlo.

#Tarea
#Dado un número entero,, realice las siguientes acciones condicionales:

#Si  es extraño, imprimir Weird
#Si  es uniforme y en el rango inclusivo de  a 2,5 impresión Not Weird
#Si  es uniforme y en el rango inclusivo de  a 6,20 impresión Weird
#Si  es uniforme y mayor que 20, impresión Not Weird
#Formato de entrada

#Una sola línea que contiene un número entero positivo, .

#Restricciones

#Formato de salida

#Imprime Weirdsi el número es extraño. De lo contrario, imprima Not Weird.

#Entrada de muestra 0

#