# Qué es la Herencia y para que sirve y como hacer que las clases hereden.
# Clase y superclases
# Principalmente se utiliza para la reutilizacion de código.
# Qué características en común, marca o modelo
# Qué comportamientos en comunm arrancar, aceleraban y frenan
# Englobar en una clase padre o superclase.
# sobre escritura de métodos.
# Herencia simple y múltiple

class Vehiculo():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True
    
    def acelera(self):
        self.acelera = True
    
    def frena(self):
        self.frena = True
    
    def estado(self):
        print("Marca: ", self.marca,
            "\nModelo: ", self.modelo,
            "\nEn Marcha: ", self.enMarcha,
            "\nAcelerando: ", self.acelera,
            "\nFrenando: ", self.frena)


class Furgoneta(Vehiculo):

    def cargar(self, cargar):
        self.cargado = cargar
        if(self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"



class Moto(Vehiculo):

    hCaballito = ""

    def caballito(self):
        self.hCaballito = "Haciendo Caballito"

    def estado(self):
        print("Marca: ", self.marca,
            "\nModelo: ", self.modelo,
            "\nEn Marcha: ", self.enMarcha,
            "\nAcelerando: ", self.acelera,
            "\nFrenando: ", self.frena,
            "\nCaballito: ", self.hCaballito )

moto = Moto("Honda","CRB")
moto.caballito()
#Llamando al método de la clase moto, cuando sobrescribe
moto.estado()


#Furgoneta
furgoneta = Furgoneta("Renault","Kangoo")
furgoneta.arrancar()
furgoneta.estado()
print(furgoneta.cargar(True))
