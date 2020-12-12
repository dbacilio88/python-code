
menu = "\nMenu:\n\t[1] Usuarios\n\t[2] Salir\n\tElegir:"

valor = True
while valor:
    opcion = (int(input(menu)))
    if opcion == 1:
        print("Hola")
    elif opcion == 2:
        valor = False
        print("Gracias: ")
        break


    
