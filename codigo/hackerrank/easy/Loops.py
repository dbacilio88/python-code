"""
EL codigo proporcionado lee un entero n, de STDINm Para todos los enteros no negativos
i < n, impreciones i2
Ejemplo:
    n = 3
    La lista de enteros no negativos q n = 3 es [0,1,2] imprime el cuadrado de cada numero 
    en una linea.
    0
    2
    4
"""




if __name__ == "__main__":
    
    numero = input("Ingrese un numero: ")

    for i in range(int(numero)):
        print(i,i**2)

