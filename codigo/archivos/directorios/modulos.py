import os

OUTPUT = "C:/Users/Developer/Documents/repositorio/gitlab/workspace-python/python/pildoras/archivos/output"
LINK = "https://matr1x.cubava.cu/top-12-mejores-temas-para-visual-studio-code/"
abspath = os.path.abspath(OUTPUT)
print("Ruta Absoluta: ", abspath)

basename = os.path.basename(OUTPUT)
print("Directorio base: ", abspath)

#Saber si un directorio existe:
exists = os.path.exists(OUTPUT)
print("Existe: ", exists )

#Ultimo acceso a un directorio:
getatime = os.path.getatime(OUTPUT);
print("Ultimo Acceso: ", getatime)

#Conocer tamaño del directorio:
getsize = os.path.getsize(OUTPUT)
print("Tamaño: ", getsize)

#Conocer si la ruta es:
#Un directorio
directorio = os.path.isdir(OUTPUT)
print("Es un directorio: ", directorio )
#Un archivo
file = os.path.isfile(OUTPUT)
print("Es un file: ", file )

#Una ruta absoluta
absoluta = os.path.isabs(OUTPUT)
print("Es una ruta absoluta: ", absoluta )

#Es un link .
link = os.path.islink(LINK)
print("Es una link: ", link )

#Es un punto de montaje
mount = os.path.ismount(OUTPUT)
print("Punto de montaje: ",mount)