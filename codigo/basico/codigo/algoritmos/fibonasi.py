# Funciones definidas
# El núcleo de la programación extensible es definir funciones. Python permite argumentos obligatorios y opcionales, argumentos de palabras clave e incluso listas de argumentos arbitrarios.


numeros = [1,2,3,4,5,6]
producto = 1

for n in numeros:
    producto = producto * n
    print(producto)

print('Producto es: ', producto)


frutas = ['Platano','Manzana','Pera']

cargar = [f.upper() for f in frutas]


a = list(enumerate(cargar))
print(cargar)
print(a)
