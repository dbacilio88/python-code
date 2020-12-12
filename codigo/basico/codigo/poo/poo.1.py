# ¿Qué es POO?
# Ventajas de este paradigma de programación.
# 2 formas de programar: Paradigmas de la programación:
#   - Programacion orientada a procedimeintos:
#       Fortran, Cobol, Basic etc.
#       Desventajas: aplicaciones complejas, poco reutilizable, complejos de decifrar,
#       código muy grandes, si existe fallo, es muy probable que todo el progama caiga,
#       frecunete aparicion de código espagueti, dificil de depurar por otros programadores.     
#   - Programacion orientada a objetos:
#       Trasladar la naturalez de los objetos de la real al código de programación,
#       ¿Cuál es la naturaleza de un objeto de la vida real?, Los objetos tienen un estado, un comportamiento y las propiedades.
#       Java, C++, Visual Net, Javascript, etc.
#       Herencia, si existe algun fallo en alguna línea de código, el programa continuará, encapsulamiento.
#       Vocabulartio: Objeto, clase, 
#       
#Conceptos de POO:
# Clase: Modelo donde se redactan las caracteristicas comunies de un grupo de objetos:
#       chasis, ruedas, 
# Ejemplar de clase o objeto de clase perteneciente a una clase o Instancia de clase: 
# Modularización: Una aplicacion puede estar compuesta de varias clases.
# Encapsulación: 
# métodos de acceso. nomenclatura del punto.
#==========================
#Construcción de una clase:
#==========================

class Coche():

    #Estado inicial de un objeto: Constructor
    def __init__(self):
        #Propiedades:
        #Encapsulación proteger una propiedad para q no se pueda modificar. __
        self.__largoChasis = 250
        self.__abchoChasis = 150
        self.__ruedas = 4
        self.__enMarcha = False

    #Comportamiento: Métodos    : función especial que pertenece a la case. 
    #Comportamiento: Funciones  : función no pertene a una clase.

    #Encapsulación de métodos:

    def arrancar(self, arrancamos): #self hace referencia hacia el propio objeto pertenciente: a la instancia de la clase o igual al this en java
        
        self.__enMarcha = arrancamos

        if (self.__enMarcha):
            chequeo = self.__chequeo_interno()



        if (self.__enMarcha and chequeo):
            return "El coche está en marcha."
        elif(self.__enMarcha and chequeo == False):
            return "Algo ha ido mal en el chequeo, no podemos arrancar."
        else:
            return "El coche está parado."

    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un largo de ", self.__largoChasis, " y un ancho de ", self.__abchoChasis)

    
    def __chequeo_interno(self):
        print("Realizando chequeo interno...")
        self.gasolina="OK"
        self.acite = "Mal"
        self.pertas = "OK"

        if(self.gasolina == "OK" and self.acite=="OK" and self.pertas =="OK"):
            return True
        else:
            return False

miCoche = Coche() # instanciar una clase o ejemplar de clase.

print(miCoche.arrancar(True))
miCoche.estado()
print("<------ A continuación creamo el segundo objeto: ------> ")

miAuto = Coche()
print(miAuto.arrancar(False))
miAuto.estado()

    #Estado: