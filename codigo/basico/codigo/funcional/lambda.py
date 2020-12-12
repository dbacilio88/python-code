suma = lambda a, b: a + b
resta = lambda a, b: a - b
mult = lambda a, b: a * b
div = lambda a, b: a / b

operacion = lambda operacion, a, b: operacion(a, b)

resultado = operacion(div, 10 , 10)
print(resultado)