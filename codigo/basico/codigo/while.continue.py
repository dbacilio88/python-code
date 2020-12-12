#Continue: saltar a la siguiente iteración del bucle. ignora
#pass: devolver null casos muy concretos.
#else: similar a un condicional.

for letra in "bacilio":
    if letra == "i":
        continue
    print("letras: " + letra)

nombre = "dbacilio88@ gmail.com"
contador = 0
for i in nombre:
    if i == " ": #ignora el espacio en blanco. y pasa a evaluar el siguiente
        continue 
    contador+=1

print(contador)
#for cantidad in nombre:

email = "dbacilio88gmail.com"

for i in email:
    if i=="@":
        arroba = True
        break;
else:
    arroba = False

print(arroba)
