def sumar(a, b):
    return b + a

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):

    try:
        return a / b
    
    except ZeroDivisionError:
        return "Error al dividir entre cero"


def operacion(funcion, a, b):
    return funcion(a, b) 


suma = sumar
resta = restar
mult = multiplicar
div = dividir
resultado = operacion(div, 10, 10)
print(resultado)


