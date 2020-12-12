#bucle range
for i in range(1,10,2): #1 inicio, 10 stop, 2 de cuanto en cuanto
    print(f"valor de la variable {i}") #f unir textos con variables

valido = False
email = input("Ingrese el email: ")

for i in range(len(email)):
    if email[i]=="@":
        valido=True

if valido:
    print("Email válido: ")
else:
    print("Email inválido")

