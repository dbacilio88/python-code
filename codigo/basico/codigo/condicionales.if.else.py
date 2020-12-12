#else => y si no es verdad.
edad=int(input("Introduce su edad, por favor: "))

if edad<18:
    print("No puede pasar.")
elif edad > 100:
    print("Edad incorrecta.")    
else:
    print("Puede pasar.")

print("El programa ha finalizado. ")
