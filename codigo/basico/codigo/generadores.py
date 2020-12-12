#Generadores;
# Que son los generadores. son estructuras que extraen valores de una funcion y se van almacenar
# en objetos iterables que se pueden recorrer.
# Estos valores se almacenan de uno a uno
# Cada cez que un generardor almacena un valor, esta permanece en un estado pausado hasta que 
# se solicite el siguiete. Esta característica es conocida como Suspención de estado
# funcion tradicionar:

#def generarNumerosPares():
    #yield= instruccion clave, el contro de ejecucion paa a la funcion y yield construye un objeto iterable
    #despues de terminar de crear el objeto pasa a  un estado de suspencion.

    # ventajas: son más eficientes que las funciones tradicionales
    # muy útiles con listas de valores infinitos.
    # bajo determiandos escenarios, será muy útil que un generador devuelva los valores de uno en uno
    # Sintaxis: Def generafdorNumeros():
                    #yield numeros pero tambien tiene return.

#funcion 
def generarNumerosPares(limite):
    num = 1
    lista = []
    while num<limite:
        lista.append(num * 2)
        num=num+1
    return lista

print(generarNumerosPares(10))
print("===========================")
#funcion generadora
def generador(limite):
    num = 1
    while num < limite:
        yield num * 2
        num = num + 1

lista = generador(10)

print(next(lista))
print("Aquí mas código..")
print(next(lista))
print("Aquí mas código..")
print(next(lista))
print("Aquí mas código..")
print(next(lista))

#for i in lista:
#    print(i)|