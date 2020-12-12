OUTPUT = "C:/Users/Developer/Documents/repositorio/gitlab/workspace-python/python/pildoras/archivos/output/archivo.txt"

file = open(OUTPUT,"r")
print(file.read())
mode = file.mode
name = file.name
closed = file.closed

print("Modo: ", mode)
print("Nombre: ", name)
#file.close()

if file.closed:
    print("EL archivo esta cerrado correctamente.")
else:
    print("El archivo permanece abierto.")

#Para cerrar de forma automatica sin necesidad de invocar al metodo
# close():
with open(OUTPUT,"r") as files:
    print(files.read())

print(files.closed)

#Cuando una estructura with finaliza, Python, automáticamente invoca al método
# close(), como se puede ver en el valor de la propiedad closed