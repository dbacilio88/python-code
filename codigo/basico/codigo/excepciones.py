#Que son las excepciones; Son errores que ocurren durante la ejecución del programa,
# la sintaxis de codigo es correcta pero durante la ejecución ha ocurrido "algo inesperado"
# error que el programador no tenia previsto.

def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):		
	return num1/num2
	

op1=(int(input("Introduce el primer número: ")))

op2=(int(input("Introduce el segundo número: ")))		
	
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")