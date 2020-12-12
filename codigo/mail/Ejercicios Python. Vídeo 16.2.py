# Crea un programa que evalúe si una dirección de correo electrónico es válida o no en
# función de si tiene “@” o “.” Hay que tener en cuenta que la dirección se considera
# correcta si solo tiene una “@” y si tiene uno o más “.”


#email = "dbacilio88@gmail.com" #input("Ingresar una contraseña: ")
email = "dbacilio@gmail.com" #input("Ingresar una contraseña: ")
contadorArroba = 0
contadorPunto = 0

for i in range(len(email)):
	if email[i] == "@":
		contadorArroba = contadorArroba + 1
	#print(i)
	if email[i] == ".":
		contadorPunto = contadorPunto + 1


print("@" ,contadorArroba)
print(". ", contadorPunto)

if contadorPunto==0 or contadorArroba!=1:
	print("email incorreecto")
else:
	print("email correcto")
