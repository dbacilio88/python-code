#yield from: Utilidad: Simplificar el codigo de los generadores en el caso de ulizar bucles anidados.

def ciudades(*ciudades): # * va a recibir un numero indeterminado de elementos en forma de tupla:
    print(ciudades)
    for elemento in ciudades:
        #for i in elemento:
        yield  from elemento

retorno = ciudades("Lima","Junin","Tumbes","Callao")
print(next(retorno))
print(next(retorno))
