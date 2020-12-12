#Crea un programa que pida por teclado introducir una contraseña. La contraseña no
#podrá tener menos de 8 caracteres ni espacios en blanco,
password =input("Ingresar una contraseña: ")
contador = 0

for i in range(len(password)):
	if password[i] == " ":
		contador = 1
	#print(i)

print(contador)
if len(password) != 8 or contador > 0:
	print("Passwor invalido. ")
else:
	print("Password correcto. ")