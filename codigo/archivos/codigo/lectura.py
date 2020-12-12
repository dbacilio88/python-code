#Para la lectura de archivos utilizaremos los metodos read, readline y realines.
#El metodo 'read' devuelve una cadena con el contenido del archivo o bien el 
# contenido de los primeros n bytes, si se especifica el tamaño maximo a leer.
#Lee el contenido del archivo, si se pasa la longitud de bytes solo leerá hasta
# la longitud indicada.
OUTPUT = "C:/Users/Developer/Documents/repositorio/gitlab/workspace-python/python/pildoras/archivos/output/archivo.txt"

file = open(OUTPUT,"r",1,"UTF-8")
# Lee el todos el contenido del archivo, si se pasa la longitud bytes, leera solo
# el contenido hasta la longitud indicada.

read = file.readline()
#readLine solo lee una linea del archivo
#readLine = file.readline()
#readLines lee tosas la slineas del archivo
#readLines = file.readlines()
#tell retorna la posicion actual del puntero
mas = file.read(file.tell() * 500)

if file.tell()> 50:
    file.seek(50)

print(mas)
print(read)

file.close()
#print(readLine)