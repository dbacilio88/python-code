#ARCHIVOS
#Python nos permite trabajar en dos niveles diferentes con respecto al sistema de archivos y directorios
OUTPUT = "C:/Users/Developer/Documents/repositorio/gitlab/workspace-python/python/pildoras/archivos/output/archivo.txt"

#Los ficheros en python son objetos del tipo file.
#Crea el objeto con el función open(abrir): toma la cadena de la ruta del fichero a abrir
# puede ser relativa o absoluta, si no se especifica se accede en el modo lectura
# 'r' => read: lectura, el archivo tiene que existir previamente, en caso contrario lanzará
# un expecion del tipo FileNotFoundError
# 'w' => write: escritura, abre el archivo en modo escritura Si el archivo no existe se crea
# si existe sobrescribe el contenido
# 'a' => append: añadir, abre el archivo en modo escritura a diferencia del modo 'w' este no 
# sobrescribe, sino que empieza a escribir al final del archivo
# 'b' => binary: binario
# '+' => permite lectura y escritura simultanea
# 'U' => universar newline: saltos de linea universales, permite trabajar con archivos que tengan
# un formato para los saltos de linea que no coinicen con el de la plataforma actual.


#open() recibe dos parametros: el primero es la ruta del archivo que se desea abrir 
# y el segundo, el modo en el cual abrirlo
# cada vez que estamos abriendo un archivo estamos creando un puntero, en el cual se posicionará 
# en un lugar determinado dentro del archivo (comienzo o final) este podra moverse dentro de 
# este archivom eligiendo su nueva posicion, mediante el numero de bytes correspondiente.
file = open(OUTPUT,"w+")
#El método seek(#) mueve el puntero hacia el byte indicado
# seek(0) el puntero queda al final del documento.
#file.seek(1)

texto = "Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original"
file.write(texto)
file.close()